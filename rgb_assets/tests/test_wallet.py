import json
import os

import pytest
import rgb_lib

from rgb_assets.config import SUPPORTED_NETWORKS, WalletConfig, get_config
from rgb_assets.tests.utils import fund_wallet
from rgb_assets.wallet_service import WalletService


def test_get_address(wallet):
    address = wallet.get_address()
    # Perform assertions to check if the address is not empty or None
    assert address is not None
    assert address != ""


def test_create_new_utxos(wallet):
    count = wallet.create_new_utxos(2)
    assert count >= 2


def test_get_new_blinded_utxo(wallet):
    blinded_utxo = wallet.get_new_blinded_utxo()
    assert blinded_utxo is not None
    assert type(blinded_utxo) == str
    assert blinded_utxo.startswith("utxob:")
    assert rgb_lib.BlindedUtxo(blinded_utxo)
