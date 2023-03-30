import sys
# cook your dish here
def easy_pronunciation(n, s):
    if n<=3:
        print("YES")
    else:
        for i in range(n-3):
            string = s[i:i+4]
            vow1 = 'a' in string or 'e' in string or 'i' in string 
            vow2 = 'o' in string or 'u' in string 
            if not vow1 and not vow2:
                print("NO")
        else:
            print("YES")
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    easy_pronunciation(n, s)
