import random

operators=["+","-","*","/"]

mino=3
maxo=12

Total=10

def generate_problem():
    left= random.randint(mino,maxo)
    right=random.randint(mino,maxo)
    operator= random.choice(operators)


    expr= str(left)+ " " + str(operator) + " " + str(right) 
    answer=eval(expr)
    print(expr)
    return answer


print(generate_problem())



#COntinue at 2:21