# -*- coding: utf-8 -*-

from .context import lserver

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        lserver.hmm()


if __name__ == '__main__':
	unittest.main()