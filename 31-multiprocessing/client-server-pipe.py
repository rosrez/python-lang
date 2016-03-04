#!/usr/bin/env python

import multiprocessing

# A server process
def adder(pipe):
    server_p, client_p = pipe   # Get both ends of pipe
    client_p.close()            # We don't need the client end
    while True:
        try:
            x,y = server_p.recv()
        except EOFError:
            break

        result = x + y
        server_p.send(result)

    # Shutdown
    print "Server done"

if __name__ == "__main__":
    (server_p, client_p) = multiprocessing.Pipe()

    # Launch the server process
    adder_p = multiprocessing.Process(target=adder,args=((server_p, client_p),))
    adder_p.start()

    # Close the server pipe in the client
    server_p.close()

    # Make some requests on the server
    client_p.send((3,4))
    print client_p.recv()

    client_p.send(('Hello','World'))
    print client_p.recv()

    # Done. Close the pipe
    client_p.close()

    # Wait for the server process to shutdown
    adder_p.join()
