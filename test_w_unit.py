from unittest import TestCase


class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_uppercase(self):
        assert 'python'.upper() == 'PYTHON'

    def test_reserved(self):
        assert list(reversed([1, 2, 3])) == [3, 2, 1]

    def test_always_fall(self):
        self.assertTrue(False)
