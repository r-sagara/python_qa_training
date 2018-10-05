# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixt = Application()
    request.addfinalizer(fixt.destroy)
    return fixt


def test_add_group_case(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="GROUPNAME1", header="GROUPHEADER2", footer="GROUPFOOTER3"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
