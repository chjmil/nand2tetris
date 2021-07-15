import sys
from enum import Enum
import re

class instruction(Enum):
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2

class Parser():
    """
    """

    def __init__(self, input_file):
        self.input: str = ""
        self.current_line = 0
        self.comp_map = {
            '0': '0101010',
            '1': '0111111',
            '-1': '0111010',
            'D': '0001100',
            'A': '0110000',
            'M': '1110000', 
            '!D': '0001101',
            '!A': '0110001',
            '!M': '1110001', 
            '-D': '0001111',
            '-A': '0110011',
            '-M': '1110011', 
            'D+1': '0011111',
            'A+1': '0110111',
            'M+1': '1110111', 
            'D-1': '0001110',
            'A-1': '0110010',
            'M-1': '1110010', 
            'D+A': '0000010',
            'D+M': '1000010', 
            'D-A': '0010011',
            'D-M': '1010011', 
            'A-D': '0000111',
            'M-D': '1000111', 
            'D&A': '0000000',
            'D&M': '1000000', 
            'D|A': '0010101',
            'D|M': '1010101', 
        }
        self.jump_map = {
            None: '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }

        # read input file
        with open(input_file, 'r') as f:
            self.input =  f.readlines()
        
        self.advance()

    def advance(self):
        """
        Loop through the file and translate it
        """
        out = []
        # dest = comp ; jmp - dest and jmp are optional
        c_instruct_regex = re.compile(r"((.*?)=)?([^;\n]+)(;(.*))?")
        for line in self.input:
            if line[:2] == '//' or line == '\n':
                # comment - ignore and don't increment
                continue
            elif line[0] == '@':
                # symbol
                # TODO this doesn't work for variables
                bin_num = bin(int(line[1:]))
                out.append(f"{bin_num[2:]:0>16}")
            else:
                # Instruction
                sections = c_instruct_regex.match(line)
                # 2 = dest, 3 = comp, 5 = JMP
                dest = self.get_dest(sections[2])
                comp = self.get_comp(sections[3])
                jmp = self.get_jump(sections[5])
                c_instruct = f"111{comp}{dest}{jmp}"
                out.append(c_instruct)                

            # increment and loop
            self.current_line += 1
        
        for i in out:
            print(i)
            
    def get_dest(self, input):
        """
        Returns the symbolic dest part of the current C-instruction
        """
        out = 0
        if input == None:
            return '000'
        if 'M' in input:
            out += 1
        if 'D' in input:
            out += 2
        if 'A' in input:
            out += 4
        # Convert to binary, substring out the '0b', pad to 3 characters
        return f"{str(bin(out))[2:]:0>3}"

    def get_comp(self, input):
        """
        Returns the symbolic comp part of the current C-instruction
        """
        return self.comp_map[input]

    def get_jump(self, input):
        """
        Returns the symbolic jump part of the current C-instruction
        """
        return self.jump_map[input]

class SymbolTable():

    def __init__(self):
        """
        Create an empty symbol table
        """
        self.symbol_table = dict()
    
    def add_entry(self, symbol: str, address: int):
        """
        Add <symbol, address> to the table
        @param symbol: symbol to add
        @param address: address to add the symbol under
        """
        self.symbol_table[address] = symbol
    
    def contains(self, symbol: str):
        """
        Does the symbol table contain the given symbol?
        @param symbol: symbol to search for
        @return true if symbol exists in table
        """
        return symbol in self.symbol_table

    def get_address(self, symbol:str):
        """
        Returns the address associated with the symbol
        @param symbol: symbol to search for
        @return address associated with symbol
        """
        return self.symbol_table.get(symbol, "")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Expecting one argument, got {len(sys.argv)-1}")
        print(f"Use: python Assembler.py <path-to-file>")
        exit(1)
    parser = Parser(sys.argv[1])