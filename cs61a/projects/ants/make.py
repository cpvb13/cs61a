def make_dig(n):
    sum, d = 0,n
    def next():
        nonlocal sum,d
        if d==0:
            return sum+d
        d,last = d//10,d%10
        sum += last
        return last
    return next
    
get = make_dig(8102)

for _ in range(4):
    print(get())

get()