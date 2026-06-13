x = 12  #global scope
def fun():
    x = 13 #local scope of the this function
    print(x)
    

    
fun()
print(x) #output is 12 