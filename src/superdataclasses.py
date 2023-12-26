import dataclasses,operator

__BINARY_OPS__ = """
  add 
  sub 
  mul 
  pow 
  matmul 
  truediv 
  floordiv 
  mod 
  lshift 
  rshift 
  and 
  xor 
  or
""".split()

__RICH_COMP_OPS__ = """
  lt
  le
  eq
  ne
  gt
  ge
""".split()

def superdataclass(obj):
  """
  Decorator for basic arithmetic with dataclass objects
  """
  def __getitem__(self,a):
    return getattr(self,a)
  def __setitem__(self,a,v):
    setattr(self,a,v)
  def __binary_op__(self,other,op='__add__'):
    sdict = dataclasses.asdict(self)
    attr  = getattr(operator,op)
    inst  = self.__class__
    if isinstance(other,inst):
      odict = dataclasses.asdict(other)
      value = inst(**{k:attr(v,odict[k]) for k,v in sdict.items()})
    elif isinstance(other,(int,float,complex)):
      value = inst(**{k:attr(v,other) for k,v in sdict.items()})
    return value
  def __len__(self):
    stup = dataclasses.astuple(self)
    return len(stup)
  for attr in [__getitem__, __setitem__, __len__]:
    setattr(obj,attr.__name__,attr)
  for baseop in __BINARY_OPS__:
    for modifier in ['','r','i']:
      op = f'{modifier}{baseop}'
      if modifier != 'i':
        operator_module_op = baseop if baseop != 'or' else f'{baseop}_'
      else:
        operator_module_op = op
      setattr(obj,f'__{op}__',lambda s,o,op=operator_module_op: __binary_op__(s,o,op=op))
  for op in __RICH_COMP_OPS__:
    setattr(obj,f'__{op}__',lambda s,o,op=op: __binary_op__(s,o,op=op))
  return obj

if __name__ == '__main__':
  import numpy as np

  @dataclasses.dataclass
  @superdataclass
  class mycontainer:
    x: object
    y: object
    z: object
  Q=mycontainer(1,2,np.array([3,4,5]))
  print('Dataclass (Q): ', Q)
  print('1+Q: ', 1+Q)
  print('Q+Q: ', Q+Q)
  print('Q*.1: ', Q*.1)
  Q+=1
  print('Q+=1: ', Q)
  print('len(Q): ', len(Q))
  print('Q>=2: ', Q>=2)
  print('Q["x"]: ', Q['x'])
