# coding=utf-8
import sys

from workflow import Workflow

import stringcase


CONVERTERS = [
    ("lower case", stringcase.lowercase),
    ("upper case", stringcase.uppercase),
    ("title case", stringcase.titlecase),
    ("slug case", stringcase.spinalcase),
    ("snake case", stringcase.snakecase),
    ("const case", stringcase.constcase),
    ("path case", stringcase.pathcase),
    ("pascal case", lambda _: stringcase.pascalcase(_.replace(" ", "_"))),
]


def main(workflow):
    string = " ".join(workflow.args).lower().strip()

    for name, converter in CONVERTERS:
        value = converter(string)

        workflow.add_item(
            title=value,
            subtitle=" > {name}".format(
                name=name,
            ),
            arg=value,
            valid=True,
        )


if __name__ == u"__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
