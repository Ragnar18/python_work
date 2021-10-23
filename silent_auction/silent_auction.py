#import clear()
from art import logo
print(logo)

end_of_bids = False
bid_dict = {}

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while not end_of_bids:
    name = input("What is your name?: ")
    bid = int(input("What is your bid: $"))
    bid_dict[name] = bid
    other_users = input("Are there other users? Type 'yes or 'no ")
    if other_users == "no":
        end_of_bids = True
        highest_bidder(bid_dict)
    elif other_users == "yes":
        end_of_bids = False
        #clear()