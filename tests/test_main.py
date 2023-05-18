import json

from pyflow.testing import WorklowTestCase

from main import main


class TestMain(WorklowTestCase):
    def test_decode_jwt(self):
        jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

        decoded = {
            "header": {
                "alg": "HS256",
                "typ": "JWT",
            },
            "payload": {
                "sub": "1234567890",
                "name": "John Doe",
                "iat": 1516239022,
            },
            "signature": "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
        }

        envs = {}
        args = ["utils", jwt]

        workflow = self.workflow(**envs)
        feedback = self.run_workflow(workflow, main, *args)

        for item in feedback["items"]:
            if item["subtitle"].startswith(" > decode-jwt"):
                break
        else:
            self.fail("item for decode jwt not found")

        self.assertEqual(item["title"], json.dumps(decoded))
        self.assertEqual(item["arg"], json.dumps(decoded, indent=2))
