import pytest


class TestDatedModel(object):
    @pytest.fixture
    def target(self):
        from beproud.django.basemodels.base import DatedModel
        return DatedModel

    def test_it(self, target):
        x = target()
        assert x
