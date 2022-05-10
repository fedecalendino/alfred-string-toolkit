import sys

from workflow import Workflow

INFOS = [
    ("lenght", len),
]


def main(workflow):
    string = " ".join(workflow.args).lower().strip()

    for name, info in INFOS:
        value = str(info(string))

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
