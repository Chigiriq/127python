import random
DIAMOND = 1     
HEART = 2
SPADE = 3
HORSESHOE = 4
LIBERTY_BELL = 5

#create a list of slot items


#now items have a name
reel_1 = 1
reel_2 = random.randint(1,5)
reel_3 = random.randint(1,5)

print(reel_1)
print(reel_2)
print(reel_3)


if reel_1 == DIAMOND:
    ans = True
else:
    ans = False
    
print(ans)
# print(convert(reel_1))
# print(convert(reel_2))
# print(convert(reel_3))