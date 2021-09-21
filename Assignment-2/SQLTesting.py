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

conn = psycopg2.connect("host=127.0.0.1 dbname=socialnetwork user=postgres password=postgres")
cur = conn.cursor()

cur.execute("drop table if exists influencers;")
cur.execute("create table influencers as select u.userid, u.name, count(userid1) as num_followers from users u join follows f on (u.userid = f.userid2) group by u.userid, u.name having count(userid1) > 10;")

cur.execute("drop trigger if exists update_influencers_on_insert on follows;")

cur.execute("drop table if exists friends_small;")
cur.execute("create table friends_small as select f.userid1, f.userid2 from friends f, users u1, users u2 where f.userid1 = u1.userid and f.userid2 = u2.userid and abs(extract(year from u1.birthdate) - extract(year from u2.birthdate)) < 5;")
conn.commit()

input('Press enter to proceed')

totalscore = 0
for i in range(0, 9):
    # If a query is specified by -q option, only do that one
    if args.query is None or args.query == i:
        try:
            if interactive:
                os.system('clear')
            print("========== Executing Query {}".format(i))
            print(queries[i])
            cur.execute(queries[i])

            if i in [1, 2, 3, 8]:
                ans = cur.fetchall()

                print("--------- Your Query Answer ---------")
                for t in ans:
                    print(t)
                print("")
            elif i in [4]:
                conn.commit()
                query_to_run = "SELECT userid, name, num_friends(userid) FROM users ORDER BY userid"
                print("--------- Running {} -------".format(query_to_run))
                cur.execute(query_to_run)
                ans = cur.fetchall()
                print("-- Result (should have appropriate friend counts)")
                for t in ans:
                    print(t)
                print("")
            elif i in [5]:
                conn.commit()
                query_to_run = "SELECT userid, user_details(userid) FROM users ORDER BY userid LIMIT 5"
                print("--------- Running {} -------".format(query_to_run))
                cur.execute(query_to_run)
                ans = cur.fetchall()
                print("-- Result (should have appropriate JSON outputs)")
                for t in ans:
                    print(t)
                print("")
            elif i in [6]:
                conn.commit()
                query_to_run = 'SELECT n.nspname as "Schema", p.proname as "Name", pg_catalog.pg_get_function_result(p.oid) as "Result data type" FROM pg_catalog.pg_proc p LEFT JOIN pg_catalog.pg_namespace n ON n.oid = p.pronamespace WHERE p.proname = \'update_influencers_on_insert\'' 
                print("--------- Running {} -------".format(query_to_run))
                cur.execute(query_to_run)
                ans = cur.fetchall()
                print("-- Result (should list the trigger function)")
                for t in ans:
                    print(t)
                print("")
            elif i in [7]:
                conn.commit()
                query_string = "insert into follows values('user0', 'user81')"
                cur.execute(query_string)
                conn.commit()
                query_string = "insert into follows values('user0', 'user2')"
                cur.execute(query_string)
                conn.commit()
                query_string = "insert into follows values('user1', 'user2')"
                cur.execute(query_string)
                conn.commit()
                query_string = "select * from influencers order by userid"
                print("--------- Running {} -------".format(query_string))
                cur.execute(query_string)
                ans = cur.fetchall()
                print("-- Result (should list user81 with 12 and user2 with 12)")
                for t in ans:
                    print(t)
                print("")
                
            if interactive:
                input('Press enter to proceed')
                os.system('clear')
        except:
            print(sys.exc_info())
            raise
