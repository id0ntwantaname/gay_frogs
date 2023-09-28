import time , sys
import bext
import os

print("𝙂𝙖𝙮 𝙛𝙧𝙤𝙜𝙨")
print("Press Ctrl + C to stop")

time.sleep(2)

indent = 0
indentIncreasing = True

while True:
    print(" " * indent, end="")

    bext.fg("red")
    print("𓆏", end="")
    bext.fg("yellow")
    print("𓆏", end="")
    bext.fg("green")
    print("𓆏", end="")
    bext.fg("blue")
    print("𓆏", end="")
    bext.fg("cyan")
    print("𓆏", end="")
    bext.fg("purple")
    print("𓆏")

    if indentIncreasing:
        indent += 1
    else:
        indent -= 1
    if indent == os.get_terminal_size()[0]-12:
        indentIncreasing = False
    if indent == 0:
        indentIncreasing = True
    time.sleep(0.0)
