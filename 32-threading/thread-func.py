#!/usr/bin/env python

import threading, time

def clock(interval,times):
    for i in xrange(times):
        print "The time is %s" % time.ctime()
        time.sleep(interval)
    print "Thread is about to terminate: the time is %s" % time.ctime()

t = threading.Thread(target = clock, args = (5,4))
t.daemon = True
t.start()
t.join()
print "Joined thread: the time is %s" % time.ctime()

