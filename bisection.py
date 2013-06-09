# _*_ coding: utf-8


def bisMethod(fx, xl, xr, Epsilon=10e-4):

    fl = fx(xl)
    fr = fx(xr)
    if fl * fr > 0:
        raise Exception('xl and xr are not bracketing the solution')

    if not hasattr(fx, '__call__'):
        raise Exception('fx must be a function')

    nx = (xl + xr) / 2.
    while abs(nx - xl) > Epsilon:
        nf = fx(nx)
        if fl * nf < 0:
            xr = nx
        else:
            xl = nx
        nx = (xl + xr) / 2
    return nx
