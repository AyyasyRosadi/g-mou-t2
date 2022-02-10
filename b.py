energi = [1,1,4,'5T']
x = []
energi_min = 0
for i in range(3,len(energi)):
    x.append(energi[i])
for j in x:
    y = ''
    z = ''
    for k in range(len(j)):
        if j[k] == 'D' or j[k] == 'N' or j[k] == 'T':
            y += j[k]
        else:
            z += j[k]
    if y == 'D' :
        energi_min += energi[0]*int(z)
    elif y == 'N':
        energi_min += energi[1]*int(z)
print(energi_min)
