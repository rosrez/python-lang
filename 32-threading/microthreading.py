#!/usr/bin/env python

def foo():
    for n in xrange(5):
        print "I'm foo %d" % n
        yield

def bar():
    for n in xrange(10):
        print "I'm bar %d" % n
        yield

def spam():
    for n in xrange(7):
        print "I'm spam %d" % n
        yield

# Create and populate a task queue

from collections import deque
taskqueue = deque()
taskqueue.append(foo())        # Add some tasks (generators)
taskqueue.append(bar())
taskqueue.append(spam())

# Run all of the tasks
while taskqueue:
    # Get the next task
    task = taskqueue.pop()
    try:
        # Run it to the next yield and enqueue
        next(task)
        taskqueue.appendleft(task)
    except StopIteration:
        # Task is done
        pass
