from numpy import *

def lglnodes(M):
  """
  ======================================================================
  -
  - lglnodes.py -- Modified from lglnodes.m  (see matlabcentral)
  -
  - Computes the Legendre-Gauss-Lobatto nodes, weights and the LGL
  - Vandermonde matrix. The LGL nodes are the zeros of (1-x^2)*P'_N(x).
  - Useful for numerical integration and spectral methods. 
  -
  - Reference on LGL nodes and weights: 
  -   C. Canuto, M. Y. Hussaini, A. Quarteroni, T. A. Tang, 
  -   "Spectral Methods in Fluid Dynamics," Section 2.3. 
  -    Springer-Verlag 1987
  -
  - Written by Greg von Winckel - 04/17/2004
  - Contact: gregvw@chtm.unm.edu
  - Translated to Python3 by Jason Yalim - 2016/03/29
  - Contact: jyalim@asu.edu
  -
  ======================================================================
  """
  # Truncation + 1
  N = M+1

  # Use the sorted Chebyshev-Gauss-Lobatto nodes as the first guess
  x = -cos(pi*arange(N)/M) 

  # Initializing the Legendre Vandermonde Matrix (And P_0)
  P = ones((N,N))
  # Compute P_(M) using the recursion relation and update x using the
  # Newton-Raphson method.

  xold, machine_epsilon = 2, finfo(float).eps
  while max(abs(x-xold)) > machine_epsilon:
    xold = x.copy()
    P[1] = x.copy()
    for k in range(2,N):
      P[k] = ( (2*k-1)*x*P[k-1]-(k-1)*P[k-2] ) / k
    x = xold - ( x*P[-1]-P[-2] ) / ( N*P[-1] )

  w = 2 / (M*N*P[-1]**2);
  return x,w,P
