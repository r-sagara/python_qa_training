# -*- coding: utf-8 -*-
from model.group import Group


"""def test_delete_all_groups_by_one(app):
    while app.group.count() > 0:
        app.group.delete_first_group()"""

def test_check_all_groups_and_delete(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_all_groups()
    new_groups = app.group.get_group_list()

    assert 0 == len(new_groups)

def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)

