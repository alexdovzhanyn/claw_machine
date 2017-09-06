from time import sleep
import RPi.GPIO as GPIO

class Claw:
  def __init__(self, pin_map):
    self.x_direction_pin = pin_map['x_direction_pin']
    self.x_step_pin = pin_map['x_step_pin']
    self.y_direction_pin = pin_map['y_direction_pin']
    self.y_step_pin = pin_map['y_step_pin']
    self.z_direction_pin = pin_map['z_direction_pin']
    self.z_step_pin = pin_map['z_step_pin']
    self.xAxisMoving = False
    self.zAxisMoving = False
    self.delay = 0.001 # How long we wait between GPIO outputs

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.x_direction_pin, GPIO.OUT)
    GPIO.setup(self.x_step_pin, GPIO.OUT)
    GPIO.output(self.x_direction_pin, 1) # 1 IS CLOCKWISE, 0 IS COUNTERCLOCKWISE
    GPIO.setup(self.y_direction_pin, GPIO.OUT)
    GPIO.setup(self.y_step_pin, GPIO.OUT)
    GPIO.output(self.y_direction_pin, 1)
    GPIO.setup(self.z_direction_pin, GPIO.OUT)
    GPIO.setup(self.z_step_pin, GPIO.OUT)
    GPIO.output(self.z_direction_pin, 1)
    
  def toggleMoveLeft(self):
    GPIO.output(self.x_direction_pin, 0)
    self.xAxisMoving = True

  def toggleMoveRight(self):
    GPIO.output(self.x_direction_pin, 1)
    self.xAxisMoving = True

  def toggleMoveUp(self):
    GPIO.output(self.y_direction_pin, 0)
    self.yAxisMoving = True

  def toggleMoveDown(self):
    GPIO.output(self.y_direction_pin, 1)
    self.yAxisMoving = True
    
  def toggleMoveBack(self):
    GPIO.output(self.z_direction_pin, 0)
    self.zAxisMoving = True

  def toggleMoveForward(self):
    GPIO.output(self.z_direction_pin, 1)
    self.zAxisMoving = True

  def stopMovementOnAxis(self, axis):
    if axis == 'x':
      self.xAxisMoving = False
    elif axis == 'y':
      self.yAxisMoving = False
    elif axis == 'z':
      self.zAxisMoving = False

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
    if self.zAxisMoving:
      GPIO.output(self.z_step_pin, GPIO.HIGH)
      sleep(self.delay)
      GPIO.output(self.z_step_pin, GPIO.LOW)
      sleep(self.delay)
