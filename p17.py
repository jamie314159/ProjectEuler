lc = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
	  10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 
	  20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",
	  100:"hundred", 1000:"thousand"}

def getLetterCount(z):
	c = ""
	x = str(z)[::-1]
	if((len(x) == 2) & (z in lc)):
		c += lc[z]
	elif(z==1000):
		c += lc[int(x[3])] + lc[z]
	else:
		for i in range(len(x)-1,-1,-1):
			if(i==0):
				c += lc[int(x[i])]
			if(i==1):
				if(int(x[1]+x[0]) in lc):
					c += lc[int(x[1]+x[0])]
					break
				c += lc[int(x[i])*10]
			if(i==2):
				c += lc[int(x[i])] + lc[100]
				if(z%100 > 0):
					c += "and"
	if(c):
		print(z, c)
	return c

n = ""
for i in range(1,1001):
	n += getLetterCount(i)
print(n)
print(len(n))
