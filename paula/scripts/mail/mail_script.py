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
The simple mail script
"""

from paula.scripts.script import Script
from paula.email.email import Email

class MailScript(Script):
    def execute(self, operand):
        """
        The operand should be something as follows.
        <content> to <email-adress>
        @param operand: The operand for this script.
        """
        content, recipient = self.parse_operand(operand)
        subject = 'A message from my master'
        e = Email(subject, content, recipient)
        e.send()
        self.debug('Mail sent to ' + recipient + ' with content: ' + content)

    def parse_operand(self,operand):
        """
        Parses the operand into the content and the recipient.
        @param operand: The given operand.
        @return: A tuple (content, recipient)
        """
        split = operand.split(' to ')
        return " to ".join(split[:-1]),split[-1] #TODO this is hardcoded.
