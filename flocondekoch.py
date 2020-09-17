from turtle import *
reset()
def flocondekoch(l,n):

    if n<=0:
        forward(l)
    elif n >=4:
        flocondekoch(l/2,n-1)
        left(60)
        flocondekoch(l/2,n-1)
        right(120)
        flocondekoch(l/2,n-1)
        left(60)
        flocondekoch(l/2,n-1)
    else:
        flocondekoch(l/3,n-1)
        left(60)
        flocondekoch(l/3,n-1)
        right(120)
        flocondekoch(l/3,n-1)
        left(60)
        flocondekoch(l/3,n-1)

def paterne(l,n):
                    
    flocondekoch(l,n)
    right(120)
    flocondekoch(l,n)
    right(120)
    flocondekoch(l,n)


etape=int(input("Etape : "))
taille=float(input("Taille : "))
paterne(taille,etape)