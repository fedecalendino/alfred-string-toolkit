# coding=utf-8
import sys

from workflow import Workflow

CONVERTERS = {
    "lower case": lambda string: string.lower(),
    "Title Case": lambda string: string.title(),
    "UPPER CASE": lambda string: string.upper(),
}


def main(workflow):
    string = " ".join(workflow.args).lower()

    for name in sorted(CONVERTERS, key=lambda n: n.lower()):
        converter = CONVERTERS[name]
        value = converter(string)

        workflow.add_item(
            title=value,
            subtitle=name,
            arg=value,
            valid=True,
        )


if __name__ == u"__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
