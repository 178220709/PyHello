#!/usr/bin/python
# Filename: using_file.py


poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''

f = open(r'D:\temp\1.txt', 'a') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file

f = open(r'D:\temp\1.txt')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0: # Zero length indicates EOF
        break
    print (line,)
    # Notice comma to avoid automatic newline added by Python
f.close() # close the file