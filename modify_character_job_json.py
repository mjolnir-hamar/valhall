import pprint
import argparse
from copy import deepcopy

from tools import (
    CLI,
    JsonManager
)
import tools.consts.cli.names as names
import lib.consts.stat_consts.names as stat_names
import lib.consts.stat_consts.scaling_function_consts.names as scaling_func_names
from lib.consts.paths import (
    CHAR_JOB_CONFIG_FILE
)

SCALING_FUNC_CHOICES: dict = {
    i+1: scaling_func_name
    for i, scaling_func_name in enumerate(sorted(scaling_func_names.ALL_SCALING_FUNCTIONS.keys()))
}


def add_new_job():
    char_job_config: dict = JsonManager.load_config(CHAR_JOB_CONFIG_FILE)

    print("Configured character jobs:")
    configured_char_jobs: dict[int, str] = JsonManager.get_enumerated_keys(char_job_config)
    for i, char_job_name in sorted(configured_char_jobs.items()):
        print(f"\t{i}. {char_job_name}")

    new_job_name = CLI.get_new_name("character job")
    print()

    print(f"NEW JOB NAME: {new_job_name}")
    if CLI.is_confirmed(
        CLI.get_input_from_choices(
            "Copy template stats from preexisting job?",
            CLI.generic_choices[names.YES_NO]
        )
    ):
        template_job_name: str = configured_char_jobs[
            CLI.get_input_from_choices_dict(
                "Pick a template job",
                configured_char_jobs
            )
        ]
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
        JsonManager.save_config(char_job_config, CHAR_JOB_CONFIG_FILE)


def delete_job():
    char_job_config: dict = JsonManager.load_config(CHAR_JOB_CONFIG_FILE)

    configured_char_jobs: dict[int, str] = JsonManager.get_enumerated_keys(char_job_config)
    job_to_delete: str = configured_char_jobs[CLI.get_input_from_choices_dict(
        "Pick a job to delete",
        configured_char_jobs
    )]
    if CLI.is_confirmed(
        CLI.get_input_from_choices(
            f"Confirm deletion of \"{job_to_delete}\"",
            CLI.generic_choices[names.YES_NO]
        )
    ):
        del char_job_config[job_to_delete]

    JsonManager.save_config(char_job_config, CHAR_JOB_CONFIG_FILE)


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
