from . import card
import random

class Deck:


    def __init__( self ):
        suits = [ "♠ spades" , "♥ hearts" , "♣ clubs" , "♦ diamonds" ]
        self.cards = [] 

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace" 
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def deal(self,players,numberCards):
        for player in players:
            for i in range(numberCards):
                player.addCard(self.cards[i])
            self.cards[0:numberCards] = []
    
    def changeCards(self, player, cardChanges):
        for i in range(len(cardChanges)):
            player.cards[int(cardChanges[i])-1] = self.cards[i]
        self.cards[0:len(cardChanges)] = []

    
    def checkWinner(self, players):
        max = 0
        winner = ""
        for player in players:
            value = 0
            equalsNumber = []
            equalsFigure = []
            ladder = True
            checkLadder = False
            player.cards.sort(key=lambda x: x.point_val)
            val_init = player.cards[0].point_val - 1
            for card in player.cards:
                if card.point_val - val_init == 1 and checkLadder:
                    ladder = True
                else:
                    ladder = False
                    checkLadder = False
                
                if len(equalsNumber) == 0:
                    equalsNumber.append([card.point_val])
                else:
                    added = False
                    for numArr in equalsNumber:
                        if card.point_val in numArr:
                            numArr.append(card.point_val)
                            added = True
                    if not added:
                        equalsNumber.append([card.point_val])
                
                if len(equalsFigure) == 0:
                    equalsFigure.append([card.suit])
                else:
                    added = False
                    for figArr in equalsFigure:
                        if card.suit in figArr:
                            figArr.append(card.suit)
                            added = True
                    if not added:
                        equalsFigure.append([card.suit])
            
            pair = 0
            thresome = 0
            poker = 0
            flush = 0
            for arrNum2 in equalsNumber:
                if(len(arrNum2) == 2):
                    pair += 1
                if(len(arrNum2) == 3):
                    thresome += 1
                if(len(arrNum2) == 4):
                    poker += 1

            for arrNum2 in equalsFigure:
                if(len(arrNum2) == 5):
                    flush += 1
                
            if(flush and ladder):
                value = 10
            elif(poker == 1):
                value = 8
            elif(thresome == 1 and pair == 2):
                value = 7
            elif(flush):
                value = 6
            elif(ladder):
                value = 5
            elif(thresome == 1):
                value = 4
            elif(pair == 2):
                value = 3
            elif(pair == 1):
                value = 2
            else:
                value = 1 

            print(f"Player:{player.name} Value:{value}")
            if value > max:
                max = value
                winner = player.name
            
        return winner 
    
