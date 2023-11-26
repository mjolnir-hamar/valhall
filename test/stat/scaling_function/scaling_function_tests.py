import unittest

import lib.consts.stat_consts.scaling_function_consts.names as scaling_func_names
from lib.stat.scaling_function import (
    ScalingFunction,
    IdentityFunction,
    LinearFunction
)

TEST_LEVEL = 1
TEST_VAL = 10


class ScalingFunctionTest(unittest.TestCase):

    def test_scaling_function_basics(self):

        zero_func: "ScalingFunction" = ScalingFunction()
        self.assertEqual(zero_func.name, scaling_func_names.ZERO)
        self.assertEqual(zero_func(TEST_LEVEL, TEST_VAL), 0.)

    def test_identity_function_basics(self):

        ident_func: "IdentityFunction" = IdentityFunction()
        self.assertEqual(ident_func.name, scaling_func_names.IDENTITY)
        self.assertEqual(ident_func(TEST_LEVEL, TEST_VAL), TEST_VAL)

    def test_linear_function_basics(self):

        linear_func: "LinearFunction" = LinearFunction(m=2, b=10)
        self.assertEqual(linear_func.name, scaling_func_names.LINEAR)
        self.assertEqual(linear_func.m, 2)
        self.assertEqual(linear_func.b, 10)
        self.assertEqual(linear_func(TEST_LEVEL, TEST_VAL), 22)
