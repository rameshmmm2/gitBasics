n = int(input())
if n == 1:
    print(1)
    exit()
else:
    a = [1]
    spaces = n-2
    
    # Initial
    print(' '*(spaces+1) + '1')
    
    # 
    for i in range(2, n+1):
        b = [1 for _ in range(i)]
        for i in range(1, i-1):
            b[i] = a[i] + a[i-1]
        s =  ' ' * spaces + ' '.join([str(i) for i in b])
        print(s)
        spaces -= 1
        a = b