#!/bin/python3

fh = open("/etc/passwd", "r")

title = ["USERNAME", "PASSWORD", "USER ID", "GROUP ID", "NONE", "HOME DIRECTORY", "SHELL"]

n = 1
for line in fh.readlines():
    user = line.strip().split(':')
    for i in range(1,len(user)):
        print("%04d: %s = [%s]" % (n, title[i], user[i]))
    n = n + 1

fh.close()
