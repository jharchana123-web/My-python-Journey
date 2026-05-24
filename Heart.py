
import os
import time
import random
from pyfiglet import Figlet
from colorama import Fore, Style, init

init(autoreset=True)

# Different colors
colors = [
    Fore.RED,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.BLUE
]

# Clear screen function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# User input
name = input("Enter your girlfriend's name: ")

# Different font styles
fonts = ["slant", "big", "banner3-D", "doom", "standard", "block", "bubble"]

# Animation loop
for i in range(30):
    clear()

    color = random.choice(colors)
    font = random.choice(fonts)
    
    # Add pulsing effect by changing spacing
    padding = " " * (i % 5)

    f = Figlet(font=font)
    
    print(padding + color + f.renderText(name).replace("\n", "\n" + padding))

    print(Fore.WHITE + "✨✨✨✨✨✨✨✨✨")
    time.sleep(0.2)

print(Fore.RED + Style.BRIGHT + "\n❤️ Forever Special ❤️")