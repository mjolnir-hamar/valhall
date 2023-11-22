import lib.consts.stat_consts.names as names
import lib.consts.stat_consts.scaling_function_consts.names as scaling_func_names

import lib.stat.scaling_function as scaling_funcs


class Stat:

    name: str = names.STAT
    val: float = 0.
    scaling_func: "scaling_funcs.ScalingFunction" = None

    def __init__(self):
        pass

    def __str__(self) -> str:
        return str(self.val)

    def set_val(self, level: float, val: float):
        self.val = self.scaling_func(level, val)

    def set_scaling_func(self, scaling_func_name: str, scaling_func_params: dict[str, float]):
        if scaling_func_name == scaling_func_names.IDENTITY:
            self.scaling_func = scaling_funcs.IdentityFunction(**scaling_func_params)
        elif scaling_func_name == scaling_func_names.LINEAR:
            self.scaling_func = scaling_funcs.LinearFunction(**scaling_func_params)

    def level_up(self, level: float):
        self.val = self.scaling_func(level, self.val)


class Level(Stat):

    name: str = names.LEVEL

    def __init__(self):
        super().__init__()

    def set_val(self, val: float):
        self.val = val

    def level_up(self):
        self.val += 1


class HP(Stat):

    name: str = names.HP

    def __init__(self):
        super().__init__()


class Attack(Stat):

    name: str = names.ATTACK

    def __init__(self):
        super().__init__()


class MagicAttack(Stat):

    name: str = names.MAGIC_ATTACK

    def __init__(self):
        super().__init__()


class Defense(Stat):

    name: str = names.DEFENSE

    def __init__(self):
        super().__init__()


class MagicDefense(Stat):

    name: str = names.MAGIC_DEFENSE

    def __init__(self):
        super().__init__()


class Speed(Stat):

    name: str = names.SPEED

    def __init__(self):
        super().__init__()


class Evasion(Stat):

    name: str = names.EVASION

    def __init__(self):
        super().__init__()
