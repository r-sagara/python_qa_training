# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_creation"))
    app.group.modify_first_group(Group(name="GROUPNAME2"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_creation"))
    app.group.modify_first_group(Group(header="GROUPHEADER2"))