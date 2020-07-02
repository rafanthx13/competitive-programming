# 1198

count = 0
results = []
while True:
	try:
		list = input().split()
		a = list[0]
		b = list[1]
		results.append(abs(int(a) - int(b)))
		count+=1
	except EOFError:
		break

for i in results:
	print(i)
