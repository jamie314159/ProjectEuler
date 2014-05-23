prime = [2]
abundent = set([])
abundentSum = set([])
numSet = set([])

def isPrime(n):
	for i in range(2, int(pow(n, .5))+1):
		if(n%i==0):
			return 0
	return 1

def getNextPrime():
	x = prime[len(prime)-1]
	x += 1
	while(not isPrime(x)):
		x += 1
	prime.append(x)

def getPrimeFactors(n):
	i = 0
	j = prime[i]
	primeFactors = {}
	while(n > 1):
		if(n%j==0):
			if(j not in primeFactors):
				primeFactors[j] = 0
			primeFactors[j] += 1
			n /= j
		else:
			i += 1
			if(i >= len(prime)):
				getNextPrime()			
			j = prime[i]
	return(primeFactors)


def getFactors(n):
	primeFactors = getPrimeFactors(n)
	primePowers = set([pow(a,b) for a in primeFactors for b in range(0, primeFactors[a]+1)])
	factors = primePowers.copy()
	temp = factors.copy()
	l = 1
	for d in primeFactors.values():
		l *= (d+1)
	l -= 1
	while(len(factors) < l):
		[factors.add(a*b) for a in primePowers for b in temp if((n%(a*b)==0)&(a*b < n))]
		temp = factors.copy()
	if n in factors:
		factors.remove(n)
	return factors

def getFactorSum(n):
	f = getFactors(n)
	s = 0
	for a in f:
		s += a
	return s

def isAbundent(n):
	if(getFactorSum(n) > n):
		return 1
	return 0




for n in range(1, 28123):
	if(isAbundent(n)):
		abundent.add(n)

t = 0
n = 0

[abundentSum.add(a+b) for a in abundent for b in abundent]
[numSet.add(a) for a in range(0, 28124) if(a not in abundentSum)]

print(len(abundentSum), max(abundentSum))
print(len(numSet), max(numSet))

# print(numSet)
for i in numSet:
	t += i
print(t)