https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import re
import sys
for line in sys.stdin:
    if re.match('^((a|b)+(b|c)+)+d$', line):
        print('yes')
    else:
        print('no')
