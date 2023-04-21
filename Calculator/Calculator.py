def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def percentage(a,b):
    return (a / b)*100


a = float(input('input first number'))
b = float(input('input second number'))


option = int(input( '''

1.Add
2.Subtract               
3.Multiply
4.Divide
5.Percentage
5.Exit
'''))

while(option != 6):
    if(option==1):
        print(plus(a,b))
        a = float(input('input first number'))
        b = float(input('input second number'))


        option = int(input( '''

        1.Add
        2.Subtract               
        3.Multiply
        4.Divide
        5.Percentage
        5.Exit
        '''))
    elif(option==2):
        print(minus(a,b))
        a = float(input('input first number'))
        b = float(input('input second number'))


        option = int(input( '''

        1.Add
        2.Subtract               
        3.Multiply
        4.Divide
        5.Percentage
        5.Exit
        '''))
    elif(option==3):
        print(multiply(a,b))
        a = float(input('input first number'))
        b = float(input('input second number'))


        option = int(input( '''

        1.Add
        2.Subtract               
        3.Multiply
        4.Divide
        5.Percentage
        5.Exit
        '''))
    elif(option==4):
        print(divide(a,b))
        a = float(input('input first number'))
        b = float(input('input second number'))


        option = int(input( '''

        1.Add
        2.Subtract               
        3.Multiply
        4.Divide
        5.Percentage
        5.Exit
        '''))
    elif(option ==5):
        print(percentage(a))
        a = float(input('input first number'))
        b = float(input('input second number'))


        option = int(input( '''

        1.Add
        2.Subtract               
        3.Multiply
        4.Divide
        5.Percentage
        5.Exit
        '''))
