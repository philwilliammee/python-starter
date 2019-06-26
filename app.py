#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on June 11, 2019
@author: psw58
"""
import argparse
import example_settings as settings
import example_resource
import my_postgres as DB

LOGGER = settings.LOGGER
example_resource.example_resource(settings)
class App():
    """
    example app that connects to postgres db
    """
    def __init__(self):
        """
        initialize the app
        """
        self._db = DB.Postgress(**settings.DB_CONN)

    def set_row(self, user, netid):
        """
        set the user value in DB test table
        Arguments:
            user {string} -- name
            netid {string} -- netid
        """
        self._db.insert_db(user, netid)

    def get_row(self):
        """ get the message
        Returns:
            string -- your message
        """
        rows = self._db.get_rows()
        my_string = (("Name={}, Netid={}".format(row[1], row[2])) for row in rows)
        return "".join(my_string)

    def close(self):
        """ roll everything back
        """
        self._db.clean_up()

if __name__ == "__main__":
    # typical ussage
    PARSER = argparse.ArgumentParser(
        description="Python test script. Save a message"
    )
    PARSER.add_argument('-u', help="Give me a username")
    PARSER.add_argument('-n', help="Give me a netid")
    ARGS = PARSER.parse_args()
    LOGGER.debug("starting App")
    UNAME = ARGS.u if ARGS.u else "John Doe"
    UNETID = ARGS.n if ARGS.n else "jd123"
    APP = App()
    LOGGER.debug("Setting user %s with netid %s", UNAME, UNETID)
    APP.set_row(UNAME, UNETID)
    RET = APP.get_row()
    LOGGER.info("Received message: %s", RET)
    APP.close()
    print("finished with success")
