import pygame
from claw import Claw

class ClawMachineGame:
  def __init__(self):
    pygame.init()
    self.joystick = pygame.joystick.Joystick(0)
    self.joystick.init()
    self.claw = Claw({
  		'x_direction_pin': 23,
  		'x_step_pin': 24,
  		'y_direction_pin': 19,
  		'y_step_pin': 26,
  		'z_direction_pin': 20,
  		'z_step_pin': 21
  	})

    print 'Initialized Joystick : %s' % self.joystick.get_name()
    print 'Axes Detected: %s' % self.joystick.get_numaxes()
    print 'Buttons Detected: %s' % self.joystick.get_numbuttons()
    
  def start(self):
    while True:
      self.claw.updatePosition()    
      values = self.getJoyStickValues()
      print values
        
      # X AXIS
      if values[1] < 0:
        self.claw.toggleMoveLeft()
      elif values[1] > 0:
        self.claw.toggleMoveRight()
      elif values[1] == 0:
        self.claw.stopMovementOnAxis('x')

      # Y AXIS
      # This axis is a bit different from X and Z because its controlled by 2 seperate buttons rather than the joystick itself
      if values[5] > 0:
      	self.claw.toggleMoveUp()
      elif values[6] > 0:
      	self.claw.toggleMoveDown()
      elif values[5] == 0 and values[6] == 0:
      	self.claw.stopMovementOnAxis('y')
            
      # Z AXIS
      if values[0] < 0:
        print 'back'
        self.claw.toggleMoveBack()
      elif values[0] > 0:
        print 'forwad'
        self.claw.toggleMoveForward()
      elif values[0] == 0:
        self.claw.stopMovementOnAxis('z')
                
  def getJoyStickValues(self):
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    it = 0 #iterator
    pygame.event.pump()
    
    #Read input from the two joysticks       
    for i in range(0, self.joystick.get_numaxes()):
      out[it] = self.joystick.get_axis(i)
      it+=1
    #Read input from buttons
    for i in range(0, self.joystick.get_numbuttons()):
      out[it] = self.joystick.get_button(i)
      it+=1
    return out
    
