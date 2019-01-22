import random 
deck=[1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
class Player():
    def __init__(self,balance=0,bet=0):
        self.balance=balance
        self.bet=bet
        self.cards=[]
        
    def __str__(self):
        return ('Your cards are: '+str(self.cards)+'\n'+'Your sum is: '+str(self.sumcards()))
    
    def sumcards(self):
        res=0
        for card in self.cards:
            if card==1:
                inp=int(input('You have an ace.\nWould you like to use it as 1 or 11?'))
                card=inp
            res+=card
        return res
    
    def hit(self):
        card1=random.choice(deck)
        deck.remove(card1)
        (self.cards).append(card1)
        
class Dealer(Player):
    def sumcards(self):
        res=0 
        for card in self.cards:
            res+=card
        return res
    def __str__(self):
        return ('Dealers cards are: '+str(self.cards)+'\n'+'Dealers sum is: '+str(self.sumcards()))
    
def play():
    global balance
    bet=int(input('What is your bet?'))
    balance-=bet
    human=Player(balance,bet)
    dealer=Dealer()
    human.hit()
    print (human)
    human.hit()
    print (human)
    dealer.hit()
    print (dealer)
    chose=input('Hit or Pass? ')
    while(chose=='Hit'):
        human.hit()
        print (human)
        if human.sumcards()>21:
            print('BUSTED!')
            break
        elif human.sumcards()==21:
            print('You have won')
            human.balance+=2*human.bet
            break
        chose=input('Hit or Pass? ')
    else:
        while(dealer.sumcards()<=human.sumcards()):
            dealer.hit()
            print (dealer)
            if dealer.sumcards()>21:
                print('Dealer BUSTED')
                human.balance+=2*(human.bet)
                break
            elif dealer.sumcards()==21:
                print('You lost')
                break
    print ('your balance is'+str(human.balance)+'\n')
    balance=human.balance
play1='Yes'

balance=int(input('How much money do you have?'))
while(play1=='Yes'):
    play()
    play1=input('Do you want to play again?')

