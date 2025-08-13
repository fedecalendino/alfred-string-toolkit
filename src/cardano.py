import re

from classes import Action

CARDANO_ASSET_ID_REGEX = r"^[a-f0-9]{56}[a-fA-F0-9]+$"


def is_cardano_asset_id(string: str) -> bool:
    return bool(re.match(CARDANO_ASSET_ID_REGEX, str(string)))


class CardanoPolicyId(Action):
    def __init__(self):
        super().__init__("policy_id")

    def __call__(self, string: str) -> str:
        if not is_cardano_asset_id(string):
            return None

        return string[:56]


class CardanoAssetName(Action):
    def __init__(self):
        super().__init__("asset_name")

    def __call__(self, string: str) -> str:
        if not is_cardano_asset_id(string):
            return None

        return string[56:]


class CardanoDecodedAssetName(Action):
    def __init__(self):
        super().__init__("decoded_asset_name")

    def __call__(self, string: str) -> str:
        if not is_cardano_asset_id(string):
            return None

        try:
            return bytes.fromhex(string[56:]).decode()
        except UnicodeDecodeError:
            return None


name = "cardano"

actions = [
    CardanoPolicyId(),
    CardanoAssetName(),
    CardanoDecodedAssetName(),
]
