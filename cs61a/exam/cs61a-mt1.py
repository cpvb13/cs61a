def rect(area, perimeter):
    side = 1

    while side * side <= area:


        other = round(perimeter/2-side)


        if side*other==area:


            return max(side,other)


        side = side + 1


    return False

print(rect(100,50))


def sequence(n, term):
    t, k = 0, 1


    while k<n:


        m = 1


        x = term(k)


        while m <= x:


            m =10*m


        t = (t*m)+x


        k = k + 1


    return t

   

print(sequence(6,abs))


def repeat(k):
    return detector(k)


def detector(f):

    def g(i):


        if k==f:


            print(k)


        return repeat(i)


    return g

repeat(1)(7)(1)

def repeat_digits(n):
    f = repeat(n%10)

    while n:

        f, n = f((n//10)%10) , n//10
print(repeat_digits(23456111))