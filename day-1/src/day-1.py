# read input
data = []
with open("../in/input.txt", "r") as f:
    data = f.read().splitlines()

# variable inits
zero_hits = 0
dial_arrow_pos = 50

# loop through input
for d in data:
    # turn right
    if d[0] == "R":
        dial_arrow_pos += int(d[1:])
    # turn left
    elif d[0] == "L":
        dial_arrow_pos -= int(d[1:])
    # input error
    else:
        print("Input Error")
        continue
    # calc mod bcs of circular dial
    dial_arrow_pos = dial_arrow_pos % 100
    # check for zero hit
    if dial_arrow_pos == 0:
        zero_hits += 1

# print result
print(f"The actual password to open the door is {zero_hits}!")