import winsound
import threading
import time
import cv2
import pyautogui
import winsound

# Path to the sound file
sound_file = "alarm.mp3"
pressed = None


def compare_images(original, duplicate):
    if original.shape == duplicate.shape:
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)

        return cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0
    else:
        return False

# Define a function to take a screenshot


def take_ss(name):
    im = pyautogui.screenshot(region=(661, 1032, 700, 47))
    im.save(name)

# Define a function to play the sound on loop


def play_sound():
    while True:
        winsound.Beep(440, 1000)


def play_sounds():
    global pressed

    # Start playing the sound on a separate thread
    sound_thread = threading.Thread(target=play_sound)
    sound_thread.start()
    sound_thread.join()
    # Wait for a key to be pressed
    print("Press any key to stop the sound...")
    pressed = input("Press any key to stop the sound...  ")


def main():
    im1 = take_ss("first.png")
    original = cv2.imread("first.png")
    while True:
        im2 = take_ss("second.png")
        duplicate = cv2.imread("second.png")
        if compare_images(original, duplicate):
            print("The images are the same.")
            time.sleep(1)
        else:
            break
        play_sound()


if __name__ == "__main__":
    main()
