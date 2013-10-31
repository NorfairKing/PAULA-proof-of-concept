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

import unittest
import time

from . import volume

class volumeTests(unittest.TestCase):

    def test_get_volume(self):
        volume.get()

    def test_set_volume(self):
        for i in range(100):
            volume.set(i)
            current_vol = volume.get()
            self.failUnless(abs(current_vol - i) <= 2) 

    def test_mute(self):
        volume.mute()
        self.assertEqual(0, volume.get())

def main():
    unittest.main()

if __name__ == '__main__':
    main()
