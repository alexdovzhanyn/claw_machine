from time import sleep
import RPi.GPIO as GPIO

class Claw:
  def __init__(self, x_direction_pin, x_step_pin, x_movement_direction):
    self.x_direction_pin = x_direction_pin
    self.x_step_pin = x_step_pin
    self.xAxisMoving = False
    self.yAxisMoving = False
    self.delay = 0.01 # How long we wait between GPIO outputs

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(x_direction_pin, GPIO.OUT)
    GPIO.setup(x_step_pin, GPIO.OUT)
    GPIO.output(x_direction_pin, x_movement_direction) # 1 IS CLOCKWISE, 0 IS COUNTERCLOCKWISE

  def toggleMoveLeft():
    GPIO.output(self.x_direction_pin, 0)
    self.xAxisMoving = not self.xAxisMoving

  def toggleMoveRight():
    GPIO.output(self.x_direction_pin, 1)
    self.xAxisMoving = not self.xAxisMoving

  def disableAxis(axis):
    if axis == 'x':
      self.xAxisMoving = False
    elif axis == 'y':
      self.yAxisMoving = False

  def updatePosition():
    if xAxisMoving:
      GPIO.output(self.x_step_pin, GPIO.HIGH)
      sleep(self.delay)
      GPIO.output(self.x_step_pin, GPIO.LOW)
      sleep(self.delay)
    elif xAxisMoving:
      # TODO
      print "Not implemented"