def f1(a):
    print(a+x)      #Variável Local
def f2(a):
    c = 10
    print(a+x+c)    #Variável Local

x = 4               #Variável Global
f1(3)
f2(3)
print(x)