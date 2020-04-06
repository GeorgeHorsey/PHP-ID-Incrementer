#!/usr/bin/env python

#Title: PHP ID incrementer
#Description: Auto magically increments the id in url

#DEPENDENCIES
import webbrowser

#VARIABLES
php_id = 0

#on the line below enter the range of integers you want to loop through.
#as an example I have it starting at 1 and going till 200.
for php_id in range(1, 200):
    #example url in line below. The main thing needed is the str insert...
    #"+str(php_id)+"
    webbrowser.open ("http://example.website.com.php?id="+str(php_id)+"&folder=1")
