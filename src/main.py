import sys

from pyflow import Workflow, Item

import base
import case
import cardano
import hash
import info
import utils

TOOLS = [
    base,
    case,
    hash,
    info,
    utils,
    cardano,
]

TOOLKITS = {toolkit.name: toolkit for toolkit in TOOLS}


def run_action(workflow, name: str, action: callable, string: str):
    try:
        result = action(string)
    except:
        return None

    if result is None:
        return None

    if isinstance(result, tuple):
        title = result[0]
        arg = result[1]
    else:
        title = result
        arg = result

    workflow.new_item(
        title=title,
        subtitle=f" > {name}('{string}')",
        arg=arg,
        valid=True,
    )


def main(workflow):
    toolkit = workflow.args[0].lower().strip()
    toolkit = TOOLKITS[toolkit]

    string = " ".join(workflow.args[1:]).strip()

    for name, action in toolkit.actions.items():
        if isinstance(action, dict):
            for subname, subaction in action.items():
                run_action(workflow, f"{name}.{subname}", subaction, string)
        else:
            run_action(workflow, name, action, string)

    if len(workflow._items) == 0:
        workflow.new_item(
            title=f"No {toolkit.name} tools available",
            valid=False,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
