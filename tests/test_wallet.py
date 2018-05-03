import unittest
import mock
from pprint import pprint
from bitshares import BitShares
from onegram.account import Account
from onegram.amount import Amount
from onegram.asset import Asset
from onegram.instance import set_shared_bitshares_instance
from onegrambase.operationids import getOperationNameForId

wif = "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"


class Testcases(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bts = BitShares(
            nobroadcast=True,
            # We want to bundle many operations into a single transaction
            bundle=True,
            # Overwrite wallet to use this list of wifs only
            wif=[wif]
        )
        self.bts.set_default_account("init0")
        set_shared_bitshares_instance(self.bts)
