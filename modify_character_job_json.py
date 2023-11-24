import json
import pprint
import argparse
from copy import deepcopy

from tools.cli import (
    CLI
)
import tools.consts.cli.names as names
import lib.consts.names as generic_names
import lib.consts.stat_consts.names as stat_names
import lib.consts.stat_consts.scaling_function_consts.names as scaling_func_names
from lib.consts.paths import (
    CHAR_JOB_CONFIG_FILE
)

SCALING_FUNC_CHOICES: dict = {
    i + 1: scaling_func_name
    for i, scaling_func_name in enumerate(sorted(scaling_func_names.ALL_SCALING_FUNCTIONS.keys()))
}


def load_job_config() -> dict:
    with open(CHAR_JOB_CONFIG_FILE, "r") as _j:
        char_job_config: dict = json.load(_j)
    return char_job_config


def save_job_config(char_job_config: dict):
    with open(CHAR_JOB_CONFIG_FILE, "w") as _j:
        json.dump(char_job_config, _j, indent=2, sort_keys=True)


def get_new_job_name() -> [str, bool]:
    new_job_name: str = CLI.get_input("New character job name", {str})
    is_confirmed: bool = CLI.is_confirmed(
        CLI.get_input_from_choices(
            f"New job name is \"{new_job_name}\"?",
            CLI.generic_choices[names.YES_NO]
        )
    )
    return new_job_name, is_confirmed


def add_new_job():
    char_job_config: dict = load_job_config()

    print("Configured character jobs:")
    for i, char_job_name in enumerate(sorted(char_job_config.keys())):
        print(f"\t{i + 1}. {char_job_name}")

    is_confirmed: bool = False
    new_job_name: str = generic_names.DEFAULT
    while not is_confirmed:
        new_job_name, is_confirmed = get_new_job_name()

    print()

    print(f"NEW JOB NAME: {new_job_name}")
    if CLI.is_confirmed(
            CLI.get_input_from_choices(
                "Copy template stats from preexisting job?",
                CLI.generic_choices[names.YES_NO]
            )
    ):
        template_job_options: dict[int, str] = {
            i + 1: char_job_name for i, char_job_name in enumerate(sorted(char_job_config.keys()))
        }
        template_job_idx: int = CLI.get_input_from_choices_dict(
            "Pick a template job",
            template_job_options
        )
        template_job_name: str = template_job_options[template_job_idx]
        new_job_stats: dict = deepcopy(char_job_config[template_job_name])[stat_names.STAT]
        print(f"Initializing new job stats from template job \"{template_job_name}\"")
    else:
        new_job_stats: dict = names.UNINITIALIZED_JOB_CONFIG
        print(f"Initializing new job stats from blank template")

    for base_stat in stat_names.ALL_BASE_STATS:
        new_job_stat: dict = new_job_stats[base_stat]
        new_job_stat_val: [int, float] = CLI.get_input(
            f"Stat value for \"{base_stat}\" (current value: {new_job_stat[stat_names.VAL]})",
            {int, float}
        )
        new_job_scaling_func: str = SCALING_FUNC_CHOICES[CLI.get_input_from_choices_dict(
            "Pick a scaling function",
            SCALING_FUNC_CHOICES
        )]
        new_scaling_func_params: dict = {
            param: CLI.get_input(
                f"Set parameter value for \"{param}\"", {int, float}
            ) for param in scaling_func_names.ALL_SCALING_FUNCTIONS[new_job_scaling_func]
        }
        print(f"New scaling function: {new_job_scaling_func} ({new_scaling_func_params})")

        print(f"New value for \"{base_stat}\": {new_job_stat_val}")
        new_job_stat[stat_names.VAL] = new_job_stat_val
        new_job_stat[stat_names.FUNC][stat_names.NAME] = new_job_scaling_func
        new_job_stat[stat_names.FUNC][stat_names.PARAMS] = new_scaling_func_params

    char_job_config[new_job_name] = {
        stat_names.STAT: new_job_stats
    }
    print()
    print(f"Completed new job config for \"{new_job_name}")
    pprint.pprint(char_job_config[new_job_name])

    if CLI.is_confirmed(CLI.get_input_from_choices("Save?", CLI.generic_choices[names.YES_NO])):
        save_job_config(char_job_config)


def delete_job():
    char_job_config: dict = load_job_config()

    configured_jobs: dict[int, str] = {
        i + 1: char_job_name for i, char_job_name in enumerate(sorted(char_job_config.keys()))
    }
    job_to_delete: str = configured_jobs[CLI.get_input_from_choices_dict(
        "Pick a job to delete",
        configured_jobs
    )]
    if CLI.is_confirmed(
            CLI.get_input_from_choices(f"Confirm deletion of \"{job_to_delete}\"", CLI.generic_choices[names.YES_NO])):
        del char_job_config[job_to_delete]

    save_job_config(char_job_config)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", action="store_true")
    group.add_argument("-d", "--delete", action="store_true")
    args = parser.parse_args()

    if args.add:
        add_new_job()
    elif args.delete:
        delete_job()


if __name__ == "__main__":
    main()
