import base64
import hashlib
import sys

from workflow import Workflow

HASHERS = [
    (
        "base64",
        lambda text: base64.b64encode(text).decode(),
    ),
    (
        "base16",
        lambda text: base64.b16encode(text).decode(),
    ),
    (
        "sha512",
        lambda text: hashlib.sha512(text).hexdigest(),
    ),
    (
        "sha384",
        lambda text: hashlib.sha384(text).hexdigest(),
    ),
    (
        "sha256",
        lambda text: hashlib.sha256(text).hexdigest(),
    ),
    (
        "sha224",
        lambda text: hashlib.sha224(text).hexdigest(),
    ),
    (
        "sha1",
        lambda text: hashlib.sha1(text).hexdigest(),
    ),
    (
        "md5",
        lambda text: hashlib.md5(text).hexdigest(),
    ),
]


def main(workflow):
    string = " ".join(workflow.args).lower().strip()
    encoded = string.encode()

    for name, hasher in HASHERS:
        value = hasher(encoded)

        workflow.add_item(
            title=value,
            subtitle=f" > {name.upper()}('{string}')",
            arg=value,
            valid=True,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
