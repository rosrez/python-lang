#!/usr/bin/env python

import multiprocessing, os

# Consume item on a pipe
def consumer(pipe):
    pid = os.getpid()
    output_p, input_p = pipe
    input_p.close()         # Close the input end of the pipe
    while True:
        try:
            item = output_p.recv()
        except EOFError:
            break
        
        # Process item
        print "Consumer (%d): %d" % (pid, item)    # Replace with useful work
    
    # Shutdown
    print "Consumer (%d) done" % pid

# Produce items and put on a queue. sequence is an
# iterable representing items to be processed.
def producer(sequence, input_p):
    for item in sequence:
        # Put the item on the queue
        input_p.send(item)

if __name__ == '__main__':
    # number of items in the sequence
    num_items = 50

    # Create pipe (returns two ends of the pipe)
    (output_p, input_p) = multiprocessing.Pipe()

    # Launch the consumer process
    cons_p = multiprocessing.Process(target=consumer, args=((output_p, input_p),))
    cons_p.start()

    # Close the output pipe in the producer
    output_p.close()
    
    # Produce items
    sequence = (i+1 for i in xrange(num_items))
    producer(sequence, input_p)

    # Signal completion by closing the input pipe
    input_p.close()

    # Wait for consumer process to shutdown
    cons_p.join()

