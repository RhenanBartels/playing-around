# _*_ coding: utf-8 _*_

def regFal(fx, xl, xr, Epsilon=10e-4):
    fl = fx(xl)
    fr = fx(xr)
    if fl * fr > 0:
        raise Exception("xl and xr are not bracketing the solution")
    if not hasattr(fx, '__call__'):
        raise Exception("fx must be a function")
    nx = xl - fl * (xr - xl) / (fr - fl)
    while abs(nx - xl) > Epsilon:
        nf = fx(nx)
        if fl * nf < 0:
            xr = nx
        else:
            xl = nx
        nx = xl - fl * (xr - xl) / (fr - fl)
    return nx
