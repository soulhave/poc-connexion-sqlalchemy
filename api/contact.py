import uuid

from connexion import NoContent

from dao.contact import ContactDao
from model.contact import Contact

CONTACTS = {}


def search(limit):
    return ContactDao().get()


def get(id):
    contact = CONTACTS.get(id)
    return contact or ('Not found', 404)


def post(contact):
    if not contact:
        return 'Not found', 401

    contact_model = Contact.to_model(contact)
    contact_model = ContactDao().save(contact_model)

    return contact_model.to_dict()


def put(id, contact):

    if not id:
        return 'Empty contact id', 401

    if id not in CONTACTS:
        return 'Contact not found', 404

    contact['id'] = id
    CONTACTS[id] = contact

    return contact


def delete(id):
    if id in CONTACTS:
        del CONTACTS[id]
        return NoContent, 204
    else:
        return 'Contact not exist', 404
