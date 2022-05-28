import os
from pathlib import Path

MODULE_PATH: Path = Path(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH: Path = MODULE_PATH.parent.parent
