def fibnacci(Positie):
    prev = 1
    curent = 1
    for i in range(Positie):
        next = prev + curent

        prev = curent
        curent = next
    return next 
print(fibnacci(11))