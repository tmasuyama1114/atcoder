k = int(input())
a, b = input().split()

def base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out

a = base_n_to_10(a, k)
b = base_n_to_10(b, k)

print(a*b)