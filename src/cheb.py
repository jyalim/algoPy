def cheb(N):
  D,x = 0.,1.
  if N==0:
    return D,x
  x = cos(pi*arange(N+1)/N).reshape(-1,1)
  c = (array([ 2, *ones(N-1), 2 ]) * (-1)**(arange(N+1))).reshape(-1,1)
  dx= x - x.T
  D = (c @ ( 1/c.T )) / (dx + eye(N+1))
  D-= diag(sum(D,1))
  return D,x
