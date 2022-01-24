def bissection(f,a,b,N):

    if f(a)*f(b) >= 0:
        print("La méthode de la bissection ne peut pas être appliquée dans ce cas là.")
        return None
    
    a_n = a
    b_n = b
    for n in range(1 , N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        
        elif f_m_n == 0:
            print("La solution exacte à été trouvé.")
            return m_n
        
        else:
            print("La méthode de la bissection n'a pas abouti")
            return None
    
    return (a_n + b_n)/2

f = lambda x: x**2 - x - 1
a = -1
b = 1
N = 1000

a = bissection(f, a, b, N)
print(a)
