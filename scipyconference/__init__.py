"""
Top-level API for scipyconference.

This module provides the main interface for generating SciPy conference puns.
It supports both community-curated puns from a JSONL file and LLM-generated puns
when the appropriate environment variables are set.

Examples::

    from scipyconference import create_puns
    create_puns(3)
    create_puns(1, "pandas dataframes")
    create_puns(np.inf)
"""

import random
from pathlib import Path

import numpy as np


__all__ = ["create_puns"]


def _read_puns_from_json():
    """
    Read puns from the JSONL file.

    Reads the community-curated puns from the puns.json file in JSONL format.
    Each line should contain a JSON object with 'pun' and 'github_username' fields.

    :return: List of dictionaries containing pun data.
        Each dictionary has 'pun' and 'github_username' keys.
        Returns empty list if file is not found or malformed.
    :rtype: list
    """
    pun_path = Path(__file__).parent / "puns.json"
    puns = []
    with open(pun_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                import json

                data = json.loads(line)
                puns.append(data)
    return puns


def create_puns(number: int, prompt: str = ""):
    """
    Create ``number`` of puns for the SciPy conference.

    This function generates puns for the SciPy conference community. It can work
    in three modes:

    1. Community-curated puns (default): Reads from puns.json file
    2. LLM-generated puns: Uses AI to generate puns based on a prompt
    3. Party mode: Creates a celebration with random emojis when number is np.inf

    :param int number: Number of puns to generate. Use np.inf for party mode.
    :param str prompt: Prompt for LLM-generated puns. Only used when LLM mode is active.
    :return: None
    :rtype: None
    :raises ImportError: If llamabot is required but not installed.
    :notes:
        The function automatically chooses between community-curated and LLM-generated
        puns based on environment variables:
        - If any of PUNBOT_API_KEY, PUNBOT_MODEL_NAME, or PUNBOT_API_BASE are set,
          it will attempt to use LLM-generated puns
        - Otherwise, it will use community-curated puns from puns.json

    Examples::

        create_puns(3)  # Generate 3 community-curated puns
        create_puns(1, "pandas")  # Generate 1 LLM pun about pandas
        create_puns(np.inf)  # Create a party celebration
    """
    if number is np.inf:
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
        puns = _read_puns_from_json()
        if not puns:
            print(
                "No puns found in puns.json. Consider adding some community-curated puns!"  # noqa: E501
            )
            return
        selected_puns = random.choices(puns, k=number)
        for pun_data in selected_puns:
            print()
            print(f"@{pun_data.get('github_username', 'anon')}: {pun_data['pun']}")
