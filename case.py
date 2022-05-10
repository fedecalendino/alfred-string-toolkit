import sys

import stringcase
from workflow import Workflow

CONVERTERS = [
    ("lower case", stringcase.lowercase),
    ("upper case", stringcase.uppercase),
    ("title case", stringcase.titlecase),
    ("slug case", stringcase.spinalcase),
    ("snake case", stringcase.snakecase),
    ("const case", stringcase.constcase),
    ("path case", stringcase.pathcase),
    ("no spaces", lambda string: string.replace(" ", "")),
]


def main(workflow):
    string = " ".join(workflow.args).lower().strip()

    for name, converter in CONVERTERS:
        value = converter(string)

        if name != "lower case" and value == string:
            continue

        workflow.add_item(
            title=value,
            subtitle=f" > {name}('{string}')",
            arg=value,
            valid=True,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
