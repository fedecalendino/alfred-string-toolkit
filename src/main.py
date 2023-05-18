import sys

from pyflow import Workflow

import base
import case
import hash
import info
import utils

TOOLKITS = {toolkit.name: toolkit for toolkit in [base, case, hash, info, utils]}


def main(workflow):
    toolkit = workflow.args[0].lower().strip()
    toolkit = TOOLKITS[toolkit]

    string = " ".join(workflow.args[1:]).strip()

    found = 0

    for name, action in toolkit.actions.items():
        try:
            result = action(string)
        except Exception as exc:
            continue

        if result is None:
            continue

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

        found += 1

    if not found:
        workflow.new_item(
            title=f"No {toolkit.name} tools available",
            valid=False,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
