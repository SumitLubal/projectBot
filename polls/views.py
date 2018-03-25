# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
import zmq
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
        servo_num = request.GET['servo_num']
        pid_percentage = request.GET['value']
        send_message(servo_num, pid_percentage)
        return HttpResponse("Done!")

def send_message(servo_num, pid_percentage):
    print("servo num:"+servo_num+" value:"+pid_percentage)
    servo_num = servo_num.encode('ascii')
    pid_percentage = pid_percentage.encode('ascii')
    print(type(servo_num))
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://127.0.0.1:5555')
    socket.send(servo_num)
    msg = socket.recv()
    socket.send(pid_percentage)
    socket.close()
    
