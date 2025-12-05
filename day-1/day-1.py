import math

# read input
data = []
with open("in/input.txt", "r") as f:
    data = f.read().splitlines()

# variable inits
zh = 0
zp = 0
pos = 50

# loop through input
for d in data:
    # skip in case someone tries a zero rotation
    if int(d[1:]) == 0:
        continue
    # save old position to decide if we hit 0 on left turns
    pos_old = pos
    # turn right
    if d[0] == "R":
        pos += int(d[1:])
        # for right turns, just use integer division of the new position
        # this counts each circle, plus if we hit 0 as the end position
        zp += math.floor(pos/100)
    # turn left
    elif d[0] == "L":
        pos -= int(d[1:])
        if pos_old == 0:
            # if we started at zero just use integer division of abs negative
            zp += math.floor((-pos)/100)
        elif pos == 0:
            # if we stop at exactly 0, we hit it once
            zp += 1
        elif pos < 0:
            # if we started above 0 and come out less then 0 add one 
            # to the first case
            zp += math.floor((-pos)/100) + 1
    # input error
    else:
        print("Input Error")
        continue
    # calc mod bcs of circular dial
    pos = pos % 100
    # check for zero hit
    if pos == 0:
        zh += 1

# print result first half
print(f"First Half: The actual password to open the door is {zh}!")
# print result second half
print(f"Second Half: Using password method 0x434C49434B, the password to open the door is {zp}!")