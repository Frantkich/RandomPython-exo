#résultat -> 26
#
#
lines = ['7', '...X...', '..X..XX', 'X......', '.......', 'X.X....', 'X......', '.......']
y = 0
lgList = int(lines[y])
Score = 0

for loop in range(lgList):
    y += 1
    for x in range(lgList):
        if lines[y][x]== 'X':
            
            StrLines2 = list(lines[y])            
            if x == 0:
                if lines[y][x+1] == '.':
                    StrLines2[x+1] = 'O'    
            elif x == lgList-1:
                if lines[y][x-1] == '.':
                    StrLines2[x-1] = 'O'
            else:
                if lines[y][x+1] == '.':
                    StrLines2[x+1] = 'O'
                if lines[y][x-1] == '.':
                    StrLines2[x-1] = 'O'
            lines[y] = "".join(StrLines2)

            
            if y == 1:
                StrLines3 = list(lines[y+1])
                if x == 0:
                    if lines[y+1][x] == '.':
                        StrLines3[x] = 'O'
                    if lines[y+1][x+1] == '.':
                        StrLines3[x+1] = 'O'
                elif x == lgList-1:
                    if lines[y+1][x-1] == '.':
                        StrLines3[x-1] = 'O'
                    if lines[y+1][x] == '.':
                        StrLines3[x] = 'O'
                else:
                    if lines[y+1][x-1] == '.':
                        StrLines3[x-1] = 'O'
                    if lines[y+1][x] == '.':
                        StrLines3[x] = 'O'
                    if lines[y+1][x+1] == '.':
                        StrLines3[x+1] = 'O'
                lines[y+1] = "".join(StrLines3)
            
            
            elif y == lgList:
                StrLines1 = list(lines[y-1])
                if x == 0:
                    if lines[y-1][x] == '.':
                        StrLines1[x] = 'O'
                    if lines[y-1][x+1] == '.':
                        StrLines1[x+1] = 'O'
                if x == lgList-1:
                    if lines[y-1][x-1] == '.':
                        StrLines1[x-1] = 'O'
                    if lines[y-1][x] == '.':
                        StrLines1[x] = 'O'
                else:
                    if lines[y-1][x-1] == '.':
                        StrLines1[x-1] = 'O'
                    if lines[y-1][x] == '.':
                        StrLines1[x] = 'O'
                    if lines[y-1][x+1] == '.':
                        StrLines1[x+1] = 'O'
                lines[y-1] = "".join(StrLines1)
            

            else:
                StrLines3 = list(lines[y+1])
                if x == 0:
                    if lines[y+1][x] == '.':
                        StrLines3[x] = 'O'
                    if lines[y+1][x+1] == '.':
                        StrLines3[x+1] = 'O'
                elif x == lgList-1:
                    if lines[y+1][x-1] == '.':
                        StrLines3[x-1] = 'O'
                    if lines[y+1][x] == '.':
                        StrLines3[x] = 'O'
                else:
                    if lines[y+1][x+1] == '.':
                        StrLines3[x+1] = 'O'
                    if lines[y+1][x] == '.':
                        StrLines3[x] = 'O'
                    if lines[y+1][x-1] == '.':
                        StrLines3[x-1] = 'O'
                lines[y+1] = "".join(StrLines3)
                
                StrLines1 = list(lines[y-1])
                if x == 0:
                    if lines[y-1][x] == '.':
                        StrLines1[x] = 'O'
                    if lines[y-1][x+1] == '.':
                        StrLines1[x+1] = 'O'  
                elif x == lgList-1:
                    if lines[y-1][x-1] == '.':
                        StrLines1[x-1] = 'O'
                    if lines[y-1][x] == '.':
                        StrLines1[x] = 'O'
                else:
                    if lines[y-1][x+1] == '.':
                        StrLines1[x+1] = 'O'
                    if lines[y-1][x] == '.':
                        StrLines1[x] = 'O'
                    if lines[y-1][x-1] == '.':
                        StrLines1[x-1] = 'O'
                lines[y-1] = "".join(StrLines1)
n = 0
for loop in range(lgList):
    n += 1
    Score += lines[n].count('O')
        
print(Score)

n = 0
for loop in range(lgList):
    n += 1
    print(lines[n])
