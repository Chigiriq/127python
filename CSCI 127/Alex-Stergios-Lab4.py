# --------------------------------------
# CSCI 127, Lab 4
# Date
# Your Name
# --------------------------------------

def process_season(season, games_played, points_earned, record):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    print(record)
    
    print()

# --------------------------------------

def process_seasons(seasons):
    for i in range(len(seasons)):
        #define season, games played, and points earned
        season = i + 1
        games_played = seasons[0 + i][0]
        points_earned = seasons[0 + i][1]

        #attempt record calcs
        
        #max wins possible
        
        #middle option
        
        #least wins
        
        record = "idk" #XXX notes on this: my idea would be to use if statements and points%games 
                        #to determine max wins
                        
                        #for middle i have no idea
                        
                        #for min i suppose it would be opposite max
                        
                        #i wonder if I could use random module with while loop to simulate every scenario
                        #brute for opproach but could work assuming games played is under 50 or so
        
        process_season(season, games_played, points_earned, record)

# --------------------------------------

def main():
    # format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
    # soccer_seasons = [[2, 3], [2, 4], [2, 6], [17, 17], [17, 24], [0, 0], [10, 2], [10, 3]]
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]
    process_seasons(soccer_seasons)

# --------------------------------------

main()