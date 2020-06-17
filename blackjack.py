#BlackJack game 
#The planning 
import random 
# Dealer cards 
dealer_cards = []
# Player cards 
player_cards = []

# Dealer Cards
while len(dealer_cards) !=2:
    dealer_cards.append(random.randint(7,11))
    if len(dealer_cards) ==2:
        print("Dealer has x &", dealer_cards[1])

# Player cards 
while len(player_cards) !=2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You have ", player_cards)

# Sum of the dealer 
if sum(dealer_cards) == 21:
    print("Dealer has won with 21!")
elif sum(dealer_cards) > 21:
    print("Dealer went bust!")


# Sum of the player 
while sum(player_cards) < 21:
    action = str(input("Do you want to stay or hit?  "))
    if action == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break

if sum(player_cards) > 21:
    print("YOU ARE BUSTED! Dealer wins!")
elif sum(player_cards) == 21:
    print("BlackJack player wins!")
    
