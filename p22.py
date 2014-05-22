def score(n):
	s = 0
	for i in n:
		s += ord(i)-64
	return s



f = open('names.txt', 'r')
s = f.read().split(',')
for i in range(0,len(s)):
	s[i] = s[i][1:len(s[i])-1]

t = 0
s = sorted(s)
for j in range(0,len(s)):
	t += (j+1)*score(s[j])
print(t)