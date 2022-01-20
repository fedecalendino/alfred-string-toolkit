# coding=utf-8
import sys

from workflow import Workflow

import stringcase


CONVERTERS = [
    ("const case", stringcase.constcase),
    ("lower case", stringcase.lowercase),
    ("pascal case", lambda _: stringcase.pascalcase(_.replace(" ", "_"))),
    ("path case", stringcase.pathcase),
    ("slug case", stringcase.spinalcase),
    ("snake case", stringcase.snakecase),
    ("title case", stringcase.titlecase),
    ("upper case", stringcase.uppercase),
]


def main(workflow):
    string = " ".join(workflow.args).strip()

    for name, converter in CONVERTERS:
        value = converter(string)

        workflow.add_item(
            title=value,
            subtitle="{name} --> {converted}".format(
                name=name,
                converted=converter(name),
            ),
            arg=value,
            valid=True,
        )


if __name__ == u"__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
