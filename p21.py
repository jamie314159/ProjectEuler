am = {}
def d(n):
	r = 0
	for i in range(1, n):
		if(n%i == 0):
			r += i
	return r

def amicable(a):
	if(a not in am.values()):
		da = d(a)
		dda = d(da)
		if(da != a)&(dda == a):
			am[len(am)] = a
			am[len(am)] = da


s = 0
for i in range(0, 10001):
	amicable(i)

for j in am:
	s += am[j]
print(s)