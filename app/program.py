import os
import sys
from app import *

class Program:
    """class Program"""
    def __init__(self):
        """contruct"""
        self.__init__
        self.db = Dao()
        pass
        
    def Program(self):
        """Method Init Program"""
        self.str = self.db.connect()
        print("Hi, %s" % self.str)

        self.Get()

        pass
        
    def Get(self):
        print("Program ...")
        pass

    def Set(self):
        print("Program ...")
        pass

if __name__ == "__main__":
    import sys
    prog = Program()
    prog.Program()