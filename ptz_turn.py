from ptz_ctrl import *

def get_photo():
 system("sudo rm -r auto.jpg")
 system("wget -q  http://admin:admin@" + ip + "/tmpfs/auto.jpg")

def check_x(x_diff):
 if x_diff >= 7:
  x_count = x_diff / 13
  if x_diff % 13 >= 7:
   x_count+=1
  for count in range(0,x_count,1):
   ptz_right()

 elif x_diff <= -7 :
  x_count = abs(x_diff) / 13
  if abs(x_diff) % 13 >= 7:
   x_count+=1
  for count in range(0,x_count,1):
   ptz_left()

def check_y(y_diff):
 if y_diff >= 8:
  y_count = y_diff / 15
  if y_diff % 15 >= 8:
   y_count+=1
  for count in range(0,y_count,1):
   ptz_down()

 elif y_diff <= -8:
  y_count = abs(y_diff) / 15
  if abs(y_diff) % 15 >= 8:
   y_count+=1
  for count in range(0,y_count,1):
   ptz_up()
