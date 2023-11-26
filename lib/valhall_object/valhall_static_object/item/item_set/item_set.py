import lib.consts.valhall_object_consts.item_consts.names as names

from lib.valhall_object.valhall_static_object.item import (
    Item,
    Equipment
)


class ItemSet:

    def __init__(self):
        pass


class InventorySlot:

    def __init__(self):
        self.item_in_slot: "Item" = None
        self.quantity: int = 0

    def get_item_name(self) -> str:
        return self.item_in_slot.name

    def is_empty(self) -> bool:
        if not self.item_in_slot:
            return True
        else:
            return False

    def add_item(self, item_to_add: "Item"):
        if not self.item_in_slot:
            self.item_in_slot = item_to_add
        self.quantity += 1

    def remove_item(self):
        self.quantity -= 1
        if self.quantity == 0:
            self.item_in_slot = None


class Inventory(ItemSet):

    def __init__(self, size: int = 10):
        super().__init__()
        self.size = size
        self.items: tuple["InventorySlot"] = tuple(InventorySlot() for i in range(self.size))

    def __str__(self) -> str:
        inventory_str = ""
        for i, inventory_slot in enumerate(self.items):
            if inventory_slot.is_empty():
                inventory_str += f"{i+1}. EMPTY\n"
            else:
                inventory_str += f"{i+1}. {inventory_slot.get_item_name()} ({inventory_slot.quantity})\n"
        return inventory_str.strip()

    def add_item(self, item_to_add: "Item"):
        item_to_add_name = item_to_add.name
        first_empty_slot_idx = -1
        is_item_added = False
        for i, inventory_slot in enumerate(self.items):
            if inventory_slot.is_empty():
                if first_empty_slot_idx == -1:
                    first_empty_slot_idx = i
            else:
                if inventory_slot.get_item_name() == item_to_add_name:
                    inventory_slot.add_item(item_to_add)
                    is_item_added = True
                    break
        if first_empty_slot_idx != -1 and not is_item_added:
            self.items[first_empty_slot_idx].add_item(item_to_add)

    def remove_item(self, item_name_to_remove: str):
        for inventory_slot in self.items:
            if not inventory_slot.is_empty():
                if inventory_slot.get_item_name() == item_name_to_remove:
                    inventory_slot.remove_item()
                    break


class EquipmentSlot:

    def __init__(self, slot_name: str):
        self.slot_name: str = slot_name
        self.equipment: "Equipment" = Equipment(f"{names.BLANK}_{self.slot_name}")


class EquipmentSet(ItemSet):

    def __init__(self):
        super().__init__()
        self.head: "EquipmentSlot" = EquipmentSlot(names.HEAD)
        self.body: "EquipmentSlot" = EquipmentSlot(names.BODY)
        self.arms: "EquipmentSlot" = EquipmentSlot(names.ARMS)
        self.hands: "EquipmentSlot" = EquipmentSlot(names.HANDS)
        self.legs: "EquipmentSlot" = EquipmentSlot(names.LEGS)
        self.feet: "EquipmentSlot" = EquipmentSlot(names.FEET)
        self.all_slots: list[list["EquipmentSlot"]] = [
            [self.head, self.body],
            [self.arms, self.hands],
            [self.legs, self.feet]
        ]

    def __str__(self) -> str:
        equipment_str: str = ""
        for line in self.all_slots:
            for equipment in line:
                if len(equipment_str) > 0:
                    if equipment_str[-1] != "\n":
                        equipment_str += "\t"
                equipment_str += f"{equipment.slot_name}: "
                if equipment.equipment:
                    equipment_str += f"{equipment.equipment.name}"
                else:
                    equipment_str += "NONE"
            if len(equipment_str) > 0:
                if equipment_str[-1] != "\n":
                    equipment_str += "\n"
        return equipment_str.strip()

    def get_equipment_slot(self, slot_name: str) -> "EquipmentSlot":
        if slot_name == names.HEAD:
            return self.head
        elif slot_name == names.BODY:
            return self.body
        elif slot_name == names.ARMS:
            return self.arms
        elif slot_name == names.HANDS:
            return self.hands
        elif slot_name == names.LEGS:
            return self.legs
        elif slot_name == names.FEET:
            return self.feet
        else:
            raise ValueError(f"Unknown equipment slot name: {slot_name}")

    def get_equipment_stat_modifier(self, stat_name: str) -> float:
        total_modifier = 0.
        for line in self.all_slots:
            for equipment in line:
                total_modifier += equipment.equipment.stats.get_stat_val(stat_name)
        return total_modifier

    def add_equipment(self, new_equipment: "Equipment"):
        self.get_equipment_slot(new_equipment.slot).equipment = new_equipment
