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

import os
import random
from . import motivation_conf as conf

class Quote:
    def __init__(self, text, author="Unknown"):
        self.text = text
        self.author = author

    @classmethod
    def from_string(cls, line):
        split = line.split(" - ")
        text_w_quotes = split[0]
        text = text_w_quotes[1:-1]
        auth_w_endline = split[1]
        auth = auth_w_endline[:-1]
        return cls(text,author=auth)

    def __str__(self):
        return "\"" + self.text + "\"" + " - " + self.author 


def get_random():
    filename = random.choice(os.listdir(conf.QUOTE_DIR))
    random_file = os.path.join(conf.QUOTE_DIR, filename)    
    r_file = open(random_file)
    
    def random_line(random_file):
        line = next(random_file)
        for num, aline in enumerate(random_file):
            if random.randrange(num + 2): 
                continue
            line = aline
        return line
    
    return Quote.from_string(random_line(r_file))
    

