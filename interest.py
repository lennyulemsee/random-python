a = float(input("please enter your investment: "))
b = float(input("please enter your interest ratea: "))

b = b / 100
for i in range(10):
    a = a + (a * b)
    
