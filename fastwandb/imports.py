import shutil
from typing import Union


import wandb
import matplotlib.pyplot as plt

from PIL import Image
from fastcore.all import *

File = Union[Path, str]
Number = Union[int, float]