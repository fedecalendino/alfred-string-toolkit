import sys

from lorem_text import lorem
from workflow import Workflow

CONVERTERS = [
    (
        "paragraph",
        "2 to 4 sentences, first one is always 'lorem ipsum dolor sit amet...'",
        lambda count: lorem.paragraphs(count),
    ),
    (
        "sentence",
        "ends in either a period or question mark, and commas are added at random.",
        lambda count: "\n".join(lorem.sentence() for _ in range(count)),
    ),
    (
        "word",
        "list of words separated by a single space.",
        lambda count: lorem.words(count),
    ),
]


def main(workflow):
    try:
        count = int(" ".join(workflow.args).lower().strip())

        if not 0 < count < 1001:
            raise ValueError()
    except ValueError:
        raise Exception("Expected an integer between 1 and 1000.")

    for name, description, converter in CONVERTERS:
        value = converter(count)

        workflow.add_item(
            title=value,
            subtitle=f"{count} {name}{('s', '')[count == 1]}: ".upper() + description,
            arg=value,
            valid=True,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
