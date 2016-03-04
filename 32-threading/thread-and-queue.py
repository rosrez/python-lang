#!/usr/bin/env python

import threading
from Queue import Queue # Use 'from queue' in Python 3

class WorkerThread(threading.Thread):
    def __init__(self,*args,**kwargs):
        threading.Thread.__init__(self,*args,**kwargs)
        self.input_queue = Queue()

    def send(self, item):
        self.input_queue.put(item)

    def close(self):
        self.input_queue.put(None)
        self.input_queue.join()

    def run(self):
        while True:
            item = self.input_queue.get()
            if item is None:
                break

            # Process the item: replace with useful work
            print item
            self.input_queue.task_done()

        # Done. Indicate that sentinel was received and return
        self.input_queue.task_done()
        return

# Example use
w = WorkerThread()
w.start()
w.send("Hello")     # Send items to the worker (via queue)
w.send("World")
w.close()
