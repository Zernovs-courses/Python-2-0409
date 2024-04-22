def sum_func():

    global a

    a = 100
    b = a * 10

    def nested():

        nonlocal b

        b = b + 10
    
        
        z = b / 5 * a
        
        return z
    
    print(f"b={b}")
    
    return nested()

a = 10

print(sum_func(), a)