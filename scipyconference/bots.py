"""
Bots for the SciPy conference.

This module provides LLM-powered pun generation capabilities for the SciPy conference.
It uses llamabot to create structured puns with emojis and explanations.
"""

import os

from pydantic import BaseModel, Field

try:
    import llamabot as lmb

    LLAMABOT_AVAILABLE = True
except ImportError:
    LLAMABOT_AVAILABLE = False


def _create_punbot():
    """
    Create and configure the punbot instance for LLM-generated puns.

    :raises ImportError: If llamabot is not available
        and the user tries to use LLM features.
    :return: A configured llamabot instance for generating structured puns.
    :rtype: lmb.StructuredBot
    """
    if not LLAMABOT_AVAILABLE:
        raise ImportError(
            "llamabot is required for LLM-generated puns. "
            "Install it with: pip install scipyconference[llm]"
        )

    @lmb.prompt("system")
    def scipy_punbot_sysprompt():
        """You are an expert at mimicking Paul Ivanov,
        a well-known pun master at the SciPy conferences.

        Paul will inject award-winning puns in response
        to almost any theme that shows up during the lightning talks at SciPy.
        Most of what SciPy attendees talk about are python, linux, science, and more.
        Your mission is to generate puns in response to whatever theme is thrown at you.
        The puns should be coherent.
        """

    class Pun(BaseModel):
        """
        Structured pun model with emoji, statement, and explanation.

        This Pydantic model defines the structure for LLM-generated puns,
        ensuring consistent output format with emoji, pun text, and explanation.

        :ivar emoji: Single emoji that represents the theme or mood of the pun.
        :vartype emoji: str
        :ivar pun_statement: The pun itself,
            with the pun core highlighted with italicization.
        :vartype pun_statement: str
        :ivar explanation: Explanation of why the pun works and what makes it funny.
        :vartype explanation: str
        """

        emoji: str = Field(description="single emoji for the whole pun.")
        pun_statement: str = Field(
            description="the pun itself, with the pun core highlighted with italicization."  # noqa: E501
        )
        explanation: str = Field(description="Why the pun is a pun.")

        def __str__(self):
            """
            String representation of the pun.

            :return: The pun formatted as "emoji pun_statement".
            :rtype: str
            """
            return f"{self.emoji} {self.pun_statement}"

    bot = lmb.StructuredBot(
        system_prompt=scipy_punbot_sysprompt(),
        pydantic_model=Pun,
        temperature=0.9,
        api_key=os.getenv("PUNBOT_API_KEY", None),
        api_base=os.getenv("PUNBOT_API_BASE", None),
        model_name=os.getenv("PUNBOT_MODEL_NAME", "gpt-4.1"),
    )
    return bot


# Create punbot instance only if llamabot is available
if LLAMABOT_AVAILABLE:
    punbot = _create_punbot()
else:
    punbot = None
