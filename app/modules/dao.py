import sqlite3
class DAO:
    def __init__(self):
        self.__init__
        pass

    def connect(self):
            self.mydb = sqlite3.connect('db.sqlite')
            
    def Set(self, xcmmd):
        self.connect()
        cmmd = self.mydb.cursor()
        cmmd.execute(xcmmd)
        cmmd.execute("SELECT * FROM CLIENT WHERE Nome = 'Nathalia'")
        print(cmmd.fetchall())
        pass

    def Get(self):
        self.connect()
        cmmd = self.mydb.cursor()
        cmmd.execute("SELECT * FROM CLIENT")
        print(cmmd.fetchall())
        pass

    def Up(self):
        pass

    def Del(self):
        pass