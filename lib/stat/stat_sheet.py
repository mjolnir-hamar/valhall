import lib.consts.stat_consts.names as names

from .stat import (
    Stat,
    Level,
    HP,
    Attack,
    MagicAttack,
    Defense,
    MagicDefense,
    Speed,
    Evasion
)


class StatSheet:

    def __init__(self):
        self.level: "Level" = Level()
        self.hp: "HP" = HP()
        self.attack: "Attack" = Attack()
        self.magic_attack: "MagicAttack" = MagicAttack()
        self.defense: "Defense" = Defense()
        self.magic_defense: "MagicDefense" = MagicDefense()
        self.speed: "Speed" = Speed()
        self.evasion: "Evasion" = Evasion()

        self.all_base_stats: list[Stat] = [
            self.hp,
            self.attack, self.magic_attack,
            self.defense, self.magic_defense,
            self.speed, self.evasion
        ]

    def __str__(self) -> str:
        return f"Level: {self.level}\n" \
            f"HP: {self.hp}\n" \
            f"Attack: {self.attack}\tMagic Attack: {self.magic_attack}\n" \
            f"Defense: {self.defense}\tMagic Defense: {self.magic_defense}\n" \
            f"Speed: {self.speed}\tEvasion: {self.evasion}"

    def init_stat(self, stat_name: str, val: float, scaling_func_name: str, scaling_func_params: dict[str, float]):
        if stat_name == names.LEVEL:
            self.level.set_val(val)
        elif stat_name == names.HP:
            self.hp.set_scaling_func(scaling_func_name, scaling_func_params)
            self.hp.set_val(self.level.val, val)
        elif stat_name == names.ATTACK:
            self.attack.set_scaling_func(scaling_func_name, scaling_func_params)
            self.attack.set_val(self.level.val, val)
        elif stat_name == names.MAGIC_ATTACK:
            self.magic_attack.set_scaling_func(scaling_func_name, scaling_func_params)
            self.magic_attack.set_val(self.level.val, val)
        elif stat_name == names.DEFENSE:
            self.defense.set_scaling_func(scaling_func_name, scaling_func_params)
            self.defense.set_val(self.level.val, val)
        elif stat_name == names.MAGIC_DEFENSE:
            self.magic_defense.set_scaling_func(scaling_func_name, scaling_func_params)
            self.magic_defense.set_val(self.level.val, val)
        elif stat_name == names.SPEED:
            self.speed.set_scaling_func(scaling_func_name, scaling_func_params)
            self.speed.set_val(self.level.val, val)
        elif stat_name == names.EVASION:
            self.evasion.set_scaling_func(scaling_func_name, scaling_func_params)
            self.evasion.set_val(self.level.val, val)
        else:
            raise ValueError(f"Unknown stat name: {stat_name}")

    def get_stat(self, stat_name: str) -> float:
        if stat_name == names.LEVEL:
            return self.level.val
        elif stat_name == names.HP:
            return self.hp.val
        elif stat_name == names.ATTACK:
            return self.attack.val
        elif stat_name == names.MAGIC_ATTACK:
            return self.magic_attack.val
        elif stat_name == names.DEFENSE:
            return self.defense.val
        elif stat_name == names.MAGIC_DEFENSE:
            return self.magic_defense.val
        elif stat_name == names.SPEED:
            return self.speed.val
        elif stat_name == names.EVASION:
            return self.evasion.val
        else:
            raise ValueError(f"Unknown stat name: {stat_name}")

    def level_up(self):
        self.level.level_up()
        for base_stat in self.all_base_stats:
            base_stat.level_up(self.level.val)
