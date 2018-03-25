import argparse
import zmq

parser = argparse.ArgumentParser(description='zeromq server/client')
parser.add_argument('--bar')
args = parser.parse_args()

if args.bar:
    # client
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://127.0.0.1:5555')
    socket.send(args.bar)
    while true:
        msg = socket.recv()
        print msg

else:
    # server
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://127.0.0.1:5555')
    while True:
        msg1 = socket.recv()
        #time.sleep (1)
        socket.send('ok')
        msg2 = socket.recv()
        socket.send('alright')
        msg = [msg1,msg2]
        print("Servo num :"+msg1+" value:"+msg2)
        
