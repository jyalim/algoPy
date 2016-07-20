#!/usr/bin/env python
import numpy

__SERIES_EVAL_DEPTH__ = 1000

class SpecFooError(Exception):
  pass

def Clausen(x,order,depth=__SERIES_EVAL_DEPTH__):
  """
    Parameters
    ----------
    x : scalar_like,array_like,matrix_like 
        Evaluation domain (if matrix then number of columns must be
        equal to depth).
    order : scalar_like
        Order of Clausen Function. Complex-valued, but Re{`order`} > 1.
    depth : scalar_like
        Number of series terms to evaluate, must be integer.

    Returns
    -------
    r : array_like     
      r = Cl_{order}(x), `r` will have the same shape as `x`.

    Raises
    ------
    SpecFooError
      If real part of `order` <= 1.

    Notes
    -----
    This is the generalized Clausen function, 
    
      $$S_{z}(x) = \sum_{k=1}^\infty\frac{\sin kx }{k^z}$$,

    where `z` = `order`.

  """
  if numpy.real(order) < 1:
    raise SpecFooError(
      "ERROR: Real part of order must be greater than 1"
    )
  K = numpy.arange(1,depth+1)
  return numpy.sin( numpy.outer(x,K) ) @ ( 1/K**order )

def Clausen2(x,depth=__SERIES_EVAL_DEPTH__):
  return Clausen(x,2,depth=depth)

def Clausen_cos(x,k,depth=__SERIES_EVAL_DEPTH__):
  K = numpy.arange(1,depth+1)
  return numpy.cos( numpy.outer(x,K) ) @ ( 1/K**k )

Clausen(numpy.linspace(0,2*numpy.pi,100),-1)
