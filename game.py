from classes.deck import Deck
from classes.player import Player

player1 = Player("Player")
player2 = Player("Enemy")
players = [player1,player2]
deck = Deck()
deck.shuffle().deal(players,5)

for player in players:
  if player.name == "Player":
    print(player.name)
    player.show_cards()

i = 0
while i<2: 
  change = input('What cards dou you want to change?, enter separated by comma (In case you dont want to change write 0): ')
  if change == "0":
    pass
  else:
    cardsChange = change.split(",")
    deck.changeCards(player1, cardsChange)
  player1.show_cards()
  i += 1

print("-----------------")
player1.show_cards()
print("----------------------------")
player2.show_cards()
print("-----------------")
print(deck.checkWinner(players))

#deck.show_cards()