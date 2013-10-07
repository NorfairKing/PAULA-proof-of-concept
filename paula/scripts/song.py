import pygame

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/syd/Music/music/avicii-wake_me_up.mp3")
    pygame.mixer.music.play()

    # Wait untill done
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

