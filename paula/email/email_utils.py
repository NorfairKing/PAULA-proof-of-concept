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

"""
Any utilities the email package might need.
"""

import re

from . import email_config as conf

def verify(adress):
    with open(conf.EMAIL_REGEX_FILE, 'r') as f:
        regex_str = f.readline()

    email_regex = re.compile(regex_str)
    return email_regex.match(adress)