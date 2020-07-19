import random

o = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8 ,9, 9, 9, 9, 10, 10, 10 ,10, 11, 11, 11, 11, 12, 12, 12, 12]
bot = 1
hand = []
hand2 = []
turns = 0



print(
    "                       **********************************************************                                    ")
print(
    "                                   Welcome to the game Casino - BLACK JACK !                                         ")
print(
    "                       **********************************************************                                    ")

def start():
    card_1 = input("Thank you for playing BlackJack!, Would you like to draw a card? y or n\n")
    if card_1 == "n":
        start()
    if card_1 == 'y':
        random_card = o[random.randint(0,49)]
        hand.append(random_card)
        global turns
        turns += 1
        print("You have drawn a faced down card")
        another()



def another():
    another_card = input("Would you like another card? y or n\n")
    if another_card == 'y':
        random_card = o[random.randint(0, 49)]
        print("You drew a {}.".format(random_card))
        hand.append(random_card)
        print("You have a {} in your hand".format(hand))
        global turns
        turns += 1
        if sum(hand) > 21:
            print('You have ' + str(sum(hand)) + ' which is too much, you busted in ' + str(turns) + ' turns' )
            hand.clear()
            turns = 0
            start()
        if sum(hand) < 21:
            another()
        if sum(hand) == 21:
            print("You've got Black Jack!")
            hand.clear()
            turns = 0 
            start()
    if another_card == 'n':
        print('You have ' + str(sum(hand)) + ' in ' + str(turns) + ' turns')
        hand.clear()
        turns = 0 
        start()




start()
