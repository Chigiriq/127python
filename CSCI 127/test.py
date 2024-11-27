soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]

print(soccer_seasons)

# n=0
# print("season 1")
# print(soccer_seasons[0+n])

# n=1
# print("season 2")
# print(soccer_seasons[0+n])

# n=2
# print("season 3")
# print(soccer_seasons[0+n])

# n=3
# print("season 4")
# print(soccer_seasons[0+n])

# print("\nlist length:", len(soccer_seasons))

for i in range(len(soccer_seasons)):
    games = soccer_seasons[0 + i][0]
    points = soccer_seasons[0 + i][1]
    
    print("season", i+1)
    print(soccer_seasons[0 + i])
    print("games:", games)
    print("points:", points)
    print("\n")