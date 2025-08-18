def hannoi(n,p1,p2,p3):
    if n == 1:
        print(f"Mover disco 1 da pilha {p1} para a pilha {p3}")
    elif n >= 2:
        hannoi(n-1,p1,p3,p2)
        print(f"Mover disco {n} da pilha {p1} para a pilha {p3}")
        hannoi(n-1,p2,p1,p3)
    return "poggers"

n= int(input())

hannoi(n,"1","2","3")