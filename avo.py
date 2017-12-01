import sqlite3
import sys
import os.path


def helpDesk():
    print("-----------------------------------------")
    print("Usage: AVO.py [OPTIONS]")
    print("Options:")
    print("-setup".ljust(16)+" {database}".ljust(19)+" #setup a database")
    print("-purge".ljust(16)+" {database} {table}".ljust(17)+" #purge a table")
    print("-add".ljust(10)+" {url} {database} {table}".ljust(24)+" #add a url to a table")
    print("-lookup".ljust(10)+" {url} {database} {table}".ljust(24)+" #lookup a url in a table")
    print("-fetchAll".ljust(16)+" {database} {table}".ljust(17)+" #fetch all the url in a table")
    print("-scan".ljust(16)+" {database} {table}".ljust(17)+" #performe an online scan on the table")
    print("-file".ljust(16)+" {database} {table}".ljust(17)+" #add multiple url from a file")
    print("-----------------------------------------")


class Database:
    def __init__(self, database):
        self.database = sqlite3.connect(database)

    def createTable(self, name):
        c = self.database.cursor()
        c.execute("""CREATE TABLE """ + name + """(
            name text,
            domain text
            )""")
        self.database.commit()

    def insert(self, name, domain, database, table):
        database = sqlite3.connect(database)
        c = database.cursor()
        c.execute("INSERT INTO " + table + " VALUES(:name, :domain)", {"name": name, "domain": domain})
        database.commit()

    def fetchAll(self, database, table):
        database = sqlite3.connect(database)
        c = database.cursor()
        c.execute("SELECT * FROM " + table)
        database.commit()
        print(c.fetchall())

    def purge(self):
        print("purged")

    def add(self, url, database, table):
        name, domain = url.replace("www.", "").split(".")
        self.insert(str(name), str(domain), str(database), str(table))

    def lookUp(self, database, table, url):
        database = sqlite3.connect(database)
        c = database.cursor()
        c.execute("SELECT * FROM " + table + " WHERE name=" + url)
        self.database.commit()
        print(c.fetchall())


if __name__ == '__main__':
    argv = sys.argv
    if len(sys.argv) < 2:
        print("AVC.py -help for more information\n")
    if argv[1] == "-help":
        helpDesk()
    if (argv[1] == "-setup"):
        database = argv[2]
        try:
            if os.path.exists(database) == True:
                print("\n \!/ Error: {} already exist.\n".format(argv[2]))
                helpDesk()
                sys.exit(1)
            database = Database(database)
            table1 = input("table 1 name\n")
            table2 = input("table 2 name\n")
            database.createTable(table1)
            database.createTable(table2)
            print("Setup complete!\n")
        except sqlite3.OperationalError as e:
            print("Error: {}".format(e))
    if (argv[1] == "-delete"):
        helpDesk()
    if (argv[1] == "-purge"):
        database = argv[3]
        database = Database(database)
        database.purge()
    if (argv[1] == "-add"):
        url = argv[2]
        database = argv[3]
        table = argv[4]
        database = Database(database)
        database.add(argv[2], argv[3], argv[4])
    if argv[1] == "-fetchAll":
        database = argv[2]
        table = argv[3]
        database = Database(database)
        database.fetchAll(argv[2], argv[3])
