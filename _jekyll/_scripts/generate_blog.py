import re
import sys
import time
title = time.strftime("%B %d, %Y")
curr_time = time.strftime("%Y-%m-%d %H:%M:%S +0000", time.gmtime())
print '---'
print 'layout: post'
print 'title:  "%s" Results' % title
print 'date: %s' % curr_time
print 'categories: results'
print '---'
for line in sys.stdin:
    print re.sub("(http\S*)", "[\g<0>](\g<0>)", line.strip())



