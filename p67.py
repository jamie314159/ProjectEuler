def getT():
	# f = open('triangle.txt', 'r')
	# a = f.read().split('\n')

	# for i in range(0, len(a)):
	# 	a[i] = a[i].split(' ')


	# a = [[int(x) for x in y] for y in a]
	# b = [list(map(int, y)) for y in a]
	# print(b==a)

	return [[int(x) for x in y] for y in [y.split(' ') for y in (open('triangle.txt', 'r').read().split('\n'))]]

def maxNext(y,x):
	return max(t[y+1][x], t[y+1][x+1])

t = getT()

for y in range(len(t)-2, -1, -1):
	for x in range(0, len(t[y])):
		t[y][x] += maxNext(y,x)

print(t[0][0])