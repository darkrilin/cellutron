# Test file for cellular.py

import cellular

cellular.init()
cellular.display.create(640,480)

i = 0
while i < 100:
    cellular.display.draw()
    i += 1
    print(i)