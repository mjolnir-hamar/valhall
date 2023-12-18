import lib.consts.valhall_object_consts.names as obj_names
from lib.valhall_object.valhall_mobile_object.character import Character
from lib.ui.valhall_ui_object.valhall_ui_object_set import ValhallUiObjectSet


class Skald:

    def __init__(self):

        self.player: "Character" = Character("test", obj_names.HUMAN, obj_names.WARRIOR)
        self.object_set = ValhallUiObjectSet(self.player)
