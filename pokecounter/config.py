"""
PokeCounter Config Loader

This module is responsible for
loading in configuration values,
saving configurations to a file,
and exporting some constant values
that will be used elsewhere in the
application
"""

from pathlib import Path

BASE_PATH = Path(__file__).parent.absolute()
BASE_SPRITES_PATH = BASE_PATH / "static" / "assets" / "sprites"
STANDARD_SPRITES = BASE_SPRITES_PATH / "standard"
ALOLAN_SPRITES = BASE_SPRITES_PATH / "alola"
GALARIAN_SPRITES = BASE_SPRITES_PATH / "galar"
HISUIAN_SPRITES = BASE_SPRITES_PATH / "hisui"
ICON_PATH = BASE_PATH / "static" / "assets" / "icon.png"
