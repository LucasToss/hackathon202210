""" 
#### factorial function example ### 
 fact n 
 n integer number
 commande_type fact
 args : n , positive integer 
 in  case of of negative return 0
"""

def factorielle(v):
    
    if v < 0:
        return 'undefined'
    if v < 2:
        return 1
    total = 1
    for curValeur in range (2,v+1):
      total = total*curValeur
    return total

def cmd_fact(n):
    return str(factorielle(n))
