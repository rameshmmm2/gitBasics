n = int(input())
for i in range(2, n):
    n *= i
cnt = 0
while n:
    if n % 10 == 0:
        cnt += 1
    else:
        break
    n //= 10
print(cnt)