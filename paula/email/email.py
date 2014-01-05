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
The module for any email PAULA sends.
"""

import smtplib

from . import exceptions
from . import email_utils as util
from . import email_config as conf


class Email(object):
    def __init__(self, subject, content, recipient):
        self.subject = subject
        self.content = content
        if not util.verify(recipient):
            raise exceptions.PAULAInvalidEmailException
        self.to_addr_list = [recipient]
        self.cc_addr_list = []

    def add_recipient(self, res):
        if not util.verify(res):
            raise exceptions.PAULAInvalidEmailException
        self.to_addr_list.append(res)

    def add_cc(self, cc):
        if not util.verify(cc):
            raise exceptions.PAULAInvalidEmailException
        self.cc_addr_list.append(cc)

    def send(self):
        header = 'From: %s\n' % conf.FROM
        header += 'To: %s\n' % ','.join(self.to_addr_list)
        header += 'Cc: %s\n' % ','.join(self.cc_addr_list)
        header += 'Subject: %s\n\n' % self.subject
        message = header + self.content

        server = smtplib.SMTP(conf.SMTP_SERVER)
        server.starttls()
        server.login(conf.LOGIN, conf.PASSWORD)
        server.sendmail(conf.FROM, self.to_addr_list, message)
        server.quit()