"""
Top-level API for scipyconference.

This module provides the main interface for generating SciPy conference puns.
It supports both community-curated puns from a JSONL file and LLM-generated puns
when the appropriate environment variables are set.

Examples::

    import scipyconference as conf
    import numpy as np

    # Generate 3 community-curated puns
    conf.create_puns(3)

    # Generate a party celebration with random emojis
    conf.create_puns(np.inf)
"""

from .puns import create_puns

__all__ = ["create_puns"]
