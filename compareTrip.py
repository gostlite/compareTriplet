def compareTriplet(a:list, b:list)->int:
    if len(a) >=1 and len(b) >=1:
        alice =0
        bob =0
        for x,y in zip(a,b):
            if x > y:
                alice+=1
            elif y >x:
                bob+=1
        return alice,bob

a = [17,28,30]
b=[99,16,8]
print(compareTriplet(a,b))