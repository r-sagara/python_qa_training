# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", email=""))


def test_add_contact(app):
    app.contact.create(Contact(firstname="blba lba", lastname="baflbkaf", email="badfjbknlaf"))




