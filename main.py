def comp(array1, array2):    

    tmp=array1
    for i in tmp:
        print(i)
        array1.remove(i)
        
    print(array1)
    return True

    

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

print(comp(a1, a2))