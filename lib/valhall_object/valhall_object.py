from lib.consts.names import (
    DEFAULT
)
from lib.stat import (
    StatSheet
)
import lib.consts.stat_consts.names as stat_names


class ValhallObject:

    def __init__(self):
        self.name: str = DEFAULT
        self.stats: "StatSheet" = StatSheet()

    def _compute_stat(self, stat_name: str) -> float:
        return self.stats.get_stat_val(stat_name)

    def _get_stat_str(self) -> str:
        stat_str: str = ""
        for stat_line in stat_names.ALL_STATS:
            for stat_name in stat_line:
                stat_val = self._compute_stat(stat_name)
                if stat_val > 0:
                    if len(stat_str) > 0:
                        if stat_str[-1] != "\n":
                            stat_str += "\t"
                    stat_str += f"{stat_name}: {stat_val}"
            if len(stat_str) > 0:
                if stat_str[-1] != "\n":
                    stat_str += "\n"
        return stat_str.strip()
