print("Welcome to the secret auction program.")

#take input for name, bid, asks if there is another bidder
#if there are other bid we clear the screen and go to add another bidder
#after we are finished inputting bids we print who won and how much they bet
#needs to include a dictionary

def runAuction():
    auction = {}
    other_bidder = "yes"
    while other_bidder == "yes":
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        other_bidder = input("Are there are any other bidders? Type 'yes' or 'no'.\n")
        auction[bid] = name
    highest_bid = 0
    for bids in auction:
        if bids > highest_bid:
            highest_bid = bids
    print(f"The winner is {auction[highest_bid]} with a bid of ${highest_bid}")
runAuction()



print("Welcome to the secret auction program.")

#take input for name, bid, asks if there is another bidder
#if there are other bid we clear the screen and go to add another bidder
#after we are finished inputting bids we print who won and how much they bet
#needs to include a dictionary

def runAuction():
    cont = "yes"
    while cont == 'yes':
        bids = {}
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        bids[name] = price
        cont = input("Are there other bidders? Type 'yes' or 'no'.\n")
    highest_bid = 0
    winner = ""
    for bid in bids:
        if bids[bid] > highest_bid:
            winner = ""
            winner = bid
            highest_bid = bids[bid]
    print(f"The winner is {winner} with a bet of ${highest_bid}")
   
runAuction()