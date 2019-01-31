def wizardish(player1='player1',player2='player2',player3='player3',player4='player4',
          p1_strategy='s1', p2_strategy='s2',p3_strategy='s3', p4_strategy='s1'):
    """
    This function simulates a game of 10 rounds similar to Wizard.
    
    Parameters
    ----------
    player_: Enter players' names. Default player_.
     
    p__strategy: s1,s2 or s3. Default s3.
             Enter players' strategies based on pre-defined ones or your own.
             Required params: hand, rank, round_n, player_. Create new inside ss.
    """
    import random
    ss = {"s1": (lambda hand, rank, n, p: sum([card>75 for card in hand])),
          "s2": (lambda hand, rank, n, p: sum([card>65 if rank[p]>2 else card>75 for card in hand])),
          "s3": (lambda hand, rank, n, p: sum([(card>(75-(rank[p]*n*.5))) if rank[p]>2 else card>75 for card in hand]))}

    players = [player1, player2, player3, player4]
    s,v = [p1_strategy, p2_strategy, p3_strategy, p4_strategy], [0, 0, 0, 0]
  
    scores = {k:v for k,v in zip(players, v)}
    guesses, win_cards, rank = scores.copy(), scores.copy(), scores.copy()
    strategies = {k:v for k,v in zip(players, s)}
    
    # Looping through 10 rounds!
    for n in range(1,11):
        print('*'*20, 'Round: %r' % n, '*'*20)

        # Start of round n: dealing
        cards = random.sample(range(1,101), n*4)  
        top_cards = sorted(cards, reverse=True)[:n]
        hand = {k:v for k,v in zip(players, [cards[i:i+n] for i in range(0,len(cards),n)])}
        
        for k,v in hand.items():
            print(k, sorted(v, reverse=True))
        print('top cards: %r' % top_cards)
        
        # Bets and round n results:
        for p in players:
            guesses[p]  = ss[strategies[p]](hand[p], rank, n, p)
            win_cards[p] = sum([1 if c in top_cards else 0 for c in hand[p]])
        
            if guesses[p] == win_cards[p]: 
                scores[p] += (2 + win_cards[p])
            else:
                scores[p] += (-abs(guesses[p] - win_cards[p]))
        
        # Calculating rank at the end of round n:
        r = {k:r for r,k in enumerate(sorted(set(scores.values()), reverse=True), 1)}
        rank = {k: r[v] for k,v in scores.items()}
        
        #print situation at the end of round n
        print('\nguesses:  ', guesses, '\nwin_card: ', win_cards)
        print('\nscores:   ', scores, '\nrank:     ', rank, '\n')

    winners = [k for k in rank if (rank[k]==min(rank.values()))]
    print("Winner, winner, chicken-dinner! ", winners, '\o/')
    return winners

wizardish()