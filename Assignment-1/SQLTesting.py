import psycopg2
import os
import sys
import datetime
from collections import Counter
from types import *
import argparse

from queries import *

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interactive', help="Run queries one at a time, and wait for user to proceed", required=False, action="store_true")
parser.add_argument('-q', '--query', type = int, help="Only run the given query number", required=False)
args = parser.parse_args()

interactive = args.interactive

conn = psycopg2.connect("dbname=socialnetwork user=postgres")
cur = conn.cursor()

cur.execute("drop table if exists userscopy;")
cur.execute("create table userscopy as select * from users;")
conn.commit()
input('Press enter to proceed')

totalscore = 0
for i in range(0, 25):
    # If a query is specified by -q option, only do that one
    if args.query is None or args.query == i:
        try:
            if interactive:
                os.system('clear')
            print("========== Executing Query {}".format(i))
            print(queries[i])
            cur.execute(queries[i])

            if i not in [21, 22, 23, 24]:
                ans = cur.fetchall()

                print("--------- Your Query Answer ---------")
                for t in ans:
                    print(t)
                print("")
            else:
                if i in [21, 22]:
                    conn.commit()
                    print("--------- Running SELECT * FROM userscopy LIMIT 5 -------")
                    cur.execute("select * from userscopy limit 5")
                    ans = cur.fetchall()
                    print("-- Result (should have two more columns)")
                    for t in ans:
                        print(t)
                    print("")
                elif i in [23]:
                    conn.commit()
                    print("--------- Running SELECT * FROM userscopy ORDER BY birthdate-------")
                    cur.execute("select * from userscopy order by birthdate")
                    ans = cur.fetchall()
                    print("-- Result (should not have any birthdates in May)")
                    for t in ans:
                        print(t)
                    print("")
                else:
                    conn.commit()
                    print("--------- Running SELECT * FROM userscopy WHERE userid like 'newuser%' -------")
                    cur.execute("select * from userscopy where userid like 'newuser%'")
                    ans = cur.fetchall()
                    print("-- Result (should list 10 new users)")
                    for t in ans:
                        print(t)
                    print("")
                
            if interactive:
                input('Press enter to proceed')
                os.system('clear')
        except:
            print(sys.exc_info())
            raise
