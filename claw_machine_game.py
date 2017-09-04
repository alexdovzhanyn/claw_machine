import pygame
import claw
import pygame_text

class ClawMachineGame:
  # Define colours for pygame
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  running = True

  def __init__(self):
    pygame.init()
    size = [1280, 720]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Claw Machine Debugger Module")
    clock = pygame.time.Clock()
    pygame.joystick.init()
    pygameText = PygameText()
    claw = Claw(23, 24, 1)

  def start():
    while running:
      claw.updatePosition()

      # Process potential events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
            
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
          print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
          print("Joystick button released.")
        if event.type == pygame.JOYAXISMOTION and event.dict['axis'] == 1:
          if round(event.dict['value']) == -1:
            claw.toggleMoveLeft()
          elif round(event.dict['value']) == 1:
            claw.toggleMoveRight()
          elif round(event.dict['value']) == 0:
            claw.disableAxis('x')
     
      # DRAWING STEP
      # First, clear the screen to white. Don't put other drawing commands
      # above this, or they will be erased with this command.
      screen.fill(WHITE)
      pygameText.reset()

      # Get count of joysticks
      joystick_count = pygame.joystick.get_count()

      pygameText.output(screen, "Number of joysticks: {}".format(joystick_count) )
      pygameText.indent()
        
      # For each joystick:
      for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        
        pygameText.output(screen, "Joystick {}".format(i) )
        pygameText.indent()
        
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        pygameText.output(screen, "Joystick name: {}".format(name) )
            
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        pygameText.output(screen, "Number of axes: {}".format(axes) )
        pygameText.indent()
            
        for i in range( axes ):
          axis = joystick.get_axis( i )
          pygameText.output(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        pygameText.unindent()
                
        buttons = joystick.get_numbuttons()
        pygameText.output(screen, "Number of buttons: {}".format(buttons) )
        pygameText.indent()

        for i in range( buttons ):
          button = joystick.get_button( i )
          pygameText.output(screen, "Button {:>2} value: {}".format(i,button) )
          pygameText.unindent()
                
          # Hat switch. All or nothing for direction, not like joysticks.
          # Value comes back in an array.
          hats = joystick.get_numhats()
          pygameText.output(screen, "Number of hats: {}".format(hats) )
        pygameText.indent()

        for i in range( hats ):
          hat = joystick.get_hat( i )
          pygameText.output(screen, "Hat {} value: {}".format(i, str(hat)) )
        pygameText.unindent()
            
        pygameText.unindent()

        
      # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
      # Go ahead and update the screen with what we've drawn.
      pygame.display.flip()

      # Limit to 60 frames per second
      clock.tick(60)

    pygame.quit ()
