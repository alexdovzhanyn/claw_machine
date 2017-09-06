from time import sleep
import RPi.GPIO as GPIO

class Claw:
  def __init__(self, x_direction_pin, x_step_pin, x_movement_direction, y_direction_pin, y_step_pin, y_movement_direction):
    self.x_direction_pin = x_direction_pin
    self.x_step_pin = x_step_pin
    self.y_direction_pin = y_direction_pin
    self.y_step_pin = y_step_pin
    self.xAxisMoving = False
    self.yAxisMoving = False
    self.delay = 0.001 # How long we wait between GPIO outputs

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(x_direction_pin, GPIO.OUT)
    GPIO.setup(x_step_pin, GPIO.OUT)
    GPIO.output(x_direction_pin, x_movement_direction) # 1 IS CLOCKWISE, 0 IS COUNTERCLOCKWISE
    GPIO.setup(y_direction_pin, GPIO.OUT)
    GPIO.setup(y_step_pin, GPIO.OUT)
    GPIO.output(y_direction_pin, y_movement_direction)
    
  def toggleMoveLeft(self):
    GPIO.output(self.x_direction_pin, 0)
    self.xAxisMoving = True

  def toggleMoveRight(self):
    GPIO.output(self.x_direction_pin, 1)
    self.xAxisMoving = True
    
  def toggleMoveBack(self):
    GPIO.output(self.y_direction_pin, 0)
    self.yAxisMoving = True

  def toggleMoveForward(self):
    GPIO.output(self.y_direction_pin, 1)
    self.yAxisMoving = True

  def stopMovementOnAxis(self, axis):
    if axis == 'x':
      self.xAxisMoving = False
    elif axis == 'y':
      self.yAxisMoving = False

  def updatePosition(self):
    if self.xAxisMoving:
      GPIO.output(self.x_step_pin, GPIO.HIGH)
      sleep(self.delay)
      GPIO.output(self.x_step_pin, GPIO.LOW)
      sleep(self.delay)
    if self.yAxisMoving:
      GPIO.output(self.y_step_pin, GPIO.HIGH)
      sleep(self.delay)
      GPIO.output(self.y_step_pin, GPIO.LOW)
      sleep(self.delay)
