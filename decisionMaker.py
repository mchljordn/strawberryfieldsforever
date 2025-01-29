import random
import time
import colorama
import keyboard

colorama.init(autoreset=True)

def on_space_pressed():
    time.sleep(0.2)
    print(colorama.Fore.YELLOW + "Spacebar pressed.", end='')
    time.sleep(0.3)
    print(colorama.Fore.GREEN + " Tossing the coin", end="")
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print()
    time.sleep(0.45)
    random_bool = random.choice([True, False])
    if random_bool:
        print(colorama.Fore.RED + "Head")
    else:
        print(colorama.Fore.BLUE + "Tail")

if __name__ == "__main__":
    keyboard.add_hotkey('space', on_space_pressed)
    print("Press spacebar to toss the coin. Press 'q' or 'ctrl + c' to quit.")
    try:
        keyboard.wait('q')
        print("Quitting", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()
    except KeyboardInterrupt as e:
        print("Quitting", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()