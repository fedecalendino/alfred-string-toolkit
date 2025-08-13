import sys

from pyflow import Workflow

import base
import cardano
import case
import hash
import info
import utils


TOOLKITS = {
    toolkit.name: {action.name: action for action in toolkit.actions}
    for toolkit in [base, case, hash, info, utils, cardano]
}


def run_action(workflow, name: str, action: callable, string: str):
    try:
        result = action(string)
    except:
        return None

    if result is None:
        return None

    title = result
    arg = result

    if "\n" in string:
        subtitle = " > {name}([{strings}])".format(
            name=name,
            strings=", ".join(map(lambda s: f"'{s}'", string.split("\n"))),
        )
    else:
        subtitle = " > {name}('{string}')".format(
            name=name,
            string=string,
        )

    workflow.new_item(
        title=title,
        subtitle=subtitle,
        arg=arg,
        valid=True,
    )


def main(workflow):
    toolkit = workflow.args[0].lower().strip()
    toolkit = TOOLKITS[toolkit]

    string = " ".join(workflow.args[1:]).strip()

    for name, action in toolkit.items():
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
