#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mandelbrot example with light shading
# after
# https://matplotlib.org/stable/gallery/showcase/mandelbrot.html
#sphx-glr-gallery-showcase-mandelbrot-py

import time
import numpy as np
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt

# mandelbrot set function: returns matrices with convergent areas and
# number of iterations until convergence
# takes x/y axis dimensions and steps, maximum iteration and converg. horizon
def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    # get evenly spaced vectors for X and Y
    X = np.linspace(xmin, xmax, xn).astype(np.float32)
    Y = np.linspace(ymin, ymax, yn).astype(np.float32)
    # make complex plane with given area and "resolution"
    # [:, None] is equivalent to making a new dimension for Y
    # in effect transposing it from a row vector to a column vector
    # mult new Ys with python's complex number j gives, along with X, the
    # desired complex plane C
    C = X + Y[:, None] * 1j
    # make new Matrices just like C, initialize them with all Zeroes
    # N integer Matrix, Z floating point
    N = np.zeros_like(C, dtype=int)
    Z = np.zeros_like(C)

    for n in range(maxiter):
        I = abs(Z) < horizon
        N[I] = n
        Z[I] = Z[I]**2 + C[I]

    N[N == maxiter - 1] = 0
    return Z, N

def main():
    xmin, xmax, xn = -2.25, +0.75, 3000 // 2
    ymin, ymax, yn = -1.25, +1.25, 2500 // 2
    maxiter = 200
    horizon = 2.0 ** 40
    log_horizon = np.log2(np.log(horizon))
    Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)

    with np.errstate(invalid='ignore'):
        M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)

    dpi = 72
    width = 10
    height = 10 * yn / xn
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)

    light = colors.LightSource(azdeg=315, altdeg=10)
    M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5,\
                    norm=colors.PowerNorm(0.3), blend_mode='hsv')
    ax.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
    ax.set_xticks([])
    ax.set_yticks([])

    year = time.strftime("%Y")
    text = "Mandelbrot set\nrendered with matplotlib after example"
    ax.text(xmin + .025, ymin + .025, text, color="white", fontsize=12,\
            alpha=0.5)
    plt.show()

# let main run
if __name__ == '__main__':
    main()
