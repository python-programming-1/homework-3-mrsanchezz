import sys

def collatz():
	validInput = False
	while not validInput:
		try:
			num = int(input('Please enter a number: '))
		except ValueError:
			print('Oops! That was no valid number. Try again...')
		else:
			validInput = True
			while True:
				if (num % 2) == 0:
					num = num // 2 
				else:
					num = 3 * num + 1

				print(num, end='\n')
				validInput = True
				if num != 1:
					continue
				if num == 1:
					return num

collatz()