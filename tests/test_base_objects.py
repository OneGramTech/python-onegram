import unittest
from bitshares import BitShares, exceptions
from onegram.instance import set_shared_bitshares_instance
from onegram.account import Account
from onegram.committee import Committee


class Testcases(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bts = BitShares(
            nobroadcast=True,
        )
        set_shared_bitshares_instance(self.bts)

    def test_Committee(self):
        with self.assertRaises(
            exceptions.AccountDoesNotExistsException
        ):
            Committee("FOObarNonExisting")

        c = Committee("init0")
        self.assertEqual(c["id"], "1.5.0")
        self.assertIsInstance(c.account, Account)

        with self.assertRaises(
            exceptions.CommitteeMemberDoesNotExistsException
        ):
            Committee("nathan")
