file = open('alignment.txt', 'r')
# print(file.read())
max_align = 0
curr_align = 0

while 1:
    char = file.read(1)          # read by character
    

    if not char: 
        break
    if char == "*":
    	curr_align = curr_align + 1
    elif char == " " or char == ".":
    	curr_align = 0

    if curr_align > max_align:
    	max_align = curr_align

    # print(char)

print (max_align)
file.close()