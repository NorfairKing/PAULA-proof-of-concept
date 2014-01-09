#!/usr/bin/env python
##
#      ____   _   _   _ _        _    
#     |  _ \ / \ | | | | |      / \   
#     | |_) / _ \| | | | |     / _ \  
#     |  __/ ___ \ |_| | |___ / ___ \ 
#     |_| /_/   \_\___/|_____/_/   \_\
#
#
# Personal
# Artificial
# Unintelligent
# Life
# Assistant
#
##

class PAULA_Exception(Exception):
    def __init__(self, message=""):
        Exception.__init__(self, message)


class PAULAInputException(PAULA_Exception):
    pass


class PAULAOutputException(PAULA_Exception):
    pass


class PAULABrokenContractException(PAULA_Exception):
    pass


class PAULAUnimplementedFeatureException(PAULA_Exception):
    pass


class PAULAImportException(PAULA_Exception):
    pass


class PAULAMissingScriptException(PAULAImportException):
    pass


class PAULAParseException(PAULA_Exception):
    pass


class PAULANotAnIntegerException(PAULAParseException):
    pass


class PAULAUnknownQuantifierException(PAULAParseException):
    pass


class PAULAConfigurationException(PAULA_Exception):
    pass


class PAULAMissingConfigException(PAULAConfigurationException):
    pass

class PAULAMissingConfigFileException(PAULAConfigurationException):
    pass


class PAULAUnknownConfigException(PAULAConfigurationException):
    pass