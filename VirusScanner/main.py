#!/usr/bin/python

import sqlite3
import sys
import os
import requests
import _thread
import time

try:
    with open("API.txt", 'r') as af:
        APIKEY = af.readlines()
        print("reading your KEY API ... ")
        time.sleep(.2)
        af.close()
except:
    print("In order to proceed you need a KEY API from www.virustotal.com")
    print("You will only need to do this the first time")
    with open("API.txt", 'w') as af:
        APIKEY = input("paste your KEY API here\n#> ")
        af.write(APIKEY)
        print("generating your KEY API file ...\n ")
        time.sleep(3)
        print("All done. Your KEY API is now stored in the API.txt file, have fun!\n")
        af.close()

class VirusScanner:
    def __init__(self, url, database):
        try:
            self.scan(url)
            time.sleep(1)
            self.report(url, database)
        except ValueError as e:
            print(e)

    def scan(self, url):
        params = {'apikey': APIKEY, 'url': url}
        requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)

    def report(self, url, database):
        db = str(database)
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "gzip,  My Python requests library example client or username"
        }
        params = {'apikey': APIKEY, 'resource': str(url)}
        response = requests.post('https://www.virustotal.com/vtapi/v2/url/report',
                                 params=params, headers=headers)
        json_response = response.json()
        total = json_response['total']
        positive = json_response['positives']
        if db != "placeholder":
            database = Database(db)
            if positive == 0:
                database.addUrl(url, db, "safe")
                print("{} has been moved to the safe list".format(url))
            else:
                database.addUrl(url, db, "danger")
                print("{} has been moved to the danger list".format(url))
        else:
            print("\n[{}] has {} positive matches to possible viruses over {} total antiviruses queried".format(url,
                                                                                                                positive,
                                                                                                                total))
            print("\nPower by www.virustotal.com")


class Database:
    # ----------------------------SETUP------------------------------------------------------
    def __init__(self, database):
        self.database = sqlite3.connect(database)

    def createTable(self, database, table):
        database = sqlite3.connect(database)
        c = database.cursor()
        try:
            c.execute("""CREATE TABLE """ + table + """(
                            name text
                            )""")
            database.commit()
        except sqlite3.OperationalError as e:
            print(e)

    # ----------------------------DB MANAGEMENT------------------------------------------------------
    def addUrl(self, url, database, table):
        database = sqlite3.connect(database)
        c = database.cursor()
        fots = "{}".format(url)
        formattedUrl = fots.replace(')', '').replace('(', '').replace('\'', '').replace('\\n', '').replace(',',
                                                                                                           '').replace(
            "https://", "").replace("http://", "")
        try:
            c.execute("INSERT INTO " + table + " VALUES(:name)", {"name": formattedUrl})
            database.commit()
        except sqlite3.OperationalError as e:
            print(e)

    def scanTable(self, database, table):
        database = sqlite3.connect(database)
        c = database.cursor()
        db = []
        try:
            for url in c.execute("SELECT * FROM " + table):
                fots = str(url)
                formattedUrl = fots.replace(')', '').replace('(', '').replace('\'', '').replace('\\n', '').replace(',',
                                                                                                                   '')
                db.append(formattedUrl)
            self.scanFile(db, database)
        except sqlite3.OperationalError as e:
            print(e)

    def fetchAllUrlInDb(self, database, table):
        database = sqlite3.connect(database)
        c = database.cursor()
        try:
            c.execute("SELECT * FROM " + table)
            database.commit()
            print(c.fetchall())
        except sqlite3.OperationalError as e:
            print(e)

    def lookUpUrl(self, url, database, table):
        database = sqlite3.connect(database)
        c = database.cursor()
        try:
            c.execute("SELECT * FROM " + table + " WHERE name=:name", {"name": url})
            database.commit()
            print(c.fetchall())
        except sqlite3.OperationalError as e:
            print(e)

    def deleteTable(self, database, table):
        database = sqlite3.connect(database)
        c = database.cursor()
        try:
            c.execute("DROP TABLE " + table)
            database.commit()
            print("Table {} dropped".format(table))
        except sqlite3.OperationalError as e:
            print(e)

    # ----------------------------FILE MANAGEMENT------------------------------------------------------
    def loadFile(self, file, database):
        databb = sqlite3.connect(database)
        c = databb.cursor()
        table = "quarantine"
        with open(file) as f:
            line = f.readlines()
        lineNum = 0
        for lines in line:
            self.addUrl(lines, str(database), table)
            lineNum += 1
        f.close()
        print("{} urls has been added to the quarantine of the database {}".format(lineNum, database))
        db = []
        try:
            for url in c.execute("SELECT * FROM " + table):
                fots = str(url)
                formattedUrl = fots.replace(')', '').replace('(', '').replace('\'', '').replace('\\n', '').replace(',',
                                                                                                                   '').split(
                    " ")
                db.append(formattedUrl)
        except sqlite3.OperationalError as e:
            print(e)
        self.scanFile(db, database)

    def scanFile(self, file, database):
        maxCycles = 2  # edit this paramenter for more or less thread - public API only 4 scan per minute.
        while maxCycles > 0:
            if list:
                for urls in file:
                    print("start scanning {}...".format(urls))
                    try:
                        _thread.start_new_thread(VirusScanner, (urls, database))
                        time.sleep(5)
                    except _thread.error as e:
                        continue
                    file.remove(urls)
                    maxCycles -= 1
                    if maxCycles == 0:
                        print("60 seconds before the next scanning")
                        timer = 60
                        while timer > 0:
                            time.sleep(1)
                            timer -= 1
                            if (timer % 20 == 0):
                                print("{} seconds before the next scanning".format(timer))
                        self.scanFile(file, database)
                else:
                    sys.exit(0)


def main():
    argv = sys.argv
    if argv[1] == "-help" or argv[1] == "-h" or len(sys.argv) < 2:
        helpDesk()
    if argv[1] == "-tutorial":
        tutorial()

    if argv[1] == "-setup" or argv[1] == "-s":
        database = argv[2]
        if os.path.exists(database) == True:
            print("\n Error: {} already exist.\n".format(argv[2]))
            helpDesk()
            sys.exit(1)
        database = Database(database)
        table1 = "quarantine"
        table2 = "safe"
        table3 = "hazard"
        database.createTable(argv[2], table1)
        print("{} table has been created ...".format(table1))
        time.sleep(1)
        database.createTable(argv[2], table2)
        print("{} table has been created ...".format(table2))
        time.sleep(1)
        database.createTable(argv[2], table3)
        print("{} table has been created ...\n".format(table3))
        time.sleep(1)
        print("The setup is now complete. \n\nTo know more about how to use this tool type -help or -h")

    if argv[1] == "-loadFile" or argv[1] == "-lF":
        database = argv[3]
        database = Database(database)
        database.loadFile(argv[2], argv[3])

    if argv[1] == "-scanTable" or argv[1] == "-sT":
        database = argv[2]
        database = Database(database)
        database.scanTable(argv[2], argv[3])

    if argv[1] == "-createTable" or argv[1] == "-cT":
        database = argv[2]
        database = Database(database)
        database.createTable(argv[2], argv[3])

    if argv[1] == "-createFile" or argv[1] == "-cF":
        print("to exit type <close>")
        urlFile = input("Give a name to this file:\n")
        with open("{}.txt".format(urlFile), 'w') as af:
            while True:
                url = input("#> ")
                if url == "close":
                    break
                af.write("\n{}".format(url))
            af.close()
    if argv[1] == "-deleteTable" or argv[1] == "-dT":
        database = argv[2]
        database = Database(database)
        database.deleteTable(argv[2], argv[3])
        print("the table {} has been deleted".format(argv[3]))

    if argv[1] == "-fetchAllTable" or argv[1] == "-fA":
        database = argv[2]
        database = Database(database)
        database.fetchAllUrlInDb(argv[2], argv[3])

    if argv[1] == "-addUrl" or argv[1] == "-a":
        database = argv[3]
        database = Database(database)
        database.addUrl(argv[2], argv[3], argv[4])
        print("'{}' added in the database '{}', table '{}'.".format(argv[2], argv[3], argv[4]))

    if argv[1] == "-lookupUrl" or argv[1] == "-l":
        database = argv[3]
        database = Database(database)
        database.lookUpUrl(argv[2], argv[3], argv[4])

    if argv[1] == "-scanUrl" or argv[1] == "-sU":
        db = "placeholder"
        VirusScanner(argv[2], db)


def helpDesk():
    print("\n-----------------------------------------")
    print("\!/BEWARE THE APIKEY ALLOW ONLY 4 OPERATIONS PER MINUTE")
    print("-----------------------------------------\n")
    print("Usage: <file>.py [-flag] [OPTIONS]")
    print("Tutorial: <file>.py -tutorial\n")
    print("Options:")
    print("-setup".ljust(16) + "-s".ljust(16) + " {database}".ljust(19) + " #setup a database")
    print("-createFile".ljust(16) + "-cF".ljust(35) + " #make a txt file to add urls")
    print("-loadFile".ljust(16) + "-lF".ljust(6) + "{file.txt}".ljust(10) + " {database}".ljust(
        19) + " #add multiple urls from a file and scan them")
    print("-scanTable".ljust(16) + "-sT".ljust(16) + " {database} {table}".ljust(17) + " #scan a specific table")
    print("-createTable".ljust(16) + "-cT".ljust(16) + " {database} {table}".ljust(17) + " #create a table")
    print("-deleteTable".ljust(16) + "-dT".ljust(16) + " {database} {table}".ljust(17) + " #purge a table")
    print(
        "-fetchTable".ljust(16) + "-fT".ljust(16) + " {database} {table}".ljust(17) + " #fetch all the urls in a table")
    print(
        "-addUrl".ljust(16) + "-aU".ljust(10) + " {url} {database} {table}".ljust(24) + " #add a url to a table".ljust(
            25) + " | eg: www.beyondthelittlebluebox.com")
    print("-lookupUrl".ljust(16) + "-lU".ljust(10) + " {url} {database} {table}".ljust(
        24) + " #lookup a url in a table".ljust(
        25) + " | eg: www.google.com")
    print("-scanUrl".ljust(16) + "-sU".ljust(10) + " {url}".ljust(26) + "#fast scan a url online")
    print("-----------------------------------------")


def tutorial():
    print("-----------------------------------------")
    print("           WELCOME TO THE TUTORIAL")
    time.sleep(2)
    print("Step {}: setup a database".format(1))
    time.sleep(2)
    print("Step {}: create a file txt with some urls (one per line)".format(2))
    time.sleep(2)
    print("Step {}: use the command -loadFile or -lF file text and the name of the database".format(3))
    time.sleep(2)
    print("Step {}: wait until is done, then you can lookup the lists using the command lookup".format(4))
    time.sleep(2)
    print("Step {}: add your API key in line 21 - 28 or using the prompt during the setup".format(5))
    time.sleep(2)
    print("Step {}: \\!// be careful: to increase the number of threads edit the code at line 149".format(6))
    time.sleep(2)
    print("Step {}: to see the full list of commands type -help".format(5))
    print("-----------------------------------------")


if __name__ == '__main__':
    main()
