import pytest


class TestDatedModel(object):
    @pytest.fixture
    def target(self):
        from beproud.django.basemodels.base import DatedModel
        return DatedModel

    def test_it(self, target):
        x = target()
        assert x


class TestBaseModel(object):
    @pytest.fixture
    def target(self):
        from beproud.django.basemodels.base import BaseModel
        return BaseModel

    def test_it(self, target):
        x = target()
        assert x


class TestBigAutoField(object):
    @pytest.fixture
    def target(self):
        from beproud.django.basemodels.fields import BigAutoField
        return BigAutoField

    def test_it(self, target):
        x = target()
        assert x
