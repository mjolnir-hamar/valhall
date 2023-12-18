import curses
import lib.consts.stat_consts.names as stat_names
from lib.ui.valhall_ui_object.valhall_ui_object_set import ValhallUiObjectSet


class GameWindow:

    def __init__(self, nlines: int, ncols: int, begin_y: int, begin_x: int, border_char: str = "-"):

        self.nlines: int = nlines
        self.ncols: int = ncols
        self.window = curses.newwin(self.nlines, self.ncols, begin_y, begin_x)
        self.border_char: str = border_char

    def update(self):
        self.window.clear()
        self._draw_border()
        self.window.addstr(1, 1, f"({self.nlines}, {self.ncols})")
        self.window.refresh()

    def _draw_border(self):
        self.window.addstr(0, 0, self.border_char * (self.ncols - 1))
        self.window.addstr(self.nlines - 1, 0, self.border_char * (self.ncols - 1))
        for i in range(1, self.nlines - 1):
            self.window.addstr(i, 0, self.border_char)
            self.window.addstr(i, self.ncols - 2, self.border_char)


class MapWindow(GameWindow):

    def __init__(self, nlines: int, ncols: int, begin_y: int, begin_x: int):
        super().__init__(nlines, ncols, begin_y, begin_x)

    def update(self, object_set: "ValhallUiObjectSet"):
        self.window.clear()
        self._draw_border()
        self.window.addstr(object_set.player.y, object_set.player.x, object_set.player.map_char)
        for npc in object_set.npcs:
            self.window.addstr(npc.y, npc.x, npc.map_char)
        self.window.refresh()


class StatusWindow(GameWindow):

    def __init__(self, nlines: int, ncols: int, begin_y: int, begin_x: int):
        super().__init__(nlines, ncols, begin_y, begin_x, border_char="=")

    def update(self, object_set: "ValhallUiObjectSet"):
        self.window.clear()
        self._draw_border()
        self.window.addstr(1, 2, object_set.player.object.name)
        self.window.addstr(2, 2, f"{stat_names.HP}: {object_set.player.object.stats.get_stat_val(stat_names.HP)}")
        self.window.addstr(
            3, 2,
            f"{stat_names.ATTACK}: {object_set.player.object.stats.get_stat_val(stat_names.ATTACK)}\t"
            f"{stat_names.MAGIC_ATTACK}: {object_set.player.object.stats.get_stat_val(stat_names.MAGIC_ATTACK)}"
        )
        self.window.addstr(
            4, 2,
            f"{stat_names.DEFENSE}: {object_set.player.object.stats.get_stat_val(stat_names.DEFENSE)}\t"
            f"{stat_names.MAGIC_DEFENSE}: {object_set.player.object.stats.get_stat_val(stat_names.MAGIC_DEFENSE)}"
        )
        self.window.addstr(
            5, 2,
            f"{stat_names.SPEED}: {object_set.player.object.stats.get_stat_val(stat_names.SPEED)}\t"
            f"{stat_names.EVASION}: {object_set.player.object.stats.get_stat_val(stat_names.EVASION)}"
        )
        self.window.refresh()


class InteractWindow(GameWindow):

    def __init__(self, nlines: int, ncols: int, begin_y: int, begin_x: int):
        super().__init__(nlines, ncols, begin_y, begin_x, border_char="=")

    def update(self, frame_text_buffer: list[str]):
        self.window.clear()
        self._draw_border()
        for i, text in enumerate(frame_text_buffer):
            self.window.addstr(i+1, 2, text)
        self.window.refresh()
