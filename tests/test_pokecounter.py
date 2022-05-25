def test_pokedex_length():
    from pokecounter.pokedex import POKEDEX

    assert len(POKEDEX) == 905


def test_paths():
    from pokecounter.config import (
        BASE_PATH,
        BASE_SPRITES_PATH,
        ALOLAN_SPRITES,
        GALARIAN_SPRITES,
        HISUIAN_SPRITES,
        STANDARD_SPRITES,
    )
    from pathlib import Path

    assert Path.exists(BASE_PATH)
    assert Path.exists(BASE_SPRITES_PATH)
    assert Path.exists(ALOLAN_SPRITES)
    assert Path.exists(GALARIAN_SPRITES)
    assert Path.exists(HISUIAN_SPRITES)
    assert Path.exists(STANDARD_SPRITES)
