from functools import singledispatch

@singledispatch
def mutate(df):
    raise NotImplementedError("Mutate is not implemented for this object")