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

from .puns import create_puns

__all__ = ["create_puns"]
