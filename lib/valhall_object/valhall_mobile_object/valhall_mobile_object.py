from lib.valhall_object import (
    ValhallObject
)

from lib.valhall_object.valhall_static_object.item.item_set import (
    Inventory
)


class ValhallMobileObject(ValhallObject):

    def __init__(self):
        super().__init__()
        self.inventory: "Inventory" = Inventory()

    def __str__(self) -> str:
        return f"Name: {self.name}\n" \
            f"{self._get_stat_str()}"
