from os import system  
from time import sleep
ip = "192.168.0.87:6611" 
url ='curl -s -o /dev/null "http://admin:admin@' + ip + '/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act=' 
def ptz_right():
 system( url + 'right"')
 sleep(.00001)
 system( url + 'stop"')

def ptz_left():
 system( url + 'left"')
 sleep(.00001)
 system( url + 'stop"')

def ptz_up():
 system( url + 'up"')
 sleep(.00001)
 system( url + 'stop"')

def ptz_down():
 system( url + 'down"')
 sleep(.00001)
 system( url + 'stop"')


if __name__ == '__main__':
 ptz_right()
 ptz_left()
 ptz_up()
 ptz_down()
