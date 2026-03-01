def fk(cb):
    total = 0
    for sb in range(0, 3, 1):
        total = total + cb[sb]
    cb[2] = total
    print(id(cb))
    return cb

ca = [10, 20, 30]

print(ca)
cd = fk(ca)     # cd = cb
print(ca)
print(cd)

print(id(ca))
print(id(cd))
