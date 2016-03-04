#!/usr/bin/env python

import multiprocessing, os

def consumer(input_q):
    pid = os.getpid()
    print "Consumer: PID = %d" % pid
    while True:
        item = input_q.get()
        # Process item
        print "Consumer (%d): %s" % (pid, item)      # Replace with useful work
        # Signal task completion
        input_q.task_done()

def producer(sequence, output_q):
    for item in sequence:
        # Put the item on the queue
        output_q.put(item)

# Set up
if __name__ == '__main__':
    print "Main process: PID = %d" % os.getpid()
    # number of consumer processes
    num_consumers = 2
    # number of items in the sequence
    num_items = 50

    q = multiprocessing.JoinableQueue()
    # Launch consumer process(es)
    # There can be multiple producers/consumers that get items
    # from the same queue
    for i in range(num_consumers):
        cons_p = multiprocessing.Process(target=consumer, args=(q,))
        cons_p.daemon = True            # daemonic process will terminate when main program finishes
        cons_p.start()

    # Produce items. sequence represents a sequence of items to
    # be sent to the consumer. In practice, this could be the
    # output of a generator or produced in some other manner.
    sequence = (i+1 for i in xrange(num_items))
    producer(sequence, q)

    # wait for all items to be processed
    q.join()
