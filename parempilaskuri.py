x = input("Enter an expression:")
result = [0,1,0,1]

if "+" in x:
    expression = x.split("+")
    for i in range(len(expression)):
        result[0] += float(expression[i])
    print(result[0])

if "*" in x:
    expression = x.split("*")
    for i in range(len(expression)):
        result[1] *= float(expression[i])
    print(result[1]) 

if "-" in x:
    expression = x.split("-")
    for i in range(len(expression)):
        if i==0:
            result[2] = float(expression[i])
        else:
            result[2] -= float(expression[i])
    print(result[2])

if "/" in x:
    expression = x.split("/")
    for i in range(len(expression)):
        if i==0:
            result[3] = float(expression[i])
        else:
            result[3] /= float(expression[i])
    print(result[3])
