lines = ['10', '4 2', '1 2', '5 10', '10 10', '6 3', '9 2', '4 8', '5 5', '4 7', '2 10']
n = 0
carteA = 0
carteB = 0
scoreA = 0
scoreB = 0

for loop in range(int(lines[n])):
    n +=1
    
    if lines[n][:2] == '10':
        carteA = int(lines[n][:2])
        if lines[n][-2:] == '10':
            carteB = int(lines[n][-2:])
        else:
            carteB = int(lines[n][3])
    else:
        carteA = int(lines[n][0])
        if lines[n][-2:] == '10':
            carteB = int(lines[n][-2:])
        else:
            carteB = int(lines[n][2])
            
    if carteA > carteB:
        scoreA +=1
    elif carteA < carteB:
        scoreB +=1
        
if scoreA > scoreB:
    print('A')
else:
    print('B')
