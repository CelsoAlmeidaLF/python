import sqlite3
class DAO:
    def __init__(self):
        self.__init__
        pass

    def connect(self):
        str = "conection ..."

        self.mydb = sqlite3.connect('db.sqlite')
        cmd = self.mydb.cursor()

        # cmd.execute("CREATE TABLE CLIENT ( Nome Text, Idade Integer, email Text )")
        # cmd.execute("INSERT INTO CLIENT VALUES (
        #       'Nathalia', 22, 'celso.almeida.leite@hotmail.com')")
        # self.mydb.commit()

        cmd.execute("SELECT * FROM CLIENT")
        print(cmd.fetchall())

        return str