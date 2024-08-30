
szamok = [6,9,8,1,3,2,5,4,10,7]
print("alap tomb, egyszeru cseres rendezes megvalositasa: ")
print(' '.join(map(str, szamok)))

for i in range(len(szamok)-1):
    for j in range(i+1,len(szamok)):
        
        if szamok[i] > szamok[j]:
            seged = szamok[j]
            szamok[j] = szamok[i]
            szamok[i] = seged
            print("Csere tortent")
            print(' '.join(map(str, szamok)))
            

print("vegso allapo: Egyszeru cseres")
print(' '.join(map(str, szamok)))
#buborek rendezes
szamok = [6,9,8,1,3,2,5,4,10,7]
print("alap tomb, Buborekrendezes megvalositasa: ")
print(' '.join(map(str, szamok)))


for i in range(len(szamok),1,-1):  
    for j in range(0,i-1):
        if szamok[j] > szamok[j+1]:
            seged = szamok[j]
            szamok[j] = szamok[j+1]
            szamok[j+1] = seged
            print("Csere tortent")
            print(' '.join(map(str, szamok)))

print("vegso allapo: Buborek")
print(' '.join(map(str, szamok)))