import json
import unittest

import lib.consts.paths as paths
import lib.consts.stat_consts.names as stat_names
import lib.consts.valhall_object_consts.names as obj_names
import lib.consts.valhall_object_consts.item_consts.names as item_names


class CharacterConfigTest(unittest.TestCase):

    def test_character_job_config_file(self):
        with open(paths.CHAR_JOB_CONFIG_FILE, "r") as _j:
            char_job_config: dict = json.load(_j)

        for char_job_entry in char_job_config.values():
            self.assertEqual(set(char_job_entry.keys()), {stat_names.STAT})
            self.assertEqual(set(char_job_entry[stat_names.STAT]), set(stat_names.ALL_BASE_STATS))
            for char_job_stat_details in char_job_entry[stat_names.STAT].values():
                self.assertEqual(set(char_job_stat_details.keys()), {stat_names.FUNC, stat_names.VAL})
                char_job_stat_func_spec: dict = char_job_stat_details[stat_names.FUNC]
                self.assertEqual(set(char_job_stat_func_spec.keys()), {stat_names.NAME, stat_names.PARAMS})
                self.assertIsInstance(char_job_stat_func_spec[stat_names.NAME], str)
                self.assertIsInstance(char_job_stat_func_spec[stat_names.PARAMS], dict)
                self.assertIn(type(char_job_stat_details[stat_names.VAL]), {int, float})

    def test_character_race_config_file(self):
        with open(paths.CHAR_RACE_CONFIG_FILE, "r") as _j:
            char_race_config: dict = json.load(_j)

        self.assertEqual(set(char_race_config.keys()), obj_names.ALL_RACES)
        for char_race_entry in char_race_config.values():
            self.assertEqual(set(char_race_entry.keys()), {stat_names.STAT})
            char_race_stats: dict = char_race_entry[stat_names.STAT]
            self.assertEqual(set(char_race_stats.keys()), set(stat_names.ALL_BASE_STATS))
            for char_race_stat, char_race_stat_val in char_race_stats.items():
                self.assertIn(type(char_race_stat_val), {int, float})


class ItemTest(unittest.TestCase):

    def test_consumable_config_file(self):
        with open(paths.CONSUMABLE_CONFIG_FILE, "r") as _j:
            consumable_config: dict = json.load(_j)

        self.assertEqual(set(consumable_config.keys()), item_names.ALL_CONSUMABLES)
        for consumable_entry in consumable_config.values():
            self.assertEqual(set(consumable_entry.keys()), {stat_names.STAT})
            for consumable_stat, consumable_stat_val in consumable_entry[stat_names.STAT].items():
                self.assertIn(consumable_stat, stat_names.ALL_BASE_STATS_WITH_LEVEL)
                self.assertIn(type(consumable_stat_val), {int, float})

    def test_equipment_config_file(self):
        with open(paths.EQUIPMENT_CONFIG_FILE, "r") as _j:
            equipment_config: dict = json.load(_j)

        self.assertEqual(set(equipment_config.keys()), item_names.ALL_EQUIPMENT)
        for equipment_entry in equipment_config.values():
            self.assertEqual(set(equipment_entry.keys()), {item_names.SLOT, stat_names.STAT})
            self.assertIn(equipment_entry[item_names.SLOT], item_names.ALL_SLOTS)
            for equipment_stat, equipment_stat_val in equipment_entry[stat_names.STAT].items():
                self.assertIn(equipment_stat, stat_names.ALL_BASE_STATS_WITH_LEVEL)
                self.assertIn(type(equipment_stat_val), {int, float})
