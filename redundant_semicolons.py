# Author: Slawomir Zurek
# The script is designed to improve the text file by eliminating redundant semicolons.

import os, time, sys

if sys.version_info < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')

def timer():
    time.sleep(3)

def nth_repl(line, sub, repl, nth):
    find = line.find(sub)
    i = find != -1
    while find != -1 and i != nth:
        find = line.find(sub, find + 1)
        i += 1
    if i == nth:
        y = line[ :find]+repl+line[find + len(sub):]
        file2.writelines(y)
    else:
        file2.writelines(line)
        
ti = time.gmtime()
sub = ';'
repl = '                         '
nth = 7

print('The correct file name to convert: file.txt \n\nStart ...')
timer()

file1 = open("file1.txt", "r")
file2 = open("tmp2.txt", "w+")

file1 = ''.join([i for i in file1]).replace ("ACTIVATED;", "ACTIVATED*")
file2.writelines(file1)
  
file1 = open("tmp2.txt", "r")
file2 = open("tmp3.txt", "w+")

for line in file1:
    x = line.count(';')
    if x >= 15:
        nth_repl(line, sub, repl, nth)
    else:
        x < 15
        file2.writelines(line)

file1 = open("tmp3.txt", "r")
file2 = open("tmp4.txt", "w+")       

for line in file1:
    z = line.count(';')
    if z >= 15:
        nth_repl(line, sub, repl, nth)
    else:
        z < 15
        file2.writelines(line)

file1 = open("tmp4.txt", "r")
file2 = open("result.txt", "w+")       

for line in file1:
    k = line.count(';')
    if k >= 15:
        nth_repl(line, sub, repl, nth)
    else:
        k < 15
        file2.writelines(line)
        
print('The file has been corrected.')
    
if os.path.exists("temp2.txt"):
    os.remove("temp2.txt")

if os.path.exists("temp3.txt"):
    os.remove("temp3.txt")

if os.path.exists("temp4.txt"):
    os.remove("temp4.txt")

