from pandas.core.frame import DataFrame
from ..mutate import mutate

@mutate.register
def _(df: DataFrame, *args):
    pd_args = {k: v for k, v in args}
    return df.assign(**pd_args)