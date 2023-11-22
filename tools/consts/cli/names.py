from copy import deepcopy
import lib.consts.stat_consts.names as stat_names

YES_NO: str = "YES/NO"

YES: set[str] = {"YES", "Y"}
NO: set[str] = {"NO", "N"}

UNINITIALIZED_STAT_CONFIG: dict = {
    "VAL": -1,
    "FUNC": {
        "NAME": "IDENTITY",
        "PARAMS": {}
    }
}

UNINITIALIZED_JOB_CONFIG: dict = {
    base_stat: deepcopy(UNINITIALIZED_STAT_CONFIG) for base_stat in stat_names.ALL_BASE_STATS
}
