# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "llamabot[all]==0.12.11",
#     "pydantic==2.11.7",
# ]
# ///

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="full")


@app.cell
def _():
    import llamabot as lmb
    from pydantic import BaseModel, Field
    import marimo as mo
    return BaseModel, Field, lmb, mo


@app.cell
def _(BaseModel, Field, lmb, mo):
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
        emoji: str = Field(description="single emoji for the whole pun.")
        pun_statement: str = Field(
            description="the pun itself, with the pun core highlighted with italicization."
        )
        explanation: str = Field(description="Why the pun is a pun.")

        def _display_(self):
            return mo.md(f"{self.emoji} {self.pun_statement}")


    bot = lmb.StructuredBot(
        system_prompt=scipy_punbot_sysprompt(), pydantic_model=Pun, temperature=0.9
    )
    return (bot,)


@app.cell
def _(bot):
    pun = bot("geodesics")
    pun
    return


if __name__ == "__main__":
    app.run()
