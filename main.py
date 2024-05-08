import pygame
import os

def play_music():
    pygame.init()
    pygame.mixer.init()
    music_file = "music.wav" 
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

def main():
    play_music()
    music_paused = False

    while True:
        command = input("輸入命令 (pause / play / exit): ")
        if command == "pause" and not music_paused:
            pygame.mixer.music.pause()
            music_paused = True
        elif command == "play" and music_paused:
            pygame.mixer.music.unpause()
            music_paused = False
        elif command == "exit":
            break

    pygame.mixer.quit()

if __name__ == "__main__":
    main()
