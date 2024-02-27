"""global-scope data for users and tasks"""

from pathlib import Path
import sys
import os

USER_LIST = []
TASK_LIST = []
CURRENT_USER = None  # place for the user currently using the app

#
# Paths
#
CWD = Path(os.path.dirname(sys.argv[0]))
DATA_PATH = CWD.joinpath("src/data")
PATH_CONSTS = {
    "USER_LIST": DATA_PATH.joinpath("users.yaml"),
    "TASK_LIST": DATA_PATH.joinpath("tasks.yaml"),
}
