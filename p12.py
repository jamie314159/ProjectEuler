import math

def getSum(x):
	return int(.5*x*(x+1))

def isPrime(n):
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return 0
	return 1

def nextPrime(x):
	if(x == 1):
		return 2
	x += 1
	while(isPrime(x) == 0):
		x += 1
	return x
	

def getPrimeDivisors(x):
	p = 2
	ps = {}
	s = x
	d = 0
	while(isPrime(s) == 0):
		# print(s,p)
		if (s % p == 0):
			s = int(s / p)
			if p in ps:
				ps[p] += 1
			else:
				ps[p] = 1
			# print(s, p)
		else:
			p = nextPrime(p)
	if s in ps:
		ps[s] += 1
	else:
		ps[s] = 1
	return ps

def getDivisors(x):
	d = 1
	ps = getPrimeDivisors(x)
	# print(ps)
	# print(range(len(ps)))
	for i in ps:
		# print(ps[i])
		d = d*(ps[i]+1)
	return d



# print(getDivisors(839160))
# def getDivisorsa(x):
# 	d = 0
# 	s = x#getSum(x);
# 	t = 1
# 	a = 2
	
# 	while(s%a > 0):
# 		a += 1
# 	f = int(s/a)+1
# 	for i in range(1,f):
# 		if (s%i == 0):
# 			d+=1
# 	return d+1


# print(isPrime(nextPrime(3)))
# print(getPrimeDivisors(100))
# print(getDivisors(2016))
# for i in range(2,100):
# 	print(i, getSum(i), getPrimeDivisors(getSum(i)))
i = 2079
ld = 0
ln = 0
while(1):
	s = getSum(i)
	d = getDivisors(s)
	if(d > ld):
		ld = d
		ln = i
		ls = s
		print(ln, ls, ld)	
	if(d>500):
		print(i)
		break
	else:
		# print(i)
		# print(ln, getSum(ln), l)	
		i+=1
	# if(getDivisors(i)==3):
	# 	print(i, getSum(i), getDivisors(i))


























# s = 0
# def getSum(x):
# 	return int(.5*x*(x+1))

# def getDivisorsa(x):
# 	d = 0
# 	s = getSum(x);
# 	t = 1
# 	a = 2
	
# 	while(s%a > 0):
# 		a += 1
# 	f = int(s/a)+1
# 	for i in range(1,f):
# 		if (s%i == 0):
# 			d+=1
# 	return d+1

# print(getDivisorsa(15))
# def getDivisors(x):



# #2079
# #3000
# i = 2
# l = 0
# ln = 0
# #print(sum(range(0,8)))
# #print(getSum(8))
# # print(8, getSum(8), getDivisors(8))

# while(1):
# 	d = getDivisors(i)
# 	if(d > l):
# 		l = d
# 		ln = i
# 		#print(ln, getSum(ln), l)	
# 	if(d>500):
# 		print(i)
# 		break
# 	else:
# 		# print(i)
# 		# print(ln, getSum(ln), l)	
# 		i+=1
# 	if(getDivisors(i)==3):
# 		print(i, getSum(i), getDivisors(i))
