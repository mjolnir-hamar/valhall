import unittest

import lib.consts.stat_consts.names as stat_names
import lib.consts.stat_consts.scaling_function_consts.names as scaling_func_names
from lib.stat import (
    StatSheet
)
from lib.stat.stat import (
    HP,
    Attack,
    MagicAttack,
    Defense,
    MagicDefense,
    Speed,
    Evasion
)

VAL = 2.
TEST_SCALING_FUNC = scaling_func_names.LINEAR
M = 2
B = 0


class StatSheetTest(unittest.TestCase):

    def test_stat_sheet_basics(self):

        stat_sheet: "StatSheet" = StatSheet()
        self.assertEqual(
            [type(stat) for stat in stat_sheet.all_base_stats],
            [
                HP,
                Attack, MagicAttack,
                Defense, MagicDefense,
                Speed, Evasion
            ]
        )
        self.assertEqual(
            [stat.val for stat in stat_sheet.all_base_stats],
            [0. for i in range(len(stat_sheet.all_base_stats))]
        )

        stat_sheet.level.set_val(1)
        self.assertEqual(stat_sheet.get_stat_val(stat_names.LEVEL), 1.)
        self.assertIsNone(stat_sheet.level.scaling_func)

        for stat in stat_names.ALL_BASE_STATS:
            stat_sheet.init_stat(
                stat,
                VAL,
                TEST_SCALING_FUNC,
                {
                    scaling_func_names.M: M,
                    scaling_func_names.B: B
                }
            )
            self.assertEqual(stat_sheet.get_stat_val(stat), 4.)
            self.assertEqual( stat_sheet.get_stat_scaling_func(stat).name, TEST_SCALING_FUNC)
            self.assertEqual( stat_sheet.get_stat_scaling_func(stat).m, M)
            self.assertEqual( stat_sheet.get_stat_scaling_func(stat).b, B)

        stat_sheet.level_up()
        self.assertEqual(stat_sheet.level.val, 2)

        for stat in stat_names.ALL_BASE_STATS:
            self.assertEqual(stat_sheet.get_stat_val(stat), 8.)
