# python v. 3.3.2

import random

def genSuit():
    suit = random.randint(1, 4)
    if suit == 1:
        return "Clubs"
    if suit == 2:
        return "Diamonds"
    if suit == 3:
        return "Hearts"
    if suit == 4:
        return "Spades"
    return "Whoops!"

def genRank():
    rank = random.randint(1, 13)
    if rank == 1:
        return "Ace"
    if rank == 11:
        return "Jack"
    if rank == 12:
        return "Queen"
    if rank == 13:
        return "King"
    return str(rank)

def drawCard():
    return genRank() + " of " + genSuit()

# def test ():
#     n = 0
#     while n < 10:
#         print (drawCard())
#         n+= 1

def value(card):
    position = card.find(" ")
    rank = card[0: position]
    # print(rank)
    if rank == "Ace":
        return 11
    if rank == "King" or rank == "Queen" or rank == "Jack":
        return 10
    return int(rank)

def hand():
    card1 = drawCard()
    card2 = drawCard()
    drawTwo = value(card1) + value(card2)

    print ("first card: ", card1, ", second card: ", card2, sep='')
    if drawTwo == 21:
        print ("Blackjack...a Natural!")
    elif drawTwo <= 16:
        card3 = drawCard()
        drawThree = value(card1) + value(card2) + value(card3)
        print ("third card: ", card3, sep='')
        if drawThree == 21:
            print ("Blackjack on third card!")
        else:
            print ("sorry, ", drawThree, " is not 21")
    else:
            print ("sorry, ", drawTwo, " is not 21")

def theGame():
    hand()
    hand()

theGame()


