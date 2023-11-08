
# 3-masala

n = int(input())
n_banknota = list(map(int, input().split()))
mijoz = int(input())
qarz = list(map(int, input().split()))

res = []

summma = sum(n_banknota)
max_bank = max(n_banknota)

for i in qarz:
    if i in n_banknota:
        res.append(1)
    
    elif summma - i in n_banknota:
        res.append(n-1)
    elif i == summma:
        res.append(n)
    elif i > summma:
        res.append(-1)
    elif i > max_bank:
        for j in n_banknota:
            if i-j in n_banknota:
                res.append(2)
                break
    
        
    # elif i not in n_banknota or summma - i not in n_banknota or i != summma or i<max_bank:
    #     res.append(-1)
    else :
        res.append(-1)
    
    
      
        
for j in res:
    print(j, end=' ')

