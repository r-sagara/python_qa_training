# -*- coding: utf-8 -*-
from model.group import Group


"""def test_delete_all_groups_by_one(app):
    while app.group.count() > 0:
        app.group.delete_first_group()"""

def test_check_all_groups_and_delete(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.check_all_groups()
    app.group.delete_groups()

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()

