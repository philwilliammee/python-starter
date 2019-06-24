#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on June 11, 2019
@author: psw58
"""
import argparse
import example_settings as settings
import example_resource

LOGGER = settings.LOGGER
example_resource.example_resource(settings)
class App():
    """
    example app
    """
    def __init__(self):
        """
        initialize the app
        """
        print(settings.DIRNAME)
        self.message = "initialized"

    def set_message(self, message):
        """
        set the messager value
        Arguments:
            message {string} -- your message
        """
        self.message = message

    def get_message(self):
        """ get the message
        Returns:
            string -- your message
        """
        return self.message

if __name__ == "__main__":
    # typical ussage
    PARSER = argparse.ArgumentParser(
        description="Python test script. Save a message"
    )
    PARSER.add_argument('-m', help="Give me a test string")
    ARGS = PARSER.parse_args()
    ARGS.verbose = False
    LOGGER.info("Logger initialized")
    MSG = ARGS.m if ARGS.m else "this is a test"
    APP = App()
    LOGGER.info("Setting message %s", MSG)
    APP.set_message(MSG)
    RET = APP.get_message()
    LOGGER.info("Received message %s", MSG)
    print(RET)

