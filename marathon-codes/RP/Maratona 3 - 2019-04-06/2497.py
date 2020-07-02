#I - 2497

cicle = [];

while True:
    num = int(input());

    if (num == -1):
        break;

    result = num//2
    cicle.append(result);

for x in range(0, len(cicle)):
    print('Experiment ' + str(x+1) + ': ' + str(cicle[x]) + ' full cycle(s)');
