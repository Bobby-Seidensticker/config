
def countVals(hand):
    res = {}
    for card in hand:
        if card[0] in res:
            res[card[0]] += 1
        else:
            res[card[0]] = 1
    return res

def highVal(hand):
    return max([card[0] for card in hand])

def lowVal(hand):
    return min([card[0] for card in hand])

def isFlush(hand):
    return all([card[1] == hand[0][1] for card in hand[1:]])

def testIsFlush():
    print 'F1: ', isFlush(convertHand('8C KC 7C TC 2C'.split(' ')))
    print 'F2: ', not isFlush(convertHand('TS 8H QD AC 5C'.split(' ')))

def isStraight(hand):
    vals = set([card[0] for card in hand])
    return all([val in vals for val in xrange(lowVal(hand), lowVal(hand) + 5)])

def testIsStraight():
    print 'S1: ', isStraight(convertHand('8C JC 7C TC 9C'.split(' ')))
    print 'S2: ', not isStraight(convertHand('TS 8H QD AC 5C'.split(' ')))

def isRF(hand):
    return highVal(hand) == 14 and isStraight(hand) and isFlush(hand)

def isStraightFlush(hand):
    return isStraight(hand) and isFlush(hand)

def isXOAK(hand, x):
    counted = countVals(hand)
    for val in counted:
        if counted[val] == x:
            return True, val
    return False, 0

def testIsXOAK():
    print '4OAK 1: ', isXOAK(convertHand('8C 8C 8C 8C 9C'.split(' ')), 4)[0]
    print '4OAK 2: ', not isXOAK(convertHand('TS 8H QD AC 5C'.split(' ')), 4)[0]

    print '3OAK 1: ', isXOAK(convertHand('8C 8C 8C TC 9C'.split(' ')), 3)[0]
    print '3OAK 2: ', not isXOAK(convertHand('TS 8H QD AC 5C'.split(' ')), 3)[0]
    print '3OAK 3: ', not isXOAK(convertHand('8C 8C 8C 8C 9C'.split(' ')), 3)[0]

    print 'Pair 1: ', isXOAK(convertHand('8C 8C 7C TC 9C'.split(' ')), 2)[0]
    print 'Pair 2: ', not isXOAK(convertHand('TS TH TD AC 5C'.split(' ')), 2)[0]
    print 'Pair 3: ', not isXOAK(convertHand('8C 8C 8C 8C 9C'.split(' ')), 2)[0]

    print 'Small Pair 1: ', isXOAK(convertHand('8C 8C'.split(' ')), 2)[0]
    print 'Small Pair 1: ', not isXOAK(convertHand('8C 7C'.split(' ')), 2)[0]
    print isXOAK([[14, 'D'], [14, 'C'], [9, 'C']], 2)
    print isXOAK(convertHand('5C AD 5D AC 9C'.split(' ')), 2)
    
def convertCard(card):
    res = []
    if card[0] == 'T':
        res.append(10)
    elif card[0] == 'J':
        res.append(11)
    elif card[0] == 'Q':
        res.append(12)
    elif card[0] == 'K':
        res.append(13)
    elif card[0] == 'A':
        res.append(14)
    else:
        res.append(int(card[0]))

    res.append(card[1])
    return res

def convertHand(hand):
    return [convertCard(card) for card in hand]

PRIMARY = 10 ** 15
PRIMARYSCORE = 10 ** 13
SECONDARYSCORE = 10 ** 11
HIGHCARDS = [10 ** i for i in xrange(9, 0, -2)]

def scoreHighCards(hand):
    hand = sorted(hand, key=lambda x: x[0])[::-1]
    result = 0
    for card, mod in zip(hand, HIGHCARDS[:len(hand)]):
        result += card[0] * mod
    return result

def scoreHand(hand):
    hand = convertHand(hand)
    final = 0

    if isRF(hand):
        final = 9 * PRIMARY
    elif isStraightFlush(hand):
        final = 8 * PRIMARY
        final += highVal(hand) * PRIMARYSCORE
    elif isXOAK(hand, 4)[0]:
        final = 7 * PRIMARY
        final += isXOAK(hand, 4)[1] * PRIMARYSCORE
    elif isXOAK(hand, 3)[0] and isXOAK(hand, 2)[0]:
        final = 6 * PRIMARY
        final += isXOAK(hand, 3)[1] * PRIMARYSCORE
        final += isXOAK(hand, 2)[1] * SECONDARYSCORE
    elif isFlush(hand):
        final = 5 * PRIMARY
        final += scoreHighCards(hand)
    elif isStraight(hand):
        final = 4 * PRIMARY
        final += highVal(hand) * HIGHCARDS[0]
    elif isXOAK(hand, 3)[0]:
        final = 3 * PRIMARY
        val = isXOAK(hand, 3)[1]
        notInvolved = [card for card in hand if card[0] != val]
        final += scoreHighCards(notInvolved)
    elif isXOAK(hand, 2)[0]:
        firstVal = isXOAK(hand, 2)[1]
        notInFirst = [card for card in hand if card[0] != firstVal]
        if isXOAK(notInFirst, 2)[0]:
            final = 2 * PRIMARY
            secondVal = isXOAK(notInFirst, 2)[1]
            final += max(firstVal, secondVal) * PRIMARYSCORE
            final += min(firstVal, secondVal) * SECONDARYSCORE
            remainder = [card for card in notInFirst if card[0] != secondVal]
            final += scoreHighCards(remainder)
        else:
            final = 1 * PRIMARY
            final += firstVal * PRIMARYSCORE
            final += scoreHighCards(notInFirst)
    else:
        final = scoreHighCards(hand)
    print hand, final
    return final

# return 1 if p1 wins, 0 if p2 wins
def doesP1Win(game):
    game = game.split(' ')

    if scoreHand(game[:5]) > scoreHand(game[5:]):
        return 1
    return 0


testIsFlush()
testIsStraight()
testIsXOAK()

'''
0 High Card: Highest value card.
1 One Pair: Two cards of the same value.
2 Two Pairs: Two different pairs.
3 Three of a Kind: Three cards of the same value.
4 Straight: All cards are consecutive values.
5 Flush: All cards of the same suit.
6 Full House: Three of a kind and a pair.
7 Four of a Kind: Four cards of the same value.
8 Straight Flush: All cards are consecutive values of same suit.
9 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
'''

allGames = open('poker').read().split('\n')

print sum([doesP1Win(x) for x in allGames])
