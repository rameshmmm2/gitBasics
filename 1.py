string = input()
s = ""
for i in range(0, len(string), 2):
    s += (string[i] * int(string[i+1]))
print(s)