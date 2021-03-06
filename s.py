from djitellopy import Tello
from time import sleep
import cv2
import pygame
import random
import requests
import numpy as np
import math

#start up
tello = Tello()
tello.connect()
print(tello.get_battery())
sleep(.5)
tello.takeoff()
tello.streamon()

#Camera
while True:
  img = tello.get_frame_read().frame
  img = cv2.resize(img,(360, 240))
  cv2.imshow("image", img)
  cv2.waitkey(1)

#variables
a = 0
b = 0

#move to location
#1
tello.move_up(61)
sleep(.1)
tello.move_forwards(183)
sleep(.1)
tello.rotate_counter_clockwise(90)
sleep(.1)

#2
tello.move_up(166)
sleep(.1)

#3
tello.rotate_clockwise(180)
sleep(.1)
tello.move_forward(113)
sleep(.1)
tello.move_up()
sleep(.1)

#4
tello.move_forward(91)
sleep(.1)
tello.move_down(183)
sleep(.1)

#5
tello.move_forward(61)
sleep(.1)
tello.rotate_clockwise(90)
sleep(.1)
tello.move_up(91)
sleep(.1)
tello.move_forward(105)
sleep(.1)

#dance moves or 6
while b < 7:
  a = random.range(1, 40)
  print(a)
  if a == 1:
      tello.move_left(30)
      sleep(.1)
      tello.move.back(30)
      sleep(.1)
      tello.flip_right()
  if a == 2:
      tello.move_right(30)
      sleep(.1)
      tello.move_left(30)
      sleep(.1)
      tello.flipback()
  if a == 3:
      tello.move_right(30)
      sleep(.1)
      tello.move_up(30)
      sleep(.1)
      tello.move_back(30)
  if a == 4:
      tello.move_left(30)
      sleep(.1)
      tello.move_forwards(30)
      sleep(.1)
      tello.flip_left()
  if a == 5:
      tello.move_up(30)
      sleep(.1)
      tello.move_forward(30)
      sleep(.1)
      tello.move_back(30)
  if a == 6:
      tello.move_right(30)
      sleep(.1)
      tello.move_down(30)
      sleep(.1)
      tello.move_back(30)
  if a == 7:
      tello.move_left(30)
      sleep(.1)
      tello.move_up(30)
      sleep(.1)
      tello.move_back(30)
  if a == 8:
      tello.move_left(30)
      sleep(.1)
      tello.move_down(30)
      sleep(.1)
      tello.flip_back()
  if a == 9:
      tello.move_down(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_forward()
  if a == 10:
      tello.move_right(30)
      sleep(.1)
      tello.move_down(30)
      sleep(.1)
      tello.flip_back()
  if a == 11:
      tello.move_right(30)
      sleep(.1)
      tello.move_down(30)
      sleep(.1)
      tello.flip_right()
  if a == 12:
      tello.move_up(30)
      sleep(.1)
      tello.move_down(30)
      sleep(.1)
      tello.flip_left()
  if a == 13:
      tello.move_right(30)
      sleep(.1)
      tello.move_left(30)
      sleep(.1)
      tello.move_up(30)
  if a == 14:
      tello.move_left(30)
      sleep(.1)
      tello.move_front(30)
      sleep(.1)
      tello.flip_forward()
  if a == 15:
      tello.move_down(30)
      sleep(.1)
      tello.move_forward(30)
      sleep(.1)
      tello.flip_forward()
  if a == 16:
      tello.move_up(30)
      sleep(.1)
      tello.move_down(30)
      sleep(.1)
      tello.move_forward(30)
  if a == 17:
      tello.move_up(30)
      sleep(.1)
      tello.move_down(30)
      sleep(.1)
      tello.move_forward(30)
  if a == 18:
      tello.move_up(30)
      sleep(.1)
      tello.move_forward(30)
      sleep(.1)
      tello.flip_forward()
  if a == 19:
      tello.move_left(30)
      sleep(.1)
      tello.move_down(30)
      sleep(.1)
      tello.move_forward(30)
  if a == 20:
      tello.move_up(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_forward()
  if a == 21:
      tello.move_up(30)
      sleep(.1)
      tello.move_forward(30)
      sleep(.1)
      tello.flip_right()
  if a == 22:
      tello.move_left(30)
      sleep(.1)
      tello.move_up(30)
      sleep(.1)
      tello.flip_forward()
  if a == 23:
      tello.move_forward(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_back()
  if a == 24:
      tello.move_right(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_right()
  if a == 25:
      tello.move_left(30)
      sleep(.1)
      tello.move_up(30)
      sleep(.1)
      tello.flip_back()
  if a == 26:
      tello.move_down(30)
      sleep(.1)
      tello.move_forward(30)
      sleep(.1)
      tello.flip_back()
  if a == 27:
      tello.move_right(30)
      sleep(.1)
      tello.move_down(30)
      sleep(.1)
      tello.flip_forward()
  if a == 28:
      tello.move_right(30)
      sleep(.1)
      tello.move_forward(30)
      sleep(.1)
      tello.flip_left()
  if a == 29:
      tello.move_left(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_back()
  if a == 30:
      tello.move_down(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_right()
  if a == 31:
      tello.move_right(30)
      sleep(.1)
      tello.move_up(30)
      sleep(.1)
      tello.flip_back()
  if a == 32:
      tello.move_up(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_forward()
  if a == 33:
      tello.move_right(30)
      sleep(.1)
      tello.move_left(30)
      sleep(.1)
      tello.flip_back()
  if a == 34:
      tello.move_forward(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_left()
  if a == 35:
      tello.move_forward(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_right()
  if a == 36:
      tello.move_left(30)
      sleep(.1)
      tello.move_back(30)
      sleep(.1)
      tello.flip_left(30)
  if a == 37:
      tello.move_left(30)
      sleep(.1)
      tello.move_up(30)
      sleep(.1)
      tello.flip_forward()
  if a == 38:
      tello.move_right(30)
      sleep(.1)
      tello.move_forward(30)
      sleep(.1)
      tello.flip_left()
  if a == 39:
      tello.move_up(30)
      sleep(.1)
      tello.move_forward(30)
      sleep(.1)
      tello.flip_left()
  if a == 40:
      tello.move_right(30)
      sleep(.1)
      tello.move_forward(30)
      sleep(.1)
      tello.flip_right()
  a = 0
  b = (b+1)
  sleep(1)
#land
tello.move_down(122)
sleep(.1)
tello.land()
print("the show is over")
