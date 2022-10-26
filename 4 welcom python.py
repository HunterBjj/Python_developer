
height = 11
width = height * 3
for stick_count in range(1, 6): # range(start, stop, step)
    print((".|. "*stick_count).center(width, "-")) 

print("Welcom".center(width,"-"))

for stick_count in range(5, 0,-1):
    print((".|. "*stick_count).center(width, "-"))



