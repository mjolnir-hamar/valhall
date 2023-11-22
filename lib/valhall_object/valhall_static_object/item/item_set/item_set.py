import lib.consts.valhall_object_consts.item_consts.names as names

from lib.valhall_object.valhall_static_object.item import (
    Equipment
)


class ItemSet:

    def __init__(self):
        pass


class Inventory(ItemSet):

    def __init__(self):
        super().__init__()


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
                total_modifier += equipment.equipment.stats.get_stat(stat_name)
        return total_modifier

    def add_equipment(self, new_equipment: "Equipment"):
        self.get_equipment_slot(new_equipment.slot).equipment = new_equipment
