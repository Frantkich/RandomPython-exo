lines = ['13', 'chaise', 'ssd 23', 'ssd 38', 'tv 8', 'chaise 49', 'chaise 37', 'ssd 67', 'ssd 98', 'chaise 55', 'chaise 32', 'chaise 99', 'tv 65', 'chaise 14', 'ssd 93']
n = 1
article = lines[1]
P = 100
for loop in range(int(lines[0])):
    n += 1
    if lines[n][:len(article)] == article:
        if int(lines[n][-2:]) < P:
            P = int(lines[n][-2:])

print(P)
        
