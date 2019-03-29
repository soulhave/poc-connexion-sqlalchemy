from dao.__base__ import BaseDao
from model.contact import Contact


class ContactDao(BaseDao):

    def save(self, contact):
        """
        Save Contact

        :type contact: contact
        """
        self.session.add(contact)
        self.session.commit()

        return contact

    def get(self):
        """
        Get all contacts from database
        :return:
        """
        return self.session.query(Contact).all()
