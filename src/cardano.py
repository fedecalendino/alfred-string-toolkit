import re

CARDANO_ASSET_ID_REGEX = r"^[a-f0-9]{56}[a-fA-F0-9]+$"


def is_cardano_asset_id(string: str) -> bool:
    return bool(re.match(CARDANO_ASSET_ID_REGEX, str(string)))


def cardano_policy_id(string: str) -> str:
    if not is_cardano_asset_id(string):
        return None

    return string[:56]


def cardano_asset_name(string: str) -> str:
    if not is_cardano_asset_id(string):
        return None

    return string[56:]


def cardano_decoded_asset_name(string: str) -> str:
    if not is_cardano_asset_id(string):
        return None

    try:
        return bytes.fromhex(string[56:]).decode()
    except UnicodeDecodeError:
        return None


name = "cardano"

actions = {
    "policy_id": cardano_policy_id,
    "asset_name": cardano_asset_name,
    "decoded_asset_name": cardano_decoded_asset_name,
}
