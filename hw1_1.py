import random
rank=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
dic_r={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
dic_rr={'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
suit=['CLUB','DIAMOND','HEART','SPADE']
def createShuffleDeck():
	deck=[]
	for s in suit:
		for r in rank:
			deck.append(r+"-"+s)
	random.shuffle(deck)
	return deck
def drawCard(deck,num):
	cards=[]
	for i in range(num):
		card=deck.pop(0)
		cards.append(card)
	return cards
def sumFirst(l):
	sum_l=0
	if l[0][0]!='A' or l[1][0]!='A':
		for i in range(2):
			n=l[i].find("-")
			sum_l+=dic_rr[l[i][:n]]
	else:
		sum_l=12 
	return sum_l
def end():
	if (21-sum_player)>(21-sum_dealer):
		print("***Dealer wins!***")
	if (21-sum_player)<(21-sum_dealer):
		print("***You beat the dealer!***")
	if (21-sum_player)==(21-sum_dealer):
		print("***You tied the dealer, nobody wins. ***")
def display(ll):
	l=""
	for i in range(len(ll)-1):
		l+=str(ll[i])+","
		l+=ll[len(ll)-1]
	return l
def hit(card,sum_):
	if card[0][0]=='A' and sum_>=11:
		sum_=sum_+1
	if card[0][0]=='A' and sum_<11:
		sum_=sum_+11
	if card[0][0]!='A':
		n=card[0].find("-")
		sum_+=dic_r[card[0][:n]]
	return sum_
while True:
	print()
	deck=createShuffleDeck()
	first_player=drawCard(deck,2)
	sum_player=sumFirst(first_player)
	if sum_player==21:
		print("Your current value is Blackjack!(21)\nwith the hand :",display(first_player),"\n")
	else:
		print("Your courrent value is :",sum_player,"\nwith the hand :",display(first_player),"\n")
	first_dealer=drawCard(deck,2)
	sum_dealer=sumFirst(first_dealer)
	i="1"
	while i!='0':
		i=input("Hit or stay?(Hit = 1 , Stay = 0) :")
		if i=='1':
			random.shuffle(deck)
			draw=drawCard(deck,1)
			first_player.extend(draw)
			print("You draw",draw[0],"\n")
			sum_player=hit(draw,sum_player)
			if sum_player==21:
				print("Your current value is Blackjack!(21)\nwith the hand :",display(first_player),"\n")
			if sum_player<21:
				print("Your current value is",sum_player,"\nwith the hand :",display(first_player),"\n")
			if sum_player>21:
				print("Your current value is Bust!(>21)\nwith the hand :",display(first_player),"\n")
				print("***Dealer wins!***")
				t=False
				break
		else:
			break
	if sum_dealer==21 and sum_player<=21:
		print("Dealer's current value is Blackjack!(21)\nwith the hand :",display(first_dealer),"\n")
		if sum_dealer==sum_player:
			print("***You tied the dealer, nobody wins. ***")
		else:
			print("***Dealer wins!***")
		t=False
	if sum_dealer<21 and sum_player<=21:
		print()
		print("Dealer's courrent value is :",sum_dealer,"\nwith the hand :",display(first_dealer),"\n")
		t=True
	if sum_dealer>=17 and sum_player<=21:
		e=end()
		t=False
	while t:
		if sum_dealer<17:
			random.shuffle(deck)
			h=drawCard(deck,1)
			print("Dealer draws",h[0])
			first_dealer.extend(h)
			sum_dealer=hit(h,sum_dealer)
			continue
		else:
			print()
			if sum_dealer>21:
				print("Dealer's current value is Bust!(>21)\nwith the hand :",display(first_dealer),"\n")
				print("***You beat the dealer!***")
				t=False
			if sum_dealer==21:
				print("Dealer's current value is Blackjack!(21)\nwith the hand :",display(first_dealer),"\n")
				if sum_dealer==sum_player:
					print("***You tied the dealer, nobody wins. ***")
				else:
					print("***Dealer wins!***")
				t=False
			if sum_dealer<21:
				print("Dealer's current value is",sum_dealer,"\nwith the hand :",display(first_dealer),"\n")
				e=end()
			t=False
	print()
	a=input("Want to play again? (y/n): ")
	if a=="y":
		print()
		print("-------------------------------------")
		continue
	elif a=="n":
		break
