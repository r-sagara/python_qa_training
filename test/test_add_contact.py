# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixt = Application()
    request.addfinalizer(fixt.destroy)
    return fixt


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", email=""))
    app.session.logout()


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="blba lba", lastname="baflbkaf", email="badfjbknlaf"))
    app.session.logout()




