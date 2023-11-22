from math import (
    ceil
)

import lib.consts.stat_consts.scaling_function_consts.names as names


class ScalingFunction:

    name: str = names.ZERO

    def __init__(self, **kwargs):
        pass

    def __call__(self, level: float, val: float) -> float:
        return 0.


class IdentityFunction(ScalingFunction):

    name: str = names.IDENTITY

    def __init__(self, **kwargs):
        super().__init__()

    def __call__(self, level: float, val: float) -> float:
        return val


class LinearFunction(ScalingFunction):

    name: str = names.LINEAR

    def __init__(self, **kwargs):
        super().__init__()
        self.m: float = kwargs[names.M]
        self.b: float = kwargs[names.B]

    def __call__(self, level: float, val: float) -> float:
        return ceil(val + ((self.m * level) + self.b))
