import math

# read input
data = []
with open("in/input.txt", "r") as f:
    data = f.read().split(",")

sum_invalid_ids = 0

# itterate over each range
for id_range in data:
    # split range string in start id and end id
    id_start = id_range.split('-')[0]
    id_end = id_range.split('-')[1]
    
    # skip invalid ranges
    if int(id_start) > int(id_end):
        continue

    # start half
    if len(id_start)%2 == 0:
        start_h = id_start[:int(len(id_start)/2)]
    else:
        start_h = int("1"+"0"*math.ceil((len(id_start)/2)-1))
    
    # end half
    if len(id_end)%2 == 0:
        end_h = id_end[:int(len(id_end)/2)]
    else:
        end_h = int("9"*math.floor(len(id_end)/2))

    # generate and test all invald ids
    for h in range(int(start_h), int(end_h)+1):
        n = int(str(h)*2)
        if n > int(id_end):
            break
        if n < int(id_start):
            continue
        #print(f"Found {n}, in range {id_range}, break is {n} > {int(id_end)} == {n > int(id_end)}")
        sum_invalid_ids += n

print(f"If I add up all of the invalid IDs, I get {sum_invalid_ids}!")


