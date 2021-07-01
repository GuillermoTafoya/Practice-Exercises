from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import fox_chicken_grain_ai as ai
#import pprint as p
import pathlib

src = str(pathlib.Path(__file__).parent.resolve()) + "\\robot assets\\"

def main():

    x_size = 100
    y_size = 100


    #robotSprite = pygame.image.load(src + 'robot.png')
    robotSprite = pygame.transform.scale(pygame.image.load(src + 'robot.png'), (x_size, y_size))
    foxSprite = pygame.transform.scale(pygame.image.load(src + 'fox.png'), (x_size, y_size))
    chickenSprite = pygame.transform.scale(pygame.image.load(src + 'chicken.png'), (x_size, y_size))
    grainSprite = pygame.transform.scale(pygame.image.load(src + 'grains.png'), (x_size, y_size))
    riverSprite = pygame.transform.scale(pygame.image.load(src + 'river.png'), (4*x_size, 600))

    resources = [robotSprite, foxSprite, chickenSprite, grainSprite]    
    
    ###
    """ The main function to obtain the solution """
    ###
    solution = ai.ai(maxPassengers=1,maxTrips=10)



    # How fast it shows the best state possible (wait time between each trip in miliseconds)
    speed = 700

    background_colour = (204, 255, 204)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Fox, Chicken, Grain')

    


    # Update the display using flip
    pygame.display.flip()

    # Variable to keep our game loop running
    #running = True

    left = 150
    right = 4*left
    
    height = 100

    #colors = ["black", "orange", "yellow", "purple"]

    step = 0
    length = len(solution)-1

    # game loop
    while step < length:
        # Fill the background colour to the screen
        screen.fill(background_colour)
        screen.blit(riverSprite, (400-x_size, 0),)
        #pygame.draw.rect(screen, "blue", pygame.Rect(400-x_size, 0, 2*x_size, 600))

        for i in range(4):
            if solution[step][i]:
                screen.blit(resources[i],(left, height+i*100))
                #pygame.draw.rect(screen, colors[i], pygame.Rect(left, heigth+i*100, x_size, y_size))
            elif not solution[step][i]:
                screen.blit(pygame.transform.flip(resources[i], True, False),(right, height+i*100))
                #pygame.draw.rect(screen, colors[i], pygame.Rect(right, heigth+i*100, x_size, y_size))
            
            

        """
        pygame.draw.rect(screen, "black", pygame.Rect(left, heigth+0, x_size, y_size))
        pygame.draw.rect(screen, "orange", pygame.Rect(left, heigth+100, x_size, y_size))
        pygame.draw.rect(screen, "yellow", pygame.Rect(left, heigth+200, x_size, y_size))
        pygame.draw.rect(screen, "purple", pygame.Rect(left, heigth+300, x_size, y_size))
        
        """
        
        pygame.display.flip()
        
        
    # for loop through the event queue  
        for event in pygame.event.get():
        
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.time.wait(speed)
        step += 1

if __name__ == '__main__':
    main()
