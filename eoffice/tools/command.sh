#!/bin/sh


##############################################################
echo "recursively removing .svn folders from"
pwd

find . -type d -name .svn


rm -rf `find . -type d -name .svn`
 
 
find . -iname ".svn" -print0 | xargs -0 rm -r
find . -name ".svn" -exec rm -rf {} \;
 