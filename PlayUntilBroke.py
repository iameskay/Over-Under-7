z = 0
m = 50

print "Welcome to Over/Under 7!"

while(z==0):
	if m <= 0:
		print "You lost all your money! Security is on its way to make sure you don't cause any problems and to escort you out."
		z = 1
	else:
		from random import randint
		x = randint(1,6)
		y = randint(1,6)
		sum = x + y
		print "You have $%s." %(m)
		value = raw_input("Enter how much you would like to bet on:")
		if value .isdigit():
			bet = int(value)
			if 0 < bet <= m:
				print "$%s it is! What would you like to bet on?" %(bet)
				print "1) Under 7!"
				print "2) Over 7!"
				print "3) 7!"
				print "4) Quit"
				ans = raw_input("Enter your choice:")
				if ans == "1":
					if sum < 7:
						print "The dice shows %s and %s. Congratulations! You win $%s." %(x,y,bet)
						m =  m + bet
					elif sum == 7 or sum > 7:
						print "The dice shows %s and %s. Sorry, you lose $%s." %(x,y,bet)
						m = m - bet
				elif ans == "2":
					if sum > 7:
						print "The dice shows %s and %s. Congratulations! You win $%s." %(x,y,bet)
						m = m + bet
					elif sum == 7 or sum < 7:
						print "The dice shows %s and %s. Sorry, you lose $%s." %(x,y, bet)
						m = m - bet
				elif ans == "3":
					if sum == 7:
						print "The dice shows %s and %s. Congratulations. You win $%s!" %(x,y,4 * bet)
						m = m + (4 * bet)
					elif sum != 7:
						print "The dice shows %s and %s. Sorry, you lose $%s." %(x,y,4 * bet)
						m = m - (4 * bet)
				elif ans == "4":
					z = 1
					print "You walk away with $%s. Thanks for playing." %(m)
				else:
					print "Please enter 1/2/3. Try again."
			else:
				print "Please enter a valid bet within $%s." %(m)
		else:
			print "Please enter a valid amount."
