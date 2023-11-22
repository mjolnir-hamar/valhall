import json

from lib.consts.paths import (
    CHAR_JOB_CONFIG_FILE,
    CHAR_RACE_CONFIG_FILE
)
import lib.consts.stat_consts.names as stat_names

from lib.valhall_object.valhall_mobile_object import (
    ValhallMobileObject
)

from lib.valhall_object.valhall_static_object.item.item_set import (
    EquipmentSet
)

with open(CHAR_JOB_CONFIG_FILE, "r") as _j:
    CHAR_JOB_CONFIG = json.load(_j)
with open(CHAR_RACE_CONFIG_FILE, "r") as _j:
    CHAR_RACE_CONFIG = json.load(_j)


class Character(ValhallMobileObject):

    def __init__(self, name: str, race: str, job: str):
        super().__init__()
        self.name: str = name.upper()
        self.race: str = race
        self.job: str = job
        self.base_job_config: dict = CHAR_JOB_CONFIG[self.job]
        self.base_race_config: dict = CHAR_RACE_CONFIG[self.race]
        self._init_stats()
        self.equipment: "EquipmentSet" = EquipmentSet()

    def _init_stats(self):
        self.stats.level.set_val(1)
        for stat_name, race_stat_val in self.base_race_config[stat_names.STAT].items():
            self.stats.init_stat(
                stat_name,
                race_stat_val + self.base_job_config[stat_names.STAT][stat_name][stat_names.VAL],
                self.base_job_config[stat_names.STAT][stat_name][stat_names.FUNC][stat_names.NAME],
                self.base_job_config[stat_names.STAT][stat_name][stat_names.FUNC][stat_names.PARAMS]
            )

    def _compute_stat(self, stat_name: str) -> float:
        return self.stats.get_stat(stat_name) + self.equipment.get_equipment_stat_modifier(stat_name)
