from .aircrack import *
from .aireplay import *
from .airmon import *
from .airodump import *
from .is_installed import *
import os

if is_installed() == False:
    os.system('sudo apt install aircrack-ng')
