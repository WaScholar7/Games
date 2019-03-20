import random as random

UserChips = 50
aiPlayer2Chips = 75
aiPlayer3Chips = 75
aiPlayer4Chips = 75

def EndGame():
    input('Thanks for playing!')
    exit()

def DealingPhase(Players, Shuffled_Deck):
    for times in range(2):
        for Player in Players:
            DrawCard(Player, Shuffled_Deck)
    BettingPhase()

def fold():
    return 'NO'


def TheShowdown():
    Remaining = []
    global UserHand
    global aiPlayer2Status
    global aiPlayer3Status
    global aiPlayer4Status
    global aiPlayer2
    global aiPlayer3
    global aiPlayer4
    global Pot
    global UserChips
    global aiPlayer2Chips
    global aiPlayer3Chips
    global aiPlayer4Chips
    print('_______________________________')
    print('|The cards:                    ')
    print('|'+format(Card1))
    print('|'+format(Card2))
    print('|'+format(Card3))
    print('|'+format(Card4))
    print('|'+format(Card5))
    print('|TIER LIST OF HANDS (Highest to lowest):')
    print('1)Royal straight flush')
    print('2)Straight Flush')
    print('3)Four of a kind')
    print('4)Full house')
    print('5)Flush')
    print('6)Straight')
    print('7)Three of a kind')
    print('8)Two pair')
    print('9)Pair')
    print('10)High card')
    if aiPlayer2Status == 'YES':
        print('|Bot 1\'s hand: ' + format(aiPlayer2[0])+' '+format(aiPlayer2[1]))
        Remaining.append('Bot 1')
    if aiPlayer3Status == 'YES':
        print('|Bot 2\'s hand: '+ format(aiPlayer3[0])+' '+format(aiPlayer3[1]))
        Remaining.append('Bot 2')
    if aiPlayer4Status == 'YES':
        print('|Bot 3\'s hand: '+ format(aiPlayer4[0])+' '+format(aiPlayer4[1]))
        Remaining.append('Bot 3')
    Remaining.append('you')
    print('|Your hand: '+format(UserHand[0])+' '+format(UserHand[1]))
    print('(Use the list 1-10)')
    HandDictionary = {}
    if 'Bot 1' in Remaining:
        aiPlayer2Win = input('What hand did Bot 1 have?: ')
        while aiPlayer2Win not in ['1','2','3','4','5','6','7','8','9','10']:
            aiPlayer2Win = input('What hand did Bot 1 have (1-10)?: ')
        HandDictionary.setdefault('Bot 1',aiPlayer2Win)
    if 'Bot 2' in Remaining:
        aiPlayer3Win = input('What hand did Bot 2 have?: ')
        while aiPlayer3Win not in ['1','2','3','4','5','6','7','8','9','10']:
            aiPlayer3Win = input('What hand did Bot 1 have (1-10)?: ')
        HandDictionary.setdefault('Bot 2',aiPlayer3Win)
    if 'Bot 3' in Remaining:
        aiPlayer4Win = input('What hand did Bot 3 have?: ')
        while aiPlayer4Win not in ['1','2','3','4','5','6','7','8','9','10']:
            aiPlayer4Win = input('What hand did Bot 1 have (1-10)?: ')
        HandDictionary.setdefault('Bot 3',aiPlayer4Win)
    UserWin = input('What hand did you have?: ')
    while UserWin not in ['1','2','3','4','5','6','7','8','9','10']:
        UserWin = input('What hand did you have (1-10)?: ')
    HandDictionary.setdefault('User',UserWin)
    Lowest = 99
    for key in HandDictionary:
        Temp = HandDictionary[key]
        if int(Temp) < int(Lowest):
            Lowest = Temp
            Name = key
    Winner = Name
    print('|Congrats '+format(Winner)+', you won!')
    print('|The pot of: '+format(Pot)+' chips is now yours!')
    if Winner =='Bot 1':
        aiPlayer2Chips+=Pot
    elif Winner =='Bot 2':
        aiPlayer3Chips+=Pot
    elif Winner =='Bot 3':
        aiPlayer4Chips+=Pot
    else:
        UserChips+=Pot
    Pot-=Pot
    PlayAgain = input('Would you like to continue(YES/NO)?: ')
    while PlayAgain not in ['YES','Yes','yes','NO','No','no']:
        PlayAgain = input('Would you like to continue(YES/NO)?: ')
    if PlayAgain in ['YES','Yes','yes']:
        Game()
    else:
        EndGame()
    
    

def TurnPass():
    return 0

def aiBets(BotChips):
    BotBet = random.randint(1,3)
    return BotBet

def BurnCard():
    Shuffled_Deck.remove(Shuffled_Deck[-1])

def Dealer():
    BurnCard()
    if Turn == 1:
        global Card1
        Card1 = Shuffled_Deck[-1]
        Shuffled_Deck.remove(Shuffled_Deck[-1])
        global Card2
        Card2 = Shuffled_Deck[-1]
        Shuffled_Deck.remove(Shuffled_Deck[-1])
        global Card3
        Card3 = Shuffled_Deck[-1]
        Shuffled_Deck.remove(Shuffled_Deck[-1])
    elif Turn == 2:
        global Card4
        Card4 = Shuffled_Deck[-1]
        Shuffled_Deck.remove(Shuffled_Deck[-1])
    elif Turn == 3:
        global Card5
        Card5 = Shuffled_Deck[-1]
        Shuffled_Deck.remove(Shuffled_Deck[-1])
    BettingPhase()

def BotDecideToMatch(Bet, Better):
    for Bot in BotList:                     #For every bot in the List
        Chance = ['YES','YES','YES','YES','YES','YES','YES','NO','YES','NO']
        global aiPlayer2Exist
        global aiPlayer2Status
        global aiPlayer3Exist
        global aiPlayer3Status
        global aiPlayer4Exist
        global aiPlayer4Status
        global aiPlayer2Chips
        global aiPlayer3Chips
        global aiPlayer4Chips
        global Pot
        if Bot == aiPlayer2 and Better != aiPlayer2 and aiPlayer2Exist == 'EXIST' and aiPlayer2Status =='YES':              #If it's bot 1
            if Bet > aiPlayer2Chips:    #If the user bets more than the bot has
                aiPlayer2Status = fold()    #Returns: NO
                print('Bot 1 has folded!')
                
            aiPlayer2Status = random.choice(Chance)   #If the bot has the cash
            if aiPlayer2Status =='YES' and Bet <= aiPlayer2Chips:                                         #If it's bot 1
                aiPlayer2Chips -= Bet                                       #Takes the amount of chips from the bot
                print('Bot 1 has decided to match, and has put in '+format(Bet)+' chips.')
                Pot+=Bet
            elif aiPlayer2Status =='NO':
                aiPlayer2Status = fold()
                print('Bot 1 has folded!')
        if Bot == aiPlayer3 and Better != aiPlayer3 and aiPlayer3Exist == 'EXIST' and aiPlayer3Status =='YES':
            if Bet > aiPlayer3Chips:
                aiPlayerStatus = fold()
                print('Bot 2 has folded!')
                
            aiPlayer3Status = random.choice(Chance)
            if aiPlayer3Status =='YES' and Bet <= aiPlayer3Chips:
                aiPlayer3Chips -= Bet
                print('Bot 2 has decided to match, and has put in '+format(Bet)+' chips.')
                Pot+=Bet
                
            elif aiPlayer3Status =='NO':
                aiPlayer3Status = fold()
                print('Bot 2 has folded!')
        if Bot == aiPlayer4 and Better != aiPlayer4 and aiPlayer4Exist == 'EXIST' and aiPlayer4Status == 'YES':

            if Bet > aiPlayer4Chips:
                aiPlayer4Status = fold()
                print('Bot 3 has folded!')
            aiPlayer4Status = random.choice(Chance)
            if aiPlayer4Status =='YES' and Bet <= aiPlayer4Chips:
                aiPlayer4Chips -= Bet
                print('Bot 3 has decided to match, and has put in '+format(Bet)+' chips.')
                Pot+=Bet
                
            elif aiPlayer4Status =='NO':
                aiPlayer4Status = fold()
                print('Bot 3 has folded!')
        if aiPlayer2Status == 'NO' and aiPlayer3Status == 'NO' and aiPlayer4Status == 'NO':
            WinByBruteForce()
        
            
def BotBetting():
    global UserChips
    global aiPlayer2Status
    global aiPlayer2Exist
    global aiPlayer2Chips
    global aiPlayer3Status
    global aiPlayer3Exist
    global aiPlayer3Chips
    global aiPlayer4Status
    global aiPlayer4Exist
    global aiPlayer4Chips
    global Pot
    for Bot in BotList:
        active = 'ACTIVE'
        Better = Bot
        decider = random.randint(1,5)
##        if aiPlayer2Chips <= 0:
##            aiPlayer2Status = fold()
##        if aiPlayer3Chips <= 0:
##            aiPlayer3Status = fold()
##        if aiPlayer4Chips <= 0:
##            aiPlayer4Status = fold()
        if decider ==1:                #If it's 1
            if Bot == aiPlayer2 and aiPlayer2Status == 'YES' and aiPlayer2Exist =='EXIST':        #If the bot is this bot
                while active == 'ACTIVE' and aiPlayer2Chips > 0:       #If active is ACTIVE
                    Bet = random.randint(1,3)   #Set the bet between 1-3
                    if Bet > aiPlayer2Chips:    #If it's more than they have
                        Bet = 0                 #Placeholder statement that does nothing
                    else:
                        active = 'INACTIVE'
                        aiPlayer2Chips -= Bet
                        Pot+=Bet
                        
                        
            if Bot == aiPlayer3 and aiPlayer3Status == 'YES' and aiPlayer3Exist == 'EXIST':
                while active == 'ACTIVE' and aiPlayer3Chips > 0:
                    Bet = random.randint(1,3)
                    if Bet > aiPlayer3Chips:
                        Bet = 0
                    else:                           
                        active = 'INACTIVE'
                        aiPlayer3Chips -= Bet
                        Pot+=Bet
                        
            if Bot == aiPlayer4 and aiPlayer4Status == 'YES' and aiPlayer4Exist == 'EXIST':
                while active == 'ACTIVE' and aiPlayer4Chips > 0:
                    Bet = random.randint(1,3)
                    if Bet > aiPlayer4Chips:
                        Bet = 0
                    else:
                        active = 'INACTIVE'
                        aiPlayer4Chips -= Bet
                        Pot+=Bet
                        
                        
        if active == 'INACTIVE':            #If one of these bots bet
            if Bot ==aiPlayer2:
                print('Bot 1 has decided to raise the pot '+format(Bet)+' chips.')
            elif Bot ==aiPlayer3:
                print('Bot 2 has decided to raise the pot '+format(Bet)+' chips.')
            else:
                print('Bot 3 has decided to raise the pot '+format(Bet)+' chips.')
            BotDecideToMatch(Bet, Bot)      #Bots decide to stay or fold
            UserMatch(Bet, Bot)             #User decides to stay or fold
    Dealer()

def AnotherRound():
    global UserChips
    global Pot
    global aiPlayer2Chips
    global aiPlayer3Chips
    global aiPlayer4Chips
    global aiPlayer2Status
    global aiPlayer3Status
    global aiPlayer4Status
    Again = []
    Really = input('Do you still want to play another round (YES/NO)?')
    while Really not in ['YES','Yes','yes','NO','No','no']:
        Really = input('Do you still want to play another round (YES/NO)?')
    if Really in ['YES','Yes','yes']:
        DoNothing = 'Hi Mr. Stolter'
    else:
        EndGame()
    if aiPlayer2Status == 'YES':
        Again.append('aiPlayer2')
    if aiPlayer3Status == 'YES':
        Again.append('aiPlayer3')
    if aiPlayer4Status == 'YES':
        Again.append('aiPlayer4')
    decider = random.choice(Again)
    if decider == 'aiPlayer2':
        print('Bot 1 has won the pot of '+format(Pot)+' chips.')
        aiPlayer2Chips += Pot
        Pot-=Pot
    elif decider == 'aiPlayer3':
        print('Bot 2 has won the pot of '+format(Pot)+' chips.')
        aiPlayer3Chips += Pot
        Pot-=Pot
    elif decider == 'aiPlayer4':
        print('Bot 3 has won the pot of '+format(Pot)+' chips.')
    Game()
            
def UserMatch(Bet, Bot):
    global UserChips
    global Pot
    global aiPlayer2Chips
    global aiPlayer3Chips
    global aiPlayer4Chips
    global aiPlayer2Status
    global aiPlayer3Status
    global aiPlayer4Status
    if Bet > UserChips:
        print('A player has just bet more than you have. You\'re out!')
        AnotherRound()
    if Bot == aiPlayer2 and aiPlayer2Status == 'NO':
        return
    elif Bot == aiPlayer3 and aiPlayer3Status == 'NO':
        return
    elif Bot == aiPlayer4 and aiPlayer4Status == 'NO':
        return
    else:
        guard = 'wassup'
    global agree
    agree = input('Will you stay in, and bet '+format(Bet)+' chips (YES/NO)?: ')
    while agree not in ['YES','Yes','yes','NO','No','no']:
        agree = input('Will you stay in (YES/NO)')
    if agree in ['YES','Yes','yes']:
        UserChips -= Bet
        Pot+=Bet
        
    else:
        
        
        
        Again = []
        Really = input('Do you still want to play another round (YES/NO)?')
        while Really not in ['YES','Yes','yes','NO','No','no']:
            Really = input('Do you still want to play another round (YES/NO)?')
        if Really in ['YES','Yes','yes']:
            DoNothing = 'Hi Mr. Stolter'
        else:
            EndGame()
        if aiPlayer2Status == 'YES':
            Again.append('aiPlayer2')
        if aiPlayer3Status == 'YES':
            Again.append('aiPlayer3')
        if aiPlayer4Status == 'YES':
            Again.append('aiPlayer4')
        decider = random.choice(Again)
        if decider == 'aiPlayer2':
            print('Bot 1 has won the pot of '+format(Pot)+' chips.')
            aiPlayer2Chips += Pot
            Pot-=Pot
        elif decider == 'aiPlayer3':
            print('Bot 2 has won the pot of '+format(Pot)+' chips.')
            aiPlayer3Chips += Pot
            Pot-=Pot
        elif decider == 'aiPlayer4':
            print('Bot 3 has won the pot of '+format(Pot)+' chips.')
        Game()
    return
        
    
def ThrowInMoneyPlayer(UserChips):
    print('The Pot is currently: '+format(Pot))
    PotAddition = int(input('How much do you want to raise the pot?: '))
    while PotAddition > UserChips or PotAddition < 0:
        PotAddition = int(input('Your chips: '+format(UserChips)+', please bet chips you have: '))
    return PotAddition

def DefineTurn():
    global Defined
    Defined = 'YES'
    global Turn
    Turn = 0

def WinByBruteForce():
    global Pot
    global UserChips
    print('Everybody else folded, so I guess you win!')
    print('|The pot of: '+format(Pot)+' chips is now yours!')
    UserChips+=Pot
    Pot-=Pot
    PlayAgain = input('Would you like to continue(YES/NO)?: ')
    while PlayAgain not in ['YES','Yes','yes','NO','No','no']:
        PlayAgain = input('Would you like to continue(YES/NO)?: ')
    if PlayAgain in ['YES','Yes','yes']:
        Game()
    else:
        EndGame()
    
    

def TurnPass():
    return 0

    exit()

def TurnUP():
    global Turn
    Turn += 1

def BettingPhase():
    global aiPlayer2Status
    global aiPlayer3Status
    global aiPlayer4Status
    
    if aiPlayer2Status == 'NO' and aiPlayer3Status == 'NO' and aiPlayer4Status == 'NO':
        WinByBruteForce()
    UserBet = 0
    global Turn
    if Turn == 4:
        TheShowdown()
    print(' ________________________________')
    print('/       BETTING     PHASE       \\')
    global Card1
    global Card2
    global Card3
    global Card4
    global Card5
    try:
        Card1
    except NameError:
        Card1 = None
    if Card1 == None:
        fallback = 0
    else:
        print('|Cards: '+format(Card1))
    try:
        Card2
    except NameError:
        Card2 = None
    if Card2 == None:
        fallback = 0
    else:
        print('|\t'+format(Card2))
    try:
        Card3
    except NameError:
        Card3 = None
    if Card3 == None:
        fallback = 0
    else:
        print('|\t'+format(Card3))
    try:
        Card4
    except NameError:
        Card4 = None
    if Card4 == None:
        fallback = 0
    else:
        print('|\t'+format(Card4))
    try:
        Card5
    except NameError:
        Card5 = None
    if Card5 == None:
        fallback = 0
    elif Card5 == Card5:
        print('|\t'+format(Card5))
    global Pot
    print('|The Pot: '+format(Pot))
    global UserChips
    print('|Your betting chips: '+format(UserChips, ',.0f'))
    global aiPlayer2Chips
    if aiPlayer2Exist == 'EXIST' and aiPlayer2Status == 'YES':
        print('|Bot 1\'s betting chips: '+format(aiPlayer2Chips, ',.0f'))
    if aiPlayer3Exist == 'EXIST' and aiPlayer3Status == 'YES':
        global aiPlayer3Chips
        print('|Bot 2\'s betting chips: '+format(aiPlayer3Chips, ',.0f'))
    if aiPlayer4Exist == 'EXIST' and aiPlayer4Status == 'YES':
        global aiPlayer4Chips
        print('|Bot 3\'s betting chips: '+format(aiPlayer4Chips, ',.0f'))
    
    print('|Who\'s in?: ')
    print('|Bot 1: '+format(aiPlayer2Status))
    if aiPlayer3Exist =='EXIST':     
        print('|Bot 2: '+format(aiPlayer3Status))
    if aiPlayer4Exist == 'EXIST':
        print('|Bot 3: '+format(aiPlayer4Status))
    print('|Your hand is: '+format(UserHand[0])+' '+format(UserHand[1]))
    print('|Would you like to RAISE, SKIP')
    choice = input('|or FOLD: ')
    if choice not in ['RAISE', 'SKIP', 'FOLD', 'raise', 'skip', 'fold', 'Raise', 'Skip', 'Fold']:
        BettingPhase()
    elif choice in ['RAISE', 'Raise', 'raise']:
        global Userbet
        if UserChips == 0:
            print('You can\'t raise the pot, because you have no chips to spend.')
            BettingPhase()
        Userbet = ThrowInMoneyPlayer(UserChips)
        UserChips = UserChips - Userbet
        Pot+=Userbet
        Better = 'User'
        TurnUP()
        BotDecideToMatch(Userbet, Better)
        BotBetting()
        
        
    elif choice in ['SKIP', 'Skip', 'skip']:
        TurnUP()
        BotBetting()
        
    else:
        AnotherRound()
    
    
def DrawCard(InputHand, Shuffled_Deck):
    InputHand.append(Shuffled_Deck[-1])
    Shuffled_Deck.remove(Shuffled_Deck[-1])

def Game():
    global Turn
    Turn = 0
    try:
        global Card1
        Card1
    except NameError:
        Card1 = 'DeleteMe'
    if Card1 == 'DeleteMe':
        del Card1
    else:
        del Card1
    try:
        global Card2
        Card2
    except NameError:
        Card2 = 'DeleteMe'
    if Card2 == 'DeleteMe':
        del Card2
    else:
        del Card2
    try:
        global Card3
        Card3
    except NameError:
        Card3 = 'DeleteMe'
    if Card3 == 'DeleteMe':
        del Card3
    else:
        del Card3
    try:
        global Card4
        Card4
    except NameError:
        Card4 = 'DeleteMe'
    if Card4 == 'DeleteMe':
        del Card4
    else:
        del Card4
    try:
        global Card5
        Card5
    except NameError:
        Card5 = 'DeleteMe'
    if Card5 == 'DeleteMe':
        del Card5
    else:
        del Card5
    
    global Pot
    Pot = 0
    global Defined
    Defined = 'NO'
    Suits = ['♥', '♠', '♦', '♣']
    Cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    Deck = []
    for card in Cards:
        Deck.append(card+Suits[0])
        Deck.append(card+Suits[1])
        Deck.append(card+Suits[2])
        Deck.append(card+Suits[3])
    global Shuffled_Deck
    Shuffled_Deck = []
    for x in range(len(Deck)):
        Shuffle = random.choice(Deck)
        Shuffled_Deck.append(Shuffle)
        Deck.remove(Shuffle)
    global UserHand    
    UserHand = []
    global aiPlayer2
    aiPlayer2 = []
    global aiPlayer3
    aiPlayer3 = []
    global aiPlayer2Exist
    aiPlayer2Exist = 'EXIST'

    global aiPlayer2Status
    aiPlayer2Status = 'YES'
    global aiPlayer3Exist
    aiPlayer3Exist = 'EXIST'
    global aiPlayer3Status
    aiPlayer3Status = 'YES'
    
    global aiPlayer4
    aiPlayer4 = []
    global aiPlayer4Exist
    aiPlayer4Exist = 'EXIST'

    global aiPlayer4Status
    aiPlayer4Status = 'YES'
    global Players
    Players = [UserHand, aiPlayer2, aiPlayer3, aiPlayer4]
    global BotList
    BotList = [aiPlayer2, aiPlayer3, aiPlayer4]
    global aiPlayer2Chips
    global aiPlayer3Chips
    global aiPlayer4Chips
    global UserChips
    if aiPlayer2Chips <=0:
          aiPlayer2Status = 'NO'
    if aiPlayer3Chips <=0:
          aiPlayer3Status = 'NO'
    if aiPlayer4Chips <=0:
          aiPlayer4Status = 'NO'
    if aiPlayer2Chips <=0 and aiPlayer3Chips <= 0 and aiPlayer4Chips <= 0:
        print('YOU WON THE GAME BY TAKING EVERYBODY ELSE\'S MONEY! HUZZAH!')
        EndGame()
    if aiPlayer2Status == 'YES':
          Pot+=1
          aiPlayer2Chips-=1
    if aiPlayer3Status == 'YES':
          Pot+=1
          aiPlayer3Chips-=1
    if aiPlayer4Status == 'YES':
          Pot+=1
          aiPlayer4Chips-=1
    if UserChips <= 0:
          print('Unfortunately it looks like you don\'t have enough chips to play anymore.')
          EndGame()
    else:
          Pot+=1
          UserChips-=1
    print('Everybody ante\'s up, and puts one chip in to start.')
    DefineTurn()
    
    DealingPhase(Players, Shuffled_Deck)

        
    
Game()
