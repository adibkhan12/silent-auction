import art
print(art.logo)
bidder_data = {}


def find_winner():
    highest_bid = 0
    for key in bidder_data:
        for bid in bidder_data:
            if highest_bid < bidder_data[bid]:
                highest_bid = bidder_data[bid]
        if bidder_data[key] == highest_bid:
            print(f"The winner is {key} with a bid of ${highest_bid}")


def secret_auction():
    name = input("What is your name?:")
    price = int(input("What is your bid?: $"))
    bidder_data[name] = price


secret_auction()

bid_over = False
while not bid_over:

    cont = input("Are there any other bidders? Type 'yes or 'no'.")
    if cont == "yes":
        print("\n" * 20)
        secret_auction()
    else:
        find_winner()
        bid_over = True
