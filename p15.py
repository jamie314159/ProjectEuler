paths = 0
n = 2
f = 3
m = 3
o = 3

for s in range(2,21):
	n = round(n*f)
	f = f +(1/m)
	m += o
	o += 1
	print(s, n)
