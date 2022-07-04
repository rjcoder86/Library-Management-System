n=6
for i in range(1, n + 1):
    C = 1
    for j in range(1, i + 1):
        # first value in a line is always 1
        print(C, end=' ')

        # using Binomial Coefficient
        C = C * (i - j) // j

    print()


n=11

x=set(0 for i in range(2,n) if n%i==0)
print('not') if x else print('prime')

l=[0,1]
for i in range(10):
    l.append(l[i]+l[i+1])
print(l)
