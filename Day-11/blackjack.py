import random

'''
Rules
1. Can't go over 21
2. Cards 2-10 are their values, face cards are 10, and Ace is 1 or 11
3. Dealer's hand (besides the first card is hidden)
4. If we tie it is a draw, if they have 21 they win
5. If the dealers hand is 16 or less, they have to draw again
'''
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] #11 is the ace and depending on if the player will bust with it, it can rever to 1
game_start = True #condition for when the game starts to get 2 cards instead of 1


def addPoints(list): #adds up the score of your hand
    sum = 0
    for i in list:
        sum+= i
    while sum > 21:
        if 11 in list:
            one = list.index(11)
            list[one] = 1
            sum = addPoints(list)
            return sum
        else:
            return sum
    return sum

def addCard(hand): #adds a card to your hand
    hand.append(cards[random.randint(0,len(cards)-1)])

def printScore(playerCards, playerScore, dealerCards): #prints the current score of the player and score of the computer
    print(f"    Your cards: {playerCards}, current score: {playerScore}")
    print(f"    Computer's first card: {dealerCards[0]}")

def gameOver(player_finalCards, playerScore, dealer_finalCards, dealerScore): #ran when one of the game Over conditions apply
    print(f"    Your final hand: {player_finalCards}, final score: {playerScore}")
    print(f"    Computer's final hand: {dealer_finalCards}, final score: {dealerScore}")
    if (playerScore == 21 or dealerScore > 21) or playerScore > dealerScore and playerScore < 21:
        print("You win")
    elif (playerScore > 21 or dealerScore == 21) or playerScore < dealerScore:
        print("You lose")
    elif playerScore == dealerScore and playerScore <= 21:
        print("You tied")

def playerTurn(p_cards): #runs until player no longer wants to continue 
    choice = input("Type 'y'to get another cards, type 'n' to pass: ")
    if choice == 'y': #they can keep playing
        addCard(p_cards) #if they do we add a card
        p_sum = addPoints(p_cards) #sum up the new total
        print(f"    Your cards: {p_cards}, current score: {p_sum}")
        if p_sum <= 21:
            playerTurn(p_cards)
    return p_cards

def dealerTurn(d_cards): #runs after the player is done with their turn
    d_sum = addPoints(d_cards)
    if d_sum < 17: #if their score is less than 17 they have to keep adding (hence the while loop)
        addCard(d_cards)
        addPoints(d_cards)
        dealerTurn(d_cards)
    return d_cards
    
def blackjack():
    player_cards = [] 
    dealer_cards = [] 
    prompt1 = input("\n\n\n\nWould you like to play a game of BlackJack? 'y' or 'n': ")
    if prompt1 == 'y':
        game_on = True
        while game_on == True:
            game_start = True
            if game_start == True: #turn into start function    
                addCard(player_cards)
                addCard(player_cards) #player gets 2 cards
                addCard(dealer_cards)  
                addCard(dealer_cards) #dealer gets 2 cards
                game_start == False #no longer the beginning
            player_sum = addPoints(player_cards)
            dealer_sum = addPoints(dealer_cards) #adding the total to see if either get to 21
            printScore(player_cards, player_sum, dealer_cards) #print your score and dealers first card

            if player_sum < 21: #while the player is still under 21, they continue their turn
                playerTurn(player_cards)
            if player_sum > 21:
                player_sum = addPoints(player_cards)
                dealer_sum = addPoints(dealer_cards)
                gameOver(player_cards,player_sum, dealer_cards, dealer_sum)
            elif dealer_sum <= 16: #while the dealer has less than 17, they continue to draw
                dealerTurn(dealer_cards)
            #once both parties are done, we sum up both scores and print out the ending
            player_sum = addPoints(player_cards)
            dealer_sum = addPoints(dealer_cards)
            gameOver(player_cards,player_sum, dealer_cards, dealer_sum)
            game_on = False
            
        blackjack()
    else:
        print("Game over")
blackjack()