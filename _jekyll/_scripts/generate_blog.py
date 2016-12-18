import re
import sys
import time
title = time.strftime("%B %d, %Y")
print '---'
print 'layout: post'
print 'title:  "%s" Results' % title
print 'categories: results'
print '---'
for line in sys.stdin:
    print re.sub("(http\S*)", "[\g<0>](\g<0>)", line.strip())



