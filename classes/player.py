class Player():
  def __init__(self,name):
    self.name = name
    self.cards = []

  def addCard(self, card):
    self.cards.append(card)

  def show_cards(self):
    num = 1
    for card in self.cards:
      card.card_info(num)
      num += 1