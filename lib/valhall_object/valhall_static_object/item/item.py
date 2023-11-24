import json

import lib.consts.valhall_object_consts.item_consts.names as names
import lib.consts.stat_consts.names as stat_names
import lib.consts.stat_consts.scaling_function_consts.names as scaling_func_names

from lib.valhall_object.valhall_static_object import (
    ValhallStaticObject
)

from lib.consts.paths import (
    CONSUMABLE_CONFIG_FILE,
    EQUIPMENT_CONFIG_FILE
)


with open(CONSUMABLE_CONFIG_FILE, "r") as _j:
    CONSUMABLE_CONFIG = json.load(_j)
with open(EQUIPMENT_CONFIG_FILE, "r") as _j:
    EQUIPMENT_CONFIG = json.load(_j)


class Item(ValhallStaticObject):

    def __init__(self, name: str):
        super().__init__()
        self.name = name


class Consumable(Item):

    def __init__(self, consumable_name: str):
        super().__init__(consumable_name)
        self.base_consumable_config: dict = CONSUMABLE_CONFIG[self.name]
        self._init_stats()

    def __str__(self) -> str:
        return f"Name: {self.name}\n" \
            f"{self._get_stat_str()}"

    def _init_stats(self):
        for stat_name, stat_val in self.base_consumable_config[stat_names.STAT].items():
            self.stats.init_stat(
                stat_name,
                stat_val,
                scaling_func_names.IDENTITY,
                {}
            )


class Equipment(Item):

    def __init__(self, equipment_name: str):
        super().__init__(equipment_name)
        self.base_equipment_config: dict = EQUIPMENT_CONFIG[self.name]
        self.slot: str = self.base_equipment_config[names.SLOT]
        self._init_stats()

    def __str__(self) -> str:
        return f"Name: {self.name}\tSlot: {self.slot}\n" \
            f"{self._get_stat_str()}"

    def _init_stats(self):
        for stat_name, stat_val in self.base_equipment_config[stat_names.STAT].items():
            self.stats.init_stat(
                stat_name,
                stat_val,
                scaling_func_names.IDENTITY,
                {}
            )
