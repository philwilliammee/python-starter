"""Connects to a Postgres DB

Returns:
    obj -- an example of a postrges db conection for testing.
"""
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
        """deletes the table and closes connection
        """
        self.down_db()
        self.logger.info("closing DB connection")
        self.conn.close()

    def up_db(self):
        """Creates a table if the table exists does nothing
        """
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
        """drops table from the db
        """
        self.cur.execute('DROP TABLE "{}";'.format(self.table_name))
        self.conn.commit()
        self.logger.warning("deleted {} table".format(self.table_name))

    def insert_db(self, user, netid):
        """inserts a row in the table

        Arguments:
            user {str} -- a user name
            netid {str} -- the netid of the user
        """
        self.cur.execute("INSERT INTO {} (NAME,NETID) \
            VALUES ('{}', '{}')".format(self.table_name, user, netid))
        self.conn.commit()
        self.logger.info("inserted {} {} into {} table".format(user, netid, self.table_name))

    def get_rows(self):
        """fetch all the rows

        Returns:
            array -- id, name and netid, of all rows in the table
        """
        self.logger.debug("fetching all rows in {} table".format(self.table_name))
        self.cur.execute("SELECT id, name, netid from {}".format(self.table_name))
        return self.cur.fetchall()
