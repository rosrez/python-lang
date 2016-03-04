#!/usr/bin/env python

import threading, time

class ClockThread(threading.Thread):
    def __init__(self,interval,times):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval
        self.times = times

    def run(self):
        for i in xrange(self.times):
            print "The time is %s" % time.ctime()
            time.sleep(self.interval)
        print "Thread is about to terminate: the time is %s" % time.ctime()

t = ClockThread(5, 3)   # Display the time at 5-sec intervals, 3 times
t.start()               # Start the thread
t.join()                # Join the thread
print "Thread terminated: the time is %s" % time.ctime()
