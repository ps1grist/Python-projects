#Never force the humans. Give them three tries to listen and then cancel them.

def num_pls():
	print("Please make sure it's a number.")
	
def success():
	print('Bye now.')

def goodbye():
	print("I don't think you really want to do this.")
	quit()

def CorF(): 
	n = 3
	while n > 0: #three goes at forcing the user to choose either C or F
		corf = input('Please answer using only the letters "C" or "F":')
		if corf == 'C':
			CtoF()
			quit()
		elif corf == 'F':
			FtoC()
			quit()
		n = n - 1
		continue
	goodbye()
	
def CtoF():
	n = 3
	while n > 0: #loop round if it generates an error by not being a numerical input
		try:
			temp = input('Enter temperature in C:')
			newtemp = str(round(int(temp) * 1.8 + 32))
			print('That is ' + newtemp + 'F')
			success()
			return
		except:
			num_pls()
			n = n - 1
			continue
	goodbye()

def FtoC():
	n = 3
	while n > 0: #loop round if it generates an error by not being a numerical input
		try:
			temp = input('Enter temperature in F:')
			newtemp = str(round((int(temp) - 32) / 1.8))
			print('That is ' + newtemp + 'C')
			success()
			return
		except:
			num_pls()
			n = n - 1
			continue
	goodbye()

#temperature conversion
corf = input('Is the temperature you wish to convert in C or F?')

#if they choose neither C or F
if corf != 'C' and corf != 'F':
	CorF()
if corf == 'C': #if they choose C	
	CtoF()
else: #if they choose F
	FtoC()


