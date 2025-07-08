"""Top-level API for scipyconference.

This is the file from which you can do:

    from scipyconference import some_function

Use it to control the top-level API of your Python data science project.
"""

import random

import numpy as np

from .bots import punbot


def create_puns(number: int, prompt: str = ""):
    """Create `number` of puns for the SciPy conference."""
    if number is np.inf:
        # TODO: make this to do something really special
        party_emojis = [
            "🎉",
            "🎊",
            "🎈",
            "🎂",
            "🍰",
            "🎁",
            "🎪",
            "🎭",
            "🎨",
            "🎯",
            "🎲",
            "🎮",
            "🎸",
            "🎹",
            "🎺",
            "🎻",
            "🎤",
            "🎧",
            "🎵",
            "🎶",
        ]
        random_repeats = random.randint(50, 200)
        for _ in range(random_repeats):
            print(" ".join(random.sample(party_emojis, random.randint(5, 15))))
    else:
        for i in range(number):
            print()
            punbot(prompt)
