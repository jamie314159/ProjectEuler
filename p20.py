f = 1
for x in range(1,101):
	f = f*x
f = str(f)
s = 0
for i in f:
	s += int(i)
print(s)