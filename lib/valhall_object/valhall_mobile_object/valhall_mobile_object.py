from lib.valhall_object import (
    ValhallObject
)

from lib.valhall_object.valhall_static_object.item import (
    Item
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

    def add_item_to_inventory(self, item_to_add: "Item"):
        self.inventory.add_item(item_to_add)

    def remove_item_from_inventory(self, item_name_to_remove: str):
        self.inventory.remove_item(item_name_to_remove)
