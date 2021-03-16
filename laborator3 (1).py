import math as mat


def combinari(n, k):
    return mat.factorial(n) / (mat.factorial(k) * mat.factorial(n - k))


def B(n, k, t):
    return combinari(n, k) * mat.pow(t, k) * mat.pow(1 - t, n - k)


def B_derivat(n, k, t):
    c = combinari(n, k)
    if k > 0:
        c1 = k * mat.pow(t, k - 1)
    else:
        c1 = 1
    c2 = mat.pow(1 - t, n - k - 1)
    return c * c1 * c2


def puncte_de_control(n):
    a = []

    for index in range(n + 1):
        print("puntcul ", index)
        x = float(input("x = "))
        y = float(input("y = "))
        a.append((x, y))

    return a


def punct_k(lista, k):
    return lista[k - 1]


def curba_bezier(n, t, puncte):
    curba_x = 0
    curba_y = 0

    for k in range(n):
        p = punct_k(puncte, k)
        curba_x += B(n, k, t) * p[0]
        curba_y += B(n, k, t) * p[1]

    return curba_x, curba_y


def curba_derivata(n, t, puncte):
    curba_derivata_x = 0
    curba_derivata_y = 0

    for k in range(n):
        p = punct_k(puncte, k)
        curba_derivata_x += B_derivat(n, k, t) * p[0]
        curba_derivata_y += B_derivat(n, k, t) * p[1]

    return curba_derivata_x, curba_derivata_y


def main():
    n = int(input("Gradul curbei Bezier : "))
    puncte = puncte_de_control(n)
    t = float(input("Da-ti un t de la 0 la 1 : "))
    r = curba_bezier(n, t, puncte)
    print("r(", t, ") = ", r)
    r_d = curba_derivata(n, t, puncte)
    print("r'(", t, ") = ", r_d)




main()