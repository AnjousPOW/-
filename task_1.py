a = float(input())
b = float(input())
c = float(input())
if a < c + b and b < a + c and c < a + b:
    print("YES")
else:
    print("NO")
