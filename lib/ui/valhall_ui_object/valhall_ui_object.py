from lib.valhall_object import ValhallObject
import lib.consts.stat_consts.names as stat_names


class ValhallUiObject:

    def __init__(
        self,
        valhall_object: "ValhallObject",
        y_pos: int, x_pos: int,
        map_char: str,
        interaction_text_str: str = None,
        is_solid: bool = True
    ):
        self.object: "ValhallObject" = valhall_object
        self.y: int = y_pos
        self.x: int = x_pos
        self.map_char = map_char
        self.interaction_text = self.set_interaction_text(interaction_text_str)
        self.is_solid = is_solid

    def set_interaction_text(self, interaction_text_str) -> list[str]:
        return [
            f"{self.object.name}: {interaction_text_str}",
            f"{stat_names.HP}: {self.object.stats.get_stat_val(stat_names.HP)}",
            f"{stat_names.ATTACK}: {self.object.stats.get_stat_val(stat_names.ATTACK)}\t"
            f"{stat_names.MAGIC_ATTACK}: {self.object.stats.get_stat_val(stat_names.MAGIC_ATTACK)}",
            f"{stat_names.DEFENSE}: {self.object.stats.get_stat_val(stat_names.DEFENSE)}\t"
            f"{stat_names.MAGIC_DEFENSE}: {self.object.stats.get_stat_val(stat_names.MAGIC_DEFENSE)}",
            f"{stat_names.SPEED}: {self.object.stats.get_stat_val(stat_names.SPEED)}\t"
            f"{stat_names.EVASION}: {self.object.stats.get_stat_val(stat_names.EVASION)}"
        ]
