import pygame, os

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick( 0 )
joystick.init()

done=False

fps_cap = 20
clock = pygame.time.Clock()
nullzone = 10

def joystick_proc():

    output = [0]*4

    for axis in range( 4 ):
        if axis < 3:
            output[ axis ] = round(joystick.get_axis( axis ), 2)*100
        else:
            #invert throttle input
            output[ axis ] = round(((joystick.get_axis( axis ) * -1)+1)/2, 2)*100
    return output

while done==False:

    try:
        clock.tick( fps_cap )

        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                os.system('clear')
                # print( joystick.get_axis(0) )
                # print( joystick.get_axis(1) )
                # print( joystick.get_axis(2) )
                # print( joystick.get_axis(3) )
                print( joystick_proc() )
        pygame.event.clear()
    except KeyboardInterrupt:
        pygame.quit()
        exit()
