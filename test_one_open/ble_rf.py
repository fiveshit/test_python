import serial
import sys  
def rfcomm0_d(data):
    port0 = '/dev/rfcomm1'
    ser = serial.Serial(port0,115200,timeout=3)
##    chr_open = 98
##    cmd_open = (chr(chr_open).encode('utf-8'))
##    ser.write(cmd_open)
    en_data = [48]
    for a in range(len(data)):
        cmd = (chr(data[a]+en_data[0]).encode('utf-8'))
        ser.write(cmd)
    chr_run = 98
    cmd_open = (chr(chr_run).encode('utf-8'))
    ser.write(cmd_open)
    ser.flushInput()
    #ser.close()
def rfcomm1_d(data):
    port1 = '/dev/rfcomm2'
    ser = serial.Serial(port1,115200,timeout=1)
    for a in range(18):
        cmd = (chr(data[a]).encode('utf-8'))
        ser.write(cmd)
    ser.flushInput()
    #ser.close()
def rfcomm2_d(data):
    global lock,voice_data_3
##    lock.acquire()
    port2 = '/dev/rfcomm3'
    ser = serial.Serial(port2,115200,timeout=1)
    for a in range(18):
        cmd = (chr(data[a]).encode('utf-8'))
        ser.write(cmd)
    ser.flushInput()
    #ser.close()
def rfcomm3_d(data):
    port3 = '/dev/rfcomm4'
    ser = serial.Serial(port3,115200,timeout=1)
    for a in range(18):
        cmd = (chr(data[a]).encode('utf-8'))
        ser.write(cmd)
    ser.flushInput()
    #ser.close()
def rfcomm4_d(data):
    port4 = '/dev/rfcomm5'
    ser = serial.Serial(port4,115200,timeout=1)
    for a in range(18):
        cmd = (chr(data[a]).encode('utf-8'))
        ser.write(cmd)
    ser.flushInput()
    #ser.close()
def rfcomm5_d(data):
    port5 = '/dev/rfcomm6'
    ser = serial.Serial(port5,115200,timeout=1)
    for a in range(18):
        cmd = (chr(data[a]).encode('utf-8'))
        ser.write(cmd)
    ser.flushInput()
    #ser.close()

    

    
