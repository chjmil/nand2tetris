import os
from enum import Enum

class instruction(Enum):
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2

class Parser():
    """
    """

    def __init__(self, input_file):
        self.input: str = input_file
        self.has_more_lines: bool = False
        self.instructionType: instruction = instruction.A_INSTRUCTION
        self.symbol: str = ""
        self.dest: str = ""
        self.comp: str = ""
        self.jump: str = ""

    def advance():
        pass

    def get_instruction_type(self):
        return self.instructionType
    
    def get_dest(self, input):
        """
        Returns the symbolic dest part of the current C-instruction
        """
        out = 0
        if 'M' in input:
            out += 1
        if 'D' in input:
            out += 2
        if 'A' in input:
            out += 4
        # Convert to binary, substring out the '0b', pad to 3 characters
        return f"{str(bin(out))[2:]}:0>3"

    def get_comp(self, input):
        """
        Returns the symbolic comp part of the current C-instruction
        """
        pass

    def get_jump(self, input):
        """
        Returns the symbolic jump part of the current C-instruction
        """
        if 'null' in input:
            out='000'
        elif 'JGT' in input:
            out = '001'
        elif 'JEQ' in input:
            out = '010'
        elif 'JGE' in input:
            out = '011'
        elif 'JLT' in input:
            out = '100'
        elif 'JNE' in input:
            out = '101'
        elif 'JLE' in input:
            out = '110'
        elif 'JMP' in input:
            out = '111'
        return out

    
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
