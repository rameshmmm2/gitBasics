a = input()

s = ""
letter = a[0]
start = 0
l = len(a)

for i in range(1, l):
    if a[i] != a[i-1]:
        s += letter + str(i-start)
        letter = a[i]
        start = i

print(s + letter + str(l-start))