#! /usr/bin/env python3
# https://projecteuler.net/problem=54

from cardlib import Card, Hand
from pokerlib import getHandRankFunc, handrankfuncs

def buildhands(line):
    """
    Builds the 2 players hands from each line in the file. Returns 2 Hand objects.
    """
    player1list = line.split(' ')[:5]
    player2list = line.split(' ')[5:]

    for c in player1list:
        card = Card(c[0], c[1])
        player1list[player1list.index(c)] = card
    
    player1hand = Hand(*player1list)
        
    for c in player2list:
        card = Card(c[0], c[1])
        player2list[player2list.index(c)] = card
    
    player2hand = Hand(*player2list)

    return player1hand, player2hand

def comparehands(hand1, hand2):
    player1hand = getHandRankFunc(hand1)
    player2hand = getHandRankFunc(hand2)
    player1index = handrankfuncs.index(player1hand)
    player2index = handrankfuncs.index(player2hand)
    #print(player1hand.__name__, player2hand.__name__)

    if player1index == player2index:
        #TODO change getHighCard() logic to count backwards from highest card until match is found
        player1highcard = hand1.getHighCard()
        player2highcard = hand2.getHighCard()
        #print(repr(player1highcard), repr(player2highcard))
        if player1highcard == player2highcard:
            return None
        elif player1highcard > player2highcard:
            return True
        else:
            return False
    elif player1index > player2index:
        return True
    else:
        return False
    assert False, 'weird error in compareHands()'

def main():
    file = open('p054_poker.txt')
    line = ''
    player1ct = 0
    player2ct = 0
    tie = 0
    while True:
        line = file.readline().rstrip()
        if not line: break
        player1, player2 = buildhands(line)
        value = comparehands(player1,player2)
        if value == True:
            player1ct += 1
        elif value == False:
            player2ct += 1
        else:
            tie += 1
    print("player1ct: %s\nplayer2ct: %s\ntie: %s" % (player1ct, player2ct, tie)) 

if __name__ == '__main__':
    line = '8C TS KC 9H 4S 7D 2S 5D 3S AC'
    main()