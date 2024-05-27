import math 

t = [0] * 30
x = [0] * 30
h = 0.01
N = 0

def intrp(T):
    p = 0 
    n = N-1 
    for i in range (n+1):
        L = 1
        for j in range (n+1):
            if i != j:
                L *= (T-t[j]) / (t[i]-t[j])
        p += x[i] * L
    return p

def fact(n):
    if n== 0: 
        return 1
    else : 
        return n*fact(n-1)

def diff (x,h,i,d):
    D = 0 
    for j in range (i+1):
        k = fact(i) // (fact(j) * fact(i-j))
        if d ==1 : 
            r = (-1) ** j
            b = 1
        if d == 2 : 
            r = (-1) ** (j+i)
            b = -1
        D += intrp(x+(b)*(i-j)*h) * r * k
    D = D / h ** i
    return D

def diffc(x):
    return (intrp(x+h)-intrp(x-h)) / (2*h)

def garis (n):
    for i in range (n):
        print("---", end="")
    print()

garis(21)
print()
m = float(input("Masukkan nilai assa benda : "))
print("Masukkan data waktu (t) terhadap perpindahan (x): ")
N = int (input("Masukkan banyanya data : "))
for i in range(N):
    t[i], x[i] = map(float,input("t[{}],x[{}] = ".format (i,i)).split())
t_ = float (input("Masukkan waktu impuls"))
Df = diff(t_,h,1,1)
Db = diff(t_,h,1,2)
Dc = diffc(t_)

garis(30)

print("Besaran\t\tForward\t\t\tBackward\t\tCentral")

garis(30)

print("dx/dt\t\t{}\t{}\t{} ".format(Df,Db,Dc))
pf = m * Dc
pb = m *Db
pc = m * Dc
print("Impuls  \t{}\t{}\t{}".format(pf,pb,pc))
garis(30)