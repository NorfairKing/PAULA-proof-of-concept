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

def search(arg_string):
    url = "https://gdata.youtube.com/feeds/api/videos?q="
        for a in arg_string.split():
            url += (str(a) + "+")
        url = url[0:-1]
        response = str(urllib.request.urlopen(url).read())
        vidid = response[response.find("<entry><id>http://gdata.youtube.com/feeds/api/videos/") + len("<entry><id>http://gdata.youtube.com/feeds/api/videos/"): response.find("</id><published>")]