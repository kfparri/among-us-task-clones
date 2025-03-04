# Imports
import pygame, sys, threading

# Work
WORK = 100000000

# Loading BG
LOADING_BG = pygame.image.load('Loading Bar Background.png')
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 500 # in milliseconds
FLASHDELAY = 200 # in milliseconds

#                R    G    B
WHITE        = (255, 255, 255)

# Loading Bar and Variables
LOADING_BAR = pygame.image.load('Loading Bar.png')
loading_bar_rect = LOADING_BAR.get_rect(midleft=(280, 360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def main():
    global BEEP1, BEEP2, BEEP3, BEEP4, FONT, CLOCK, DISPLAYSURF

    pygame.init()

    # Screen and font
    DISPLAYSURF = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    pygame.display.set_caption("Upload")

    FONT = pygame.font.SysFont("Roboto", 100)

    # Clock
    CLOCK = pygame.time.Clock()

    # load the sound files
    BEEP1 = pygame.mixer.Sound('beep1.ogg')
    BEEP2 = pygame.mixer.Sound('beep2.ogg')
    BEEP3 = pygame.mixer.Sound('beep3.ogg')
    BEEP4 = pygame.mixer.Sound('beep4.ogg')
    
    # Finished text
    finished = FONT.render("Task Complete!", True, "white")
    finished_rect = finished.get_rect(center=(640,360))

    # Download text
    downloadText = FONT.render("Downloading...", True, "white")
    downloadText_rect = downloadText.get_rect(center=(640, 230))

    # Thread
    threading.Thread(target=doWork).start()
    # Game Loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        DISPLAYSURF.fill("#0d0e2e")

        if not loading_finished:
            loading_bar_width = loading_progress / WORK * 720
            
            loading_bar = pygame.transform.scale(LOADING_BAR, (int(loading_bar_width), 150))
            loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))

            DISPLAYSURF.blit(LOADING_BG, LOADING_BG_RECT)
            DISPLAYSURF.blit(downloadText, downloadText_rect)
            DISPLAYSURF.blit(loading_bar, loading_bar_rect)
        else:
            taskCompleteAnimation()
            terminate()
            #DISPLAYSURF.blit(finished, finished_rect)

        
        pygame.display.update()
        CLOCK.tick(FPS)
        
# Flashes the screen and displays 'Task Complete!' on the screen
def taskCompleteAnimation(color=WHITE, animationSpeed=50):
    # play all beeps at once, then flash the background
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    BEEP1.play() # play all four beeps at the same time, roughly.
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()
    r, g, b = color
    for i in range(3): # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # The first iteration in this loop sets the following for loop
            # to go from 0 to 255, the second from 255 to 0.
            for alpha in range(start, end, animationSpeed * step): # animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf, (0, 0))
                DISPLAYSURF.blit(flashSurf, (0, 0))

                # Display the task complete message
                TASKCOMPLETEFONT = pygame.font.Font('freesansbold.ttf', 72)
                taskCompleteSurf = TASKCOMPLETEFONT.render('Task Complete!', 1, WHITE)
                taskCompleteRect = taskCompleteSurf.get_rect()
                taskCompleteRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)

                DISPLAYSURF.blit(taskCompleteSurf, taskCompleteRect)

                pygame.display.update()
                CLOCK.tick(FPS)

def doWork():
    # do some math WORK amount of times
    global loading_finished, loading_progress

    for i in range(WORK):
        math_equation = 523687 / 23458 * 892345
        loading_progress = i

    loading_finished = True

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()