#compare a search term vs another search term
#the first search wil have a value and the second you need to guess which is higher
#you are comparing to followers on instagram
from random import randint
from data import dataset


game_on = True
score = 0
while(game_on == True):
    #print(game_on," at teh start")
    A = dataset.pop(randint(0,len(dataset)-1))
    B = dataset.pop(randint(0,len(dataset)-1))
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print("VS.")
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
    print(A['follower_count'],B["follower_count"])
    followerCount = input("Who has more followers? Type 'A' or 'B': ")
    
    
    if (followerCount == "A" and A['follower_count'] > B["follower_count"]) or (followerCount == "B" and B['follower_count'] > A["follower_count"]):
        score+=1
        print(f"\nYou're right! Current score: {score}")
    elif (followerCount == "A" and A['follower_count'] < B["follower_count"]) or (followerCount == "B" and B['follower_count'] < A["follower_count"]):
        game_on = False
        print(f"Sorry, that's wrong. Final score: {score}")