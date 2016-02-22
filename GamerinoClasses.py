import random
class Player:
    names = 'player'
    def __init__(self, h, a, m, c, cc, name):
        self.name = name
        self.health = h
        self.attack = a
        self.charge = c
        self.mana = m
        self.currentcharge = cc

    def currentcharge(self):
        self.currentcharge = 0

class Enemy:
    def __init__(self, h, ranb, rans, c, cc, name):
        self.name = name
        self.attack= random.randrange(ranb, rans)
        self.health = h
        self.charge = c
        self.ranbegin = ranb
        self.ranstop = rans
        self.currentcharge = cc

    def health(self):
        self.health = 120

    def attack(self):
        self.attack

    def charge(self):
        self.charge = 4

    def currentcharge(self):
        self.currentcharge = 0