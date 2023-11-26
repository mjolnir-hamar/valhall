import unittest

import lib.consts.stat_consts.scaling_function_consts.names as scaling_func_names
from lib.stat.stat import (
    Stat,
    Level,
    Attack
)


class StatTest(unittest.TestCase):

    def test_stat_basics_with_identity(self):

        stat: "Stat" = Stat()
        stat.set_scaling_func(scaling_func_names.IDENTITY, {})
        self.assertEqual(stat.scaling_func.name, scaling_func_names.IDENTITY)

        self.assertEqual(stat.val, 0.)
        stat.set_val(1, 5.)
        self.assertEqual(stat.val, 5.)
        stat.level_up(2)
        self.assertEqual(stat.val, 5.)

    def test_stat_basic_with_linear(self):

        stat: "Stat" = Stat()
        stat.set_scaling_func(
            scaling_func_names.LINEAR,
            {
                scaling_func_names.M: 2,
                scaling_func_names.B: 5
            }
        )
        self.assertEqual(stat.scaling_func.name, scaling_func_names.LINEAR)
        self.assertEqual(stat.scaling_func.m, 2)
        self.assertEqual(stat.scaling_func.b, 5)

        self.assertEqual(stat.val, 0.)
        stat.set_val(1, 5.)
        # val + ((M * level) * B)
        # 5 + ((2 * 1) + 5) = 12.
        self.assertEqual(stat.val, 12.)
        stat.level_up(2)
        # 12. + ((2 * 2) + 5 = 21
        self.assertEqual(stat.val, 21.)

    def test_level_stat(self):

        level: "Level" = Level()
        self.assertIsNone(level.scaling_func)
        level.set_val(1)
        self.assertEqual(level.val, 1)
        level.level_up()
        self.assertEqual(level.val, 2)

    def test_non_level_stat(self):

        attack: "Attack" = Attack()
        attack.set_scaling_func(
            scaling_func_names.LINEAR,
            {
                scaling_func_names.M: 1,
                scaling_func_names.B: 0
            }
        )
        self.assertEqual(attack.scaling_func.name, scaling_func_names.LINEAR)
        self.assertEqual(attack.scaling_func.m, 1)
        self.assertEqual(attack.scaling_func.b, 0)

        attack.set_val(1, 15.)
        self.assertEqual(attack.val, 16.)
        attack.level_up(2)
        self.assertEqual(attack.val, 18.)
