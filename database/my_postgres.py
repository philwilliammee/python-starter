#!/usr/bin/python
import psycopg2

class Postgress():
    """simple connection

    Returns:
        init -- interface for connection adapter
    """
    def __init__(self, database, user, password, host, port):
        self.conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()
        self.up_db()
        self.insert_db()
        self.query_db()
        self.down_db()
        self.close_db()

    def up_db(self):
        self.cur.execute('''CREATE TABLE TEST
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      NETID            CHAR(10)     NOT NULL);''')

        print("Table created successfully")

    def down_db(self):
        self.cur.execute('DROP TABLE "test";')
        self.conn.commit()

    def query_db(self):
        self.cur.execute("SELECT id, name, netid from TEST")
        rows = self.cur.fetchall()
        for row in rows:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("NETID = ", row[2])

    def insert_db(self):
        self.cur.execute("INSERT INTO TEST (ID,NAME,NETID) \
            VALUES (1, 'root', 'root1')")
        self.conn.commit()
        print("values inserted into user table")

    def close_db(self):
        self.conn.close()
