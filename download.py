# Imports
import pygame, sys, threading

pygame.init()

# Screen and font
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Upload")

FONT = pygame.font.SysFont("Roboto", 100)

# Clock
CLOCK = pygame.time.Clock()

# Work
WORK = 100000000

# Loading BG
LOADING_BG = pygame.image.load('Loading Bar Background.png')
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))

# Loading Bar and Variables
LOADING_BAR = pygame.image.load('Loading Bar.png')
loading_bar_rect = LOADING_BAR.get_rect(midleft=(280, 360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
    # do some math WORK amount of times
    global loading_finished, loading_progress

    for i in range(WORK):
        math_equation = 523687 / 23458 * 892345
        loading_progress = i

    loading_finished = True

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
    screen.fill("#0d0e2e")

    if not loading_finished:
        loading_bar_width = loading_progress / WORK * 720
        
        loading_bar = pygame.transform.scale(LOADING_BAR, (int(loading_bar_width), 150))
        loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))

        screen.blit(LOADING_BG, LOADING_BG_RECT)
        screen.blit(downloadText, downloadText_rect)
        screen.blit(loading_bar, loading_bar_rect)
    else:
        screen.blit(finished, finished_rect)

    
    pygame.display.update()
    CLOCK.tick(60)
