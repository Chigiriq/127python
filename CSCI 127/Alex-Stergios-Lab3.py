# --------------------------------------
# CSCI 127, Lab 3                      |
# Date                  |
# Your Name                            |
# -------------------------------------- 
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------


def count_built_in(sentence):
    sentence.lower()
    ans = sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u")
    return ans
    

def count_iterative(sentence):
    vowels = "aeiou"
    sentence.lower()
    ans = 0
    
    for i in sentence:
        if i in vowels:
            ans += 1
    
    return ans
    


def count_recursive(sentence):
    vowels = "AEIOUaeiou"
    
    #base case... no vowel ever
    if sentence == "":
        ans = 0
       
    #general case
    else:
        #vowel there
        if sentence[0] in vowels:
            ans = count_recursive(sentence[1:]) + 1
        
        #no vowel
        else:
            ans = count_recursive(sentence[1:])
            
    return ans
    
    #... theres probably a simpler way but this is how the solution makes sense in my head
    
       
       
# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()