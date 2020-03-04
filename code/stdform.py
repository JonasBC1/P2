#Metode til invers matrix. Mellem bevis 3.16 og eks 3.19.
obj = "4*x1+6*x2+x3"
bet = [
	"12*x1-x2<=15",
	"3*x2+2*x3<=10"]
neg = [
	"x1>=0",
	"x2>=0",
	"x3>=0"]

def findx(l):
	xi	= True
	xii	= True
	i 	= 0

	while xi == True:
		xi = "x" + str(i+1)

		for st in l:
			if xi in st:
				xi = True
				
			else:
				xi = False

		i += 1

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

findx(bet)