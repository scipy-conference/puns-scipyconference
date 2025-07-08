"""Top-level API for scipyconference.

This is the file from which you can do:

    from scipyconference import some_function

Use it to control the top-level API of your Python data science project.
"""

import os
import random
from pathlib import Path

import numpy as np

from .bots import punbot

__all__ = ["create_puns"]


def _read_puns_from_json():
    """Read puns from the JSONL file."""
    pun_path = Path(__file__).parent / Path("puns.json")
    puns = []
    try:
        with open(pun_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    import json

                    data = json.loads(line)
                    puns.append(data)
        return puns
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _should_use_llm():
    """Check if we should use LLM-generated puns based on environment variables."""
    return any(
        [
            os.getenv("PUNBOT_API_KEY"),
            os.getenv("PUNBOT_MODEL_NAME"),
            os.getenv("PUNBOT_API_BASE"),
        ]
    )


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
        if _should_use_llm():
            # Use LLM-generated puns
            if punbot is None:
                print("llamabot is required for LLM-generated puns.")
                print("Install it with: pip install scipyconference[llm]")
                print(
                    "Or use community-curated puns by not setting PUNBOT_* environment variables."  # noqa: E501
                )
                return

            for i in range(number):
                print("🤖🐍:")
                punbot(prompt)
        else:
            # Use community-curated puns from JSONL file
            puns = _read_puns_from_json()
            if not puns:
                print(
                    "No puns found in puns.json. Consider adding some community-curated puns!"  # noqa: E501
                )
                return

            # Randomly sample puns, with replacement if needed
            selected_puns = random.choices(puns, k=number)

            for pun_data in selected_puns:
                print()
                print(f"@{pun_data['github_username']}: {pun_data['pun']}")
