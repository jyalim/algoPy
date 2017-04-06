import numpy as np

def polyinterp(x,y,u):
  """
   Polynomial interpolation.
      polyinterp(x,y,u) computes v(j) = P(u(j)) where P is the
      polynomial of degree d = length(x)-1 with P(x(i)) = y(i).

      Copyright 2012 Cleve Moler and The MathWorks, Inc.

      Converted to python 2017

   Use Lagrangian representation.
   Evaluate at all elements of u simultaneously.
  """
  n = len(x)
  v = np.zeros(u.shape)
  for k in range(n):
    w = np.ones(u.shape)
    for j in np.r_[np.arange(0,k),np.arange(k+1,n)]:
      w *= (u-x[j])/(x[k]-x[j])
    v += w*y[k]
  return v
