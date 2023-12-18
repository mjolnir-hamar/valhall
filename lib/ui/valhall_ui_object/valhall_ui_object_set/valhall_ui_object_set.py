from typing import Union
from lib.valhall_object.valhall_mobile_object.character import Character
from lib.ui.valhall_ui_object import ValhallUiObject


class ValhallUiObjectSet:

    def __init__(self, player: "Character"):
        self.player = ValhallUiObject(player, 5, 5, "@")
        self.npcs: list["ValhallUiObject"] = []

    def add_npc(self, npc: "Character", y_pos: int, x_pos: int, map_char: str, interaction_text: str):
        self.npcs.append(ValhallUiObject(npc, y_pos, x_pos, map_char, interaction_text))

    def check_adjacent_npc(self, y, x, exact_position=False):
        for i, npc in enumerate(self.npcs):
            if exact_position:
                if (npc.y == y and npc.x == x) and npc.is_solid:
                    return i
            else:
                if ((npc.y-1 == y or npc.y+1 == y) and npc.x == x) or (npc.y == y and (npc.x-1 == x or npc.x+1 == x)):
                    return i
        return -1

    def get_interact_text(self) -> Union[None, list[str]]:
        adjacent_npc_idx: int = self.check_adjacent_npc(self.player.y, self.player.x)
        if adjacent_npc_idx != -1:
            adjacent_npc: "ValhallUiObject" = self.npcs[adjacent_npc_idx]
            if adjacent_npc.interaction_text:
                return adjacent_npc.interaction_text
            else:
                return [adjacent_npc.object.name]
        else:
            return None

    def update_player_pos(self, y_mod: int, x_mod: int, nlines: int, ncols: int):
        new_y: int = self.player.y + y_mod
        new_x: int = self.player.x + x_mod

        if (0 < new_y < nlines-1) and (0 < new_x < ncols-1):
            adjacent_npc_idx: int = self.check_adjacent_npc(new_y, new_x, exact_position=True)
            if adjacent_npc_idx == -1:
                self.player.y = new_y
                self.player.x = new_x
