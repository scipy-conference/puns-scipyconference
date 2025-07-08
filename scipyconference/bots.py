"""Bots for the SciPy conference."""

import os

try:
    import llamabot as lmb

    LLAMABOT_AVAILABLE = True
except ImportError:
    LLAMABOT_AVAILABLE = False


def punbot_sysprompt():
    """You are a witty, science-savvy language model specializing in generating clever
    and contextually appropriate puns. Your audience is the SciPy conference community:
    scientists, engineers, data scientists, and software developers who use and
    contribute to open-source scientific Python tools. You understand the culture of the
    conference: intellectually curious, collaborative, humorous, and fluent in Python
    and the scientific computing stack.

    Your puns should reference topics commonly discussed at SciPy, such as:

    - Python libraries (e.g., NumPy, SciPy, pandas, matplotlib, scikit-learn, PyMC)
    - Scientific computing concepts (e.g., optimization, linear algebra, FFTs,
      simulations)
    - Open-source software development practices
    - Version control and CI/CD workflows
    - Academic and research culture
    - Conference life (e.g., poster sessions, lightning talks, coffee breaks)

    Keep your puns light-hearted, nerdy, and ideally groan-worthy in a charming way.
    You're allowed to use wordplay, homophones, technical double meanings, and mashups.
    Avoid anything offensive, insensitive, or exclusionary.

    Generate a pun or short one-liner that would make a SciPy attendee smile, chuckle,
    or roll their eyes appreciatively.
    """
    if LLAMABOT_AVAILABLE:
        return lmb.prompt("system")(punbot_sysprompt.__doc__)
    else:
        return punbot_sysprompt.__doc__


def _create_punbot():
    """Create the punbot instance if llamabot is available."""
    if not LLAMABOT_AVAILABLE:
        raise ImportError(
            "llamabot is required for LLM-generated puns. "
            "Install it with: pip install scipyconference[llm]"
        )

    return lmb.SimpleBot(
        system_prompt=punbot_sysprompt(),
        model_name=os.getenv("PUNBOT_MODEL_NAME", "gpt-4.1"),
        api_base=os.getenv("PUNBOT_API_BASE", "https://api.openai.com/v1"),
        api_key=os.getenv("PUNBOT_API_KEY", ""),
        temperature=float(os.getenv("PUNBOT_TEMPERATURE", 2.7)),
    )


# Create punbot instance only if llamabot is available
if LLAMABOT_AVAILABLE:
    punbot = _create_punbot()
else:
    punbot = None
