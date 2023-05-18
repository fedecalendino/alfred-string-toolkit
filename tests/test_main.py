import json

from pyflow.testing import WorklowTestCase

from main import main


class TestMain(WorklowTestCase):
    def check(self, toolkit: str, string: str, expected: dict):
        envs = {}
        args = [toolkit, string]

        workflow = self.workflow(**envs)
        feedback = self.run_workflow(workflow, main, *args)

        found = {}

        for item in feedback["items"]:
            name = item["subtitle"].split("(")[0]
            found[name] = item["arg"]

        for name, value in expected.items():
            self.assertIn(name, found)
            self.assertEqual(value, found[name])

    def test_base(self):
        string = "dGVzdA=="
        expected = {
            " > b64.decode": "test",
            " > b64.encode": "ZEdWemRBPT0=",
            " > b32.encode": "MRDVM6TEIE6T2===",
            " > b16.encode": "6447567A64413D3D",
        }

        self.check("base", string, expected)

    def test_case(self):
        string = "This iS a Test"
        expected = {
            " > lowercase": "this is a test",
            " > uppercase": "THIS IS A TEST",
            " > titlecase": "This Is A Test",
            " > slugcase": "this-is-a-test",
            " > snakecase": "this_is_a_test",
            " > constcase": "THIS_IS_A_TEST",
            " > pathcase": "this/is/a/test",
            " > nospaces": "thisisatest",
        }

        self.check("case", string, expected)

    def test_hash(self):
        string = "this is a test"
        expected = {
            " > SHA3-512": "a68bf14c14f2f81a3ed31a849cc104555834af7dd7cc586829debd330641d9f799d5f261201a54802157f40aa3435b495f2f060831c28edd79cf0bf43938a3ac",
            " > SHA-512": "7d0a8468ed220400c0b8e6f335baa7e070ce880a37e2ac5995b9a97b809026de626da636ac7365249bb974c719edf543b52ed286646f437dc7f810cc2068375c",
            " > SHA3-256": "b69ced483a79e37e13372af7cdd9e6757542fe91be6e6d05b654fa19dab9056d",
            " > SHA-256": "2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c",
            " > MD5": "54b0c58c7ce9f2a8b551351102ee0938",
        }

        self.check("hash", string, expected)

    def test_info(self):
        string = "test 123"
        expected = {
            " > string": "test 123",
            " > digits": 3,
            " > letters": 4,
            " > lenght": 8,
            " > words": 2,
        }

        self.check("info", string, expected)

    def test_decode_jwt(self):
        string = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

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

        expected = {" > decode-jwt": json.dumps(decoded, indent=2)}

        self.check("utils", string, expected)
