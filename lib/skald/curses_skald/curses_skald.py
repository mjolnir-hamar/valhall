import curses
from lib.skald import Skald
from lib.ui.curses import (
    MapWindow,
    StatusWindow,
    InteractWindow
)
import lib.consts.ui_consts.curses.consts as curses_consts


class CursesSkald(Skald):

    def __init__(self):
        super().__init__()
        self.frame_text_buffer = []

    def update_game_windows(
        self,
        map_window: "MapWindow",
        status_window: "StatusWindow",
        interact_window: "InteractWindow"
    ):
        map_window.update(self.object_set)
        status_window.update(self.object_set)
        interact_window.update(self.frame_text_buffer)
        self.frame_text_buffer = []

    def _run(self):
        curses.initscr()
        curses.noecho()

        center_y = curses.LINES // 2
        center_x = curses.COLS // 2
        begin_y = center_y - (curses_consts.NLINES // 2)
        begin_x = center_x - (curses_consts.NCOLS // 2)

        map_window_nlines = int(curses_consts.NLINES * curses_consts.MAP_WINDOW_PERC)
        status_window_nlines = curses_consts.NLINES - map_window_nlines
        status_window_ncols = curses_consts.NCOLS // 2

        map_window = MapWindow(map_window_nlines, curses_consts.NCOLS, begin_y, begin_x)
        status_window = StatusWindow(status_window_nlines, status_window_ncols, begin_y + map_window_nlines, begin_x)
        interact_window = InteractWindow(
            status_window_nlines, status_window_ncols, begin_y + map_window_nlines, begin_x + (curses_consts.NCOLS // 2)
        )
        self.update_game_windows(map_window, status_window, interact_window)

        while True:
            key = map_window.window.get_wch()
            if key in curses_consts.MVNT_KEYS.keys():
                self.object_set.update_player_pos(
                    curses_consts.MVNT_KEYS[key][0],
                    curses_consts.MVNT_KEYS[key][1],
                    map_window.nlines,
                    map_window.ncols
                )
            elif key == "e":
                interact_text = self.object_set.get_interact_text()
                if interact_text:
                    self.frame_text_buffer += interact_text
            elif key == "q":
                break
            self.update_game_windows(map_window, status_window, interact_window)
        curses.echo()
        curses.endwin()

    def __call__(self):
        self._run()
