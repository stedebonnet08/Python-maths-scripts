#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn).astype(np.float32)
    Y = np.linspace(ymin, ymax, yn).astype(np.float32)
    C = X + Y[:, None] * 1j
    N = np.zeros_like(C, dtype=int)
    Z = np.zeros_like(C)

    for n in range(maxiter):
        I = abs(Z) < horizon
        N[I] = n
        Z[I] = Z[I]**2 + C[I]

    N[N == maxiter - 1] = 0

    print("X: ",X)
    print("Y: ",Y)
    print("C: ",C)

    print("N: ",N)
    print("Z: ",Z)

    return Z, N

def main():
    xmin, xmax, xn = -2.25, +0.75, 20 // 2
    ymin, ymax, yn = -1.25, +1.25, 20 // 2
    maxiter = 200
    horizon = 2.0 ** 40
    log_horizon = np. log2(np.log(horizon))
    Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)

    return 0

# let main run
if __name__ == '__main__':
    main()
