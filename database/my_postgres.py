#!/usr/bin/python
import psycopg2

class Postgress():
    """simple connection

    Returns:
        init -- interface for connection adapter
    """
    def __init__(self, database, user, password, host, port, LOGGER):
        self.conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.logger = LOGGER
        self.table_name = "test"
        self.cur = self.conn.cursor()
        self.logger.debug("conected to db: {}".format(database))
        self.up_db()

    def clean_up(self):
        self.down_db()
        self.logger.info("closing DB connection")
        self.conn.close()

    def up_db(self):
        try:
            self.cur.execute('''CREATE TABLE {}
                (ID       SERIAL,
                NAME      TEXT        NOT NULL,
                NETID     CHAR(10)    NOT NULL);'''.format(self.table_name))
            self.logger.warning("created {} table".format(self.table_name))
        except psycopg2.errors.lookup("42P07"):
            #42P07 = psycopg2.errors.DuplicateTable:
            self.logger.critical("table already exists")

    def down_db(self):
        self.cur.execute('DROP TABLE "{}";'.format(self.table_name))
        self.conn.commit()
        self.logger.warn("deleted {} table".format(self.table_name))

    def insert_db(self, user, netid):
        self.cur.execute("INSERT INTO {} (NAME,NETID) \
            VALUES ('{}', '{}')".format(self.table_name, user, netid))
        self.conn.commit()
        self.logger.info("inserted {} {} into {} table".format(user, netid, self.table_name))

    def get_rows(self):
        self.logger.debug("fetching all rows in {} table".format(self.table_name))
        self.cur.execute("SELECT id, name, netid from {}".format(self.table_name))
        return self.cur.fetchall()
