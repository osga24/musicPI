import pygame
import os

def play_music():
    pygame.init()
    pygame.mixer.init()
    music_file = "music.wav"  # 音樂文件與執行檔案位於相同目錄
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(0.5)  # 預設音量設置為 0.5（範圍在 0.0 到 1.0 之間）
    pygame.mixer.music.play()

def main():
    play_music()
    music_paused = False

    while True:
        command = input("輸入命令 (pause / play / volume / exit): ")
        if command == "pause" and not music_paused:
            pygame.mixer.music.pause()
            music_paused = True
        elif command == "play" and music_paused:
            pygame.mixer.music.unpause()
            music_paused = False
        elif command == "volume":
            volume_percent = int(input("請輸入音量大小 (0 到 100): "))
            volume_percent = max(0, min(100, volume_percent))  # 確保音量在有效範圍內
            volume = volume_percent / 100.0  # 將百分比轉換為 0.0 到 1.0 的範圍
            pygame.mixer.music.set_volume(volume)
        elif command == "exit":
            break

    pygame.mixer.quit()

if __name__ == "__main__":
    main()
