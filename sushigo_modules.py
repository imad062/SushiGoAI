"""
Author: Nooruddin Imad
"""

from numpy import random
from copy import deepcopy
from itertools import combinations

class CardDeck(object):
    """
        A class for the deck of cards.
        
        Attributes
        ----------
        _card_names : list
            Contains the unique card names.
        _card_numbers : list
            Contains the number of cards for each type.
        _cards : list
            Contains the names of all 98 cards.
        ----------

    """
    def __init__(self):
        self._card_names = ['Tempura', 'Sashimi', 'Dumpling', 'DoubleMaki', 'TripleMaki', 'SingleMaki', 'SalmonNigiri', 'SquidNigiri', 'EggNigiri', 'Wasabi', 'Chopsticks']
        self._card_numbers = [14, 14, 14, 12, 8, 6, 10, 5, 5, 6, 4]
        self._cards = [self._card_names[i] for i in range(len(self._card_names)) for j in range(self._card_numbers[i])]

    def dealCards(self, n):
        """
            Deals cards randomly to players' hands.

            Parameters
            ----------
            n : int
                Number of cards required.
            ----------

            Return
            ------
            list1, list2 : list, list
                Returns 2 lists containing n number of cards.
            ------
        """
        random.shuffle(self._cards)
        return self._cards[0:n], self._cards[n:2*n] 

class GameState(object):
    """
        Attributes
        ----------
        _p1_hand : list

        _p2_hand : list

        _p1_table : list

        _p2_table : list

        
    """
    def __init__(self):
        cardDeck = CardDeck()
        self._p1_hand, self._p2_hand = cardDeck.dealCards(6)
        self._p1_table, self._p2_table = [], []
        self._p1_total_score, self._p2_total_score = 0, 0

    def getTotalScores(self):
        return self._p1_total_score, self._p2_total_score


    def getWinningStatement(self, winstr):
        """
        """
        statements = [" is deemed worthy of the champion cup.", " jumps to the sky joyfully.", " is pronounced as the winner.", " wins and the crowd goes bonkers.", " is the chosen one.", " gets chicken dinner.", " W I N N E R "]
        random.shuffle(statements)
        return winstr + statements[random.randint(0, len(statements))]

    def getVanillaWinningStatement(self, winstr):
        """
        """
        return winstr + "wins this round."

    def getTables(self):

        """
        """
        return self._p1_table, self._p2_table
    
    def getHands(self):

        """
        """
        return self._p1_hand, self._p2_hand

    def _swap(self):

        """
        """
        self._p1_hand, self._p2_hand = self._p2_hand, self._p1_hand
        return self._p1_hand, self._p2_hand

    def play(self, p1_move, p2_move):
        """

        """
        p1_valid, p2_valid = False, False
        p1_spoon, p2_spoon = False, False

        #check if the the move of p1 is valid
        #There can be two moves -> 0 means normal put in table, 1 means spoon swap
        if p1_move[0] == 0 and p1_move[1] in self._p1_hand:
            p1_valid = True
        elif p1_move[0] == 1 and 'Chopsticks' in self._p1_table and p1_move[1][0] in self._p1_hand and p1_move[1][1] in self._p1_hand:
            p1_valid, p1_spoon = True, True

        #check the validity of p2_move
        if p2_move[0] == 0 and p2_move[1] in self._p2_hand:
            p2_valid = True
        elif p2_move[0] == 1 and 'Chopsticks' in self._p2_table and p2_move[1][0] in self._p2_hand and p2_move[1][1] in self._p2_hand:
            p2_valid, p2_spoon = True, True

        if p1_valid and p2_valid:
            if p1_spoon:
                #perform a chopstick swap
                #remove chopstick from p1 table
                self._removeFromP1Table('Chopsticks')
                #add chopstick to p1 hand
                self._addToP1Hand('Chopsticks')
                #remove the two cards from p1 hand
                card1 = p1_move[1][0]
                card2 = p1_move[1][1]

                self._removeFromP1Hand(card1)
                self._removeFromP1Hand(card2)
                #add two cards into p1 table
                self._addToP1Table(card1)
                self._addToP1Table(card2)

            else:
                #normal card play
                #remove card from p1 hand
                card1 = p1_move[1]

                self._removeFromP1Hand(card1)
                #add card to p1 table
                self._addToP1Table(card1)
            
            if p2_spoon:
                self._removeFromP2Table('Chopsticks')

                self._addToP2Hand('Chopsticks')

                card1 = p2_move[1][0]
                card2 = p2_move[1][1]

                self._removeFromP2Hand(card1)
                self._removeFromP2Hand(card2)

                self._addToP2Table(card1)
                self._addToP2Table(card2)
                
            else:
                card1 = p2_move[1]

                self._removeFromP2Hand(card1)
                self._addToP2Table(card1)

            #perform swap to swap the hands
            self._swap()

        else:
            print("[ ERROR : play() -> invalid play. ]")

    def printP1Hand(self):
        print("P1 Hand: ", end="")
        print(self._p1_hand)

    def printP2Hand(self):
        print("P2 Hand: ", end="")
        print(self._p2_hand)

    def printHands(self):
        self.printP1Hand()
        self.printP2Hand()
    
    def printP1Table(self):
        print("P1 Table: ", end="")
        print(self._p1_table)

    def printP2Table(self):
        print("P2 Table: ", end="")
        print(self._p2_table)

    def printTable(self):
        print("P1 Table: ", end="")
        print(self._p1_table)
        print("P2 Table: ", end="")
        print(self._p2_table)

    def _addToP1Table(self, card):

        """
        """
        if self._p1_table.count('Wasabi') > 0 and 'Nigiri' in card:
            self._p1_table.remove('Wasabi')
            self._p1_table.append(card + 'Wasabi')
        else:
            self._p1_table.append(card)

    def _addToP2Table(self, card):

        """
        """
        if self._p2_table.count('Wasabi') > 0 and 'Nigiri' in card:
            self._p2_table.remove('Wasabi')
            self._p2_table.append(card + 'Wasabi')
        else:
            self._p2_table.append(card)

    def _addToP1Hand(self, card):
        """
        """
        self._p1_hand.append(card)

    def _addToP2Hand(self, card):
        """
        """
        self._p2_hand.append(card)
    
    def _removeFromP1Hand(self, card):
        """
        """
        self._p1_hand.remove(card)
    
    def _removeFromP2Hand(self, card):
        """
        """
        self._p2_hand.remove(card)

    def _removeFromP1Table(self, card):
        """
        """
        self._p1_table.remove(card)
    
    def _removeFromP2Table(self, card):
        """
        """
        self._p2_table.remove(card)

    def _evalScores(self):

        """

        """

        p1_total, p1_maki = 0, 0
        p2_total, p2_maki = 0, 0
        p1_table, p2_table = self._p1_table, self._p2_table

        p1_total += 5 * (p1_table.count('Tempura') / 2)
        p1_total += 10 * (p1_table.count('Sashimi') / 3)
        p1_total += (p1_table.count('Dumpling') * (p1_table.count('Dumpling') + 1)) / 2
        p1_maki += p1_table.count('SingleMaki') + 2 * p1_table.count('DoubleMaki') + 3 * p1_table.count('TripleMaki')
        p1_total += p1_table.count('EggNigiri')
        p1_total += 2 * p1_table.count('SalmonNigiri')
        p1_total += 3 * p1_table.count('SquidNigiri')
        p1_total += 3 * p1_table.count('EggNigiriWasabi')
        p1_total += 6 * p1_table.count('SalmonNigiriWasabi')
        p1_total += 9 * p1_table.count('SquidNigiriWasabi')
    

        p2_total += 5 * (p2_table.count('Tempura') / 2)
        p2_total += 10 * (p2_table.count('Sashimi') / 3)
        p2_total += (p2_table.count('Dumpling') * (p2_table.count('Dumpling') + 1)) / 2
        p2_maki += p2_table.count('SingleMaki') + 2 * p2_table.count('DoubleMaki') + 3 * p2_table.count('TripleMaki')
        p2_total += p2_table.count('EggNigiri')
        p2_total += 2 * p2_table.count('SalmonNigiri')
        p2_total += 3 * p2_table.count('SquidNigiri')
        p2_total += 3 * p2_table.count('EggNigiriWasabi')
        p2_total += 6 * p2_table.count('SalmonNigiriWasabi')
        p2_total += 9 * p2_table.count('SquidNigiriWasabi')

        """
        if p1_maki > p2_maki:
            p1_total += 6
            p2_total += 3
        elif p1_maki < p2_maki:
            p1_total += 3
            p2_total += 6
        else:
            p1_total += 3
            p2_total += 3
        """
        maki_diff = 0

        if p1_maki > p2_maki:
            maki_diff = 6
            if p2_maki > 0:
                maki_diff = 3
        if p2_maki > p1_maki:
            maki_diff = -6
            if p1_maki > 0:
                maki_diff = -3

        self._p1_total_score = p1_total + maki_diff
        self._p2_total_score = p2_total

        #return p1_total if p1_total > p2_total else p2_total
        return p1_total - p2_total + maki_diff

    def finished(self):
        return len(self._p1_hand) == 0 and len(self._p2_hand) == 0


def findP2BestMove(G, alpha, beta):
        """
        """
        p1_hand, p2_hand = G.getHands()
        p1_table, p2_table = G.getTables()

        #If there is only one card to play, play it.
        if len(p2_hand) == 1:
            H = deepcopy(G)
            H.play([0,p1_hand[0]],[0,p2_hand[0]])
            return [0,p2_hand[0]], H._evalScores()

        #Collect all possible moves for p1. Moves are cards in hand or chopstick swaps.
        p1_moves = [[0,c] for c in set(p1_hand)]
        if 'Chopsticks' in p1_table:
            p1_swaps_set = set(combinations(p1_hand,2))
            p1_swaps = [[1,list(s)] for s in p1_swaps_set]

            #Allow chopstick swaps for wasabi and nigiri in either order, so that
            #wasabi can either be applied immediately or saved for later.
            wasabi_swap_reorders = []
            for s in p1_swaps:
                if 'Wasabi' in s[1] and ('Nigiri' in s[1][0] or 'Nigiri' in s[1][1]):
                    wasabi_swap_reorders.append([1,[s[1][1],s[1][0]]])

            p1_swaps += wasabi_swap_reorders
            p1_moves += p1_swaps

        #Collect all possible moves for p2. Moves are cards in hand or chopstick swaps.
        p2_moves = [[0,c] for c in set(p2_hand)]
        if 'Chopsticks' in p2_table:
            p2_swaps_set = set(combinations(p2_hand,2))
            p2_swaps = [[1,list(s)] for s in p2_swaps_set]

            #Allow chopstick swaps for wasabi and nigiri in either order, so that
            #wasabi can either be applied immediately or saved for later.
            wasabi_swap_reorders = []
            for s in p2_swaps:
                if 'Wasabi' in s[1] and ('Nigiri' in s[1][0] or 'Nigiri' in s[1][1]):
                    wasabi_swap_reorders.append([1,[s[1][1],s[1][0]]])

            p2_swaps += wasabi_swap_reorders
            p2_moves += p2_swaps

        #Minimax it up with alpha-beta pruning, p2 is the minimizing player.
        ev_p2 = 1000
        for p2_move in p2_moves:
            ev_p1 = -1000

            for p1_move in p1_moves:
                H = deepcopy(G)
                H.play(p1_move, p2_move)

                #Hold onto the best outcome for p1 from this node, pass the best outcomes
                #seen so far for each player down the call stack.
                ev_p1 = max(ev_p1, findP2BestMove(H, ev_p1, ev_p2)[1])

                #If we already know p2 can force a better outcome from an earlier move than
                #p1 can force from this one, no need to explore any more children of this node.
                if beta < ev_p1:
                    break

            #Hold onto the best outcome and best move for p2 from this node. The value
            #of a p2 move is the value of the p1 move that would follow it when p1 plays
            #using minimax, i.e. ev_p1.
            if ev_p1 < ev_p2:
                p2_best_move = p2_move
            ev_p2 = min(ev_p1, ev_p2)

            #If we already know p1 can force a better outcome from an earlier move than
            #p2 can force from this one, no need to explore any more children of this node.
            if alpha > ev_p2:
                break

        return p2_best_move, ev_p2

        


        



        
