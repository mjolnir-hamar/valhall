from typing import Union

import lib.consts.names as generic_names
import tools.consts.cli.names as names


class CLI:

    general_valid_input_dtypes: set[type] = {int, float, str}

    generic_choices: dict[str, set] = {
        names.YES_NO: names.YES | names.NO
    }

    def __init__(self):
        pass

    @staticmethod
    def get_input(prompt: str, valid_input_dtypes: set) -> Union[int, float, str]:
        user_input = None
        while type(user_input) not in valid_input_dtypes:
            user_input = input(f"{prompt}: ")
            try:
                user_input = int(user_input)
            except ValueError:
                try:
                    user_input = float(user_input)
                except ValueError:
                    user_input = user_input.upper()
        return user_input

    @staticmethod
    def get_input_from_choices(prompt: str, choices: set) -> Union[int, float, str]:
        valid_input_dtypes: set[type] = {type(choice) for choice in choices}
        user_input = None
        while user_input not in choices:
            user_input = CLI.get_input(f"{prompt} ({sorted(choices)})", valid_input_dtypes)
        return user_input

    @staticmethod
    def get_input_from_choices_dict(prompt: str, choices_dict: dict) -> Union[int, float, str]:
        choices: set = set()

        prompt += "\n"
        for choice, choice_desc in sorted(choices_dict.items()):
            choices.add(choice)
            prompt += f"\t{choice}: {choice_desc}\n"
        prompt += "Choice"

        valid_input_dtypes = {type(choice) for choice in choices}
        user_input = None
        while user_input not in choices:
            user_input = CLI.get_input(prompt, valid_input_dtypes)
        return user_input

    @staticmethod
    def is_confirmed(user_input: str) -> bool:
        if user_input in names.YES:
            return True
        else:
            return False

    @staticmethod
    def get_new_name(name_type: str):
        new_name: str = generic_names.DEFAULT
        is_confirmed: bool = False

        while not is_confirmed:
            new_name: str = CLI.get_input(f"New {name_type} name", {str})
            is_confirmed = CLI.is_confirmed(
                CLI.get_input_from_choices(
                    f"New {name_type} name is \"{new_name}\"?",
                    CLI.generic_choices[names.YES_NO]
                )
            )

        return new_name
