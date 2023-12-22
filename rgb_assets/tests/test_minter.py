import pytest
import rgb_lib
import pytest 
from rgb_assets.tests.utils import fund_wallet

from rgb_assets.minter import NftMintingService


def test_mint_from_file(minter):
    pass 


def test_mint(minter, nft_demo):
    # Test the mint a CFA asset
    fund_wallet(minter)
    assets = minter.get_cfa_assets()
    # There should be no assets yet
    assert len(assets) == 0 
    asset_id = minter.mint_nft(nft_demo)
    assets = minter.get_cfa_assets()
    assert len(assets) > 0 
    assert asset_id is not None 
    assert type(asset_id) == str
    assert asset_id.startswith("rgb:")


def test_send_nft(minter, nft_demo):
    # Mint a CFA asset and try to send it to a new utxob
    fund_wallet(minter)
    blinded_utxo = minter.get_new_blinded_utxo()
    asset_id = minter.mint_nft(nft_demo)
    txid = minter.send_nft(blinded_utxo, asset_id)
    assert txid is not None 
    assert type(txid) == str
 