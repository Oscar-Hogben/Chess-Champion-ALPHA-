import os

green = "\033[1;32;12m"
red = "\033[0;31;12m"
orange = "\033[0;33;12m"
white = "\033[0;37;12m"
blank = "\033[0;37;12m"


def clear():
  os.system('clear')

  print(f"{blank}Chess Champion {orange}[ALPHA]{blank}")
  print()
  print()


hello = "There"
