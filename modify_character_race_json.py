import pprint
import argparse
from copy import deepcopy

import tools.consts.cli.names as names
import lib.consts.stat_consts.names as stat_names
from tools import (
    CLI,
    JsonManager
)
from lib.consts.paths import (
    CHAR_RACE_CONFIG_FILE
)


def add_new_race():
    char_race_config: dict = JsonManager.load_config(CHAR_RACE_CONFIG_FILE)

    print("Configured character races:")
    configured_char_races: dict[int, str] = JsonManager.get_enumerated_keys(char_race_config)
    for i, char_race_name in sorted(configured_char_races.items()):
        print(f"\t{i}. {char_race_name}")

    new_race_name = CLI.get_new_name("character race")
    print()

    print(f"NEW RACE NAME: {new_race_name}")
    if CLI.is_confirmed(
        CLI.get_input_from_choices(
            "Copy template stats from preexisting race?",
            CLI.generic_choices[names.YES_NO]
        )
    ):
        template_race_name: str = configured_char_races[
            CLI.get_input_from_choices_dict(
                "Pick a template race",
                configured_char_races
            )
        ]
        new_race_stats: dict = deepcopy(char_race_config[template_race_name])[stat_names.STAT]
        print(f"Initializing new race stats from template race \"{template_race_name}\"")
    else:
        new_race_stats: dict = names.UNINITIALIZED_RACE_CONFIG
        print(f"Initializing new race stats from blank template")

    for base_stat in stat_names.ALL_BASE_STATS:
        new_race_stat_val: [int, float] = CLI.get_input(
            f"Stat value for \"{base_stat}\" (current value: {new_race_stats[base_stat]}",
            {int, float}
        )

        print(f"New value for \"{base_stat}\": {new_race_stat_val}")
        new_race_stats[base_stat] = new_race_stat_val

    char_race_config[new_race_name] = {
        stat_names.STAT: new_race_stats
    }
    print()
    print(f"Completed new race config for \"{new_race_name}\"")
    pprint.pprint(char_race_config[new_race_name])

    if CLI.is_confirmed(CLI.get_input_from_choices("Save?", CLI.generic_choices[names.YES_NO])):
        JsonManager.save_config(char_race_config, CHAR_RACE_CONFIG_FILE)


def delete_race():
    char_race_config: dict = JsonManager.load_config(CHAR_RACE_CONFIG_FILE)

    configured_char_races: dict[int, str] = JsonManager.get_enumerated_keys(char_race_config)
    race_to_delete: str = configured_char_races[CLI.get_input_from_choices_dict(
        "Pick a race to delete",
        configured_char_races
    )]
    if CLI.is_confirmed(
        CLI.get_input_from_choices(
            f"Confirm deletion of \"{race_to_delete}\"",
            CLI.generic_choices[names.YES_NO]
        )
    ):
        del char_race_config[race_to_delete]

    JsonManager.save_config(char_race_config, CHAR_RACE_CONFIG_FILE)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", action="store_true")
    group.add_argument("-d", "--delete", action="store_true")
    args = parser.parse_args()

    if args.add:
        add_new_race()
    elif args.delete:
        delete_race()


if __name__ == "__main__":
    main()
