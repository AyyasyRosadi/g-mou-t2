barang = [20,10,20,30,40,50,60]
A = barang[0]
B = barang[0]
C = barang[0]
sisa = 0
for i in range(1,len(barang)):
    if A >= B and A >= C:
        if A >= barang[i]:
            A -= barang[i]
        else:
            sisa+=1
    elif B >= A and B >= C:
        if B >= barang[i]:
            B -= barang[i]
        else:
            sisa+=1
    elif C >= A and C >= B:
        if C >= barang[i]:
            C -= barang[i]
        else:
            sisa+=1
    elif b > A and b > B and b > C:
        sisa += 1
print(sisa)

