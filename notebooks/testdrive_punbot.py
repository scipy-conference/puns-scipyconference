# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "scipyconference==0.0.1",
# ]
# ///

import marimo

__generated_with = "0.14.5"
app = marimo.App(width="full")


@app.cell
def _():
    return


@app.cell
def _():
    from scipyconference.bots import punbot

    return (punbot,)


@app.cell
def _():
    user_prompt = """Generate a list of clever, funny, and diverse puns. Vary the topics, wordplay styles, and formats. You can include puns based on:
    	•	Word meanings or homophones (e.g., “I used to be a banker but I lost interest.”)
    	•	Pop culture references
    	•	Professions, hobbies, or fields of study (e.g., science, tech, music, literature)
    	•	Food, animals, or everyday objects
    	•	Literal vs. figurative language twists

    Keep each pun short and self-contained—ideally one-liners or short quips. Aim for a range of tones: groan-worthy dad jokes, sharp-witted wordplay, or unexpectedly clever turns of phrase. Avoid anything offensive or derogatory.

    Feel free to include a mix of original wordplay and light variations on classic puns."""
    return (user_prompt,)


@app.cell
def _(punbot, user_prompt):
    punbot(user_prompt)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
