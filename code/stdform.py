obj = "4*x1+6*x2+x3"
bet = [
	"12*x1-x2<=15",
	"3*x2+2*x3<=10"]
neg = [
	"x1>=0",
	"x2>=0",
	"x3>=0"]

def findx(st):
	xi	= True
	i 	= 0

	while xi == True:
		xi = "x" + str(i+1)

		if xi in st:
			xi = True
			i += 1
		else:
			xi = False


	print(i)

#def split(f=bet):
#	split = []

#	while 

#	for i in range(len(f)):
#		if "<=" in f[i]:
#			split.append(f[i].split("<="))
#			split[-1][-1] = float(split[-1][-1])

#		else:
#			split.append(f[i].split(">="))

#	print(split)

#def stdform(f=obj, bet=bet):
	
#split()

findx(bet[0])
findx(bet[1])