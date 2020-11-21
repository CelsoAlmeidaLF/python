import sqlite3

class DAO:
    def __init__(self):
        self.__init__
        pass

    def connect(self):
            self.mydb = sqlite3.connect('db.sqlite')
            
    def Set(self, xcmmd):
        try:
            self.connect()
            cmmd = self.mydb.cursor()
            cmmd.execute(xcmmd)
            cmmd.execute("SELECT * FROM CLIENT WHERE Nome = 'Nathalia'")
            print(cmmd.fetchall())
        except self.mydb.Error as sqlex:
            print("ERRO!: %s" % sqlex)
        pass

    def Get(self):
        try:
            self.connect()
            cmmd = self.mydb.cursor()
            cmmd.execute("SELECT * FROM CLIENT")
            print(cmmd.fetchall())
        except self.mydb.Error as sqlex:
            print("ERRO!: %s" % sqlex)
        pass

    def Up(self):
        try:
            self.connect()
            cmmd = self.mydb.cursor()
            cmmd.execute("UPDATE AS")
            cmmd.execute("SELECT * FROM CLIENT WHERE Nome = 'Nathalia'")
            print(cmmd.fetchall())
        except self.mydb.Error as sqlex:
            print("ERRO!: %s" % sqlex)
        pass

    def Del(self, arg):
        try:
            self.connect()
            cmmd = self.mydb.cursor()
            cmmd.execute("DELETE CLIENT WHERE Id = %s", arg)
            cmmd.execute("SELECT * FROM CLIENT WHERE Nome = 'Nathalia'")
            print(cmmd.fetchall())
        except self.mydb.Error as sqlex:
            print("ERRO!: %s" % sqlex)
        pass