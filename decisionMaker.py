import random
import time
import keyboard

def on_space_pressed():
    print("Spacebar pressed. Tossing the coin...")
    time.sleep(1)
    random_bool = random.choice([True, False])
    if random_bool:
        print("Head")
    else:
        print("Tail")

if __name__ == "__main__":
    keyboard.add_hotkey('space', on_space_pressed)
    print("Press spacebar to toss the coin. Press 'q' to quit.")
    keyboard.wait('q')