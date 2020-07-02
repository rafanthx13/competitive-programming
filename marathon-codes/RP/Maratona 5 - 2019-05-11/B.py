OUT = []

while True:
    try:
        ip = int(input().split('/')[1])
        total = pow(2, 32-ip)
        OUT.append(str(total) + ' IPs.')

    except EOFError:
        break


for i in OUT:
    print(i)