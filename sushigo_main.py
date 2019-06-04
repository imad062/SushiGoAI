from sushigo_modules import CardDeck, GameState, findP2BestMove
from copy import deepcopy

def main():
    G = GameState()
    game_mode = 0

    print("\nSushiGo!\n")
    while not(game_mode in ['1','2']):
        game_mode = input("1. Human vs Human, 2. Human vs Robot: ")

    while not(G.finished()):
        print(G.finished())
        print(len(G._p1_hand))
        print(len(G._p2_hand))

        p1_hand, p2_hand = G.getHands()
        p1_table, p2_table = G.getTables()

        print ('\n')
        print ("p1's hand: " + str(p1_hand) + '\n')
        print ("p1's table: " + str(p1_table) + '\n')
        print ("p2's hand: " + str(p2_hand) + '\n')
        print ("p2's table: " + str(p2_table) + '\n')

        #Human vs Human
        if game_mode == '1':
            p1_input = input("p1's play: ")

            #Parse human input, checking for a swap if it occurred.
            if p1_input[:9] == 'Swap for ':
                #[1,[c1,c2]] denotes a chopstick swap for cards c1 and c2 (in that order).
                p1_select = [1, [p1_input[(p1_input.index('for ') + 4):p1_input.index(' and')], p1_input[p1_input.index('and ') + 4:]]]
            else:
                #[0,c] denotes playing the card c.
                p1_select = [0, p1_input]

            p2_input = input("p2's play: ")

            #Parse human input, checking for a swap if it occurred.
            if p2_input[:9] == 'Swap for ':
                #[1,[c1,c2]] denotes a chopstick swap for cards c1 and c2 (in that order).
                p2_select = [1, [p2_input[(p2_input.index('for ') + 4):p2_input.index(' and')], p2_input[p2_input.index('and ') + 4:]]]
            else:
                #[0,c] denotes playing the card c.
                p2_select = [0, p2_input]

        #Human vs Robot
        elif game_mode == '2':
            p1_input = input("p1's play: ")

            #Parse human input, checking for a swap if it occurred.
            if p1_input[:9] == 'Swap for ':
                #[1,[c1,c2]] denotes a chopstick swap for cards c1 and c2 (in that order).
                p1_select = [1, [p1_input[(p1_input.index('for ') + 4):p1_input.index(' and')], p1_input[p1_input.index('and ') + 4:]]]
            else:
                #[0,c] denotes playing the card c.
                p1_select = [0, p1_input]

            #Find optimal robot move.
            p2_select = findP2BestMove(deepcopy(G), -1000, 1000)[0]

            #Pretty printing for robot move.
            if p2_select[0] == 0:
                p2_play = p2_select[1]
            elif p2_select[0] == 1:
                p2_play = 'Swap for ' + p2_select[1][0] + ' and ' +  p2_select[1][1]

            print ("p2's play: " + p2_play)

        G.play(p1_select,p2_select)

    p1_table, p2_table = G.getTables()
    score_diff = G._evalScores()
    print(G.getTotalScores())

    print ('\n')
    print ("p1's table: " + str(p1_table) + '\n')
    print ("p2's table: " + str(p2_table) + '\n')

    
    p1_score, p2_score = G.getTotalScores()
    if p1_score > p2_score:
        print(G.getWinningStatement("P1"))
    elif p1_score < p2_score:
        print(G.getWinningStatement("P2"))
    else:
        print(G.getTotalScores())
        print("Everbody's a loser.")


if __name__ == '__main__':
    main()