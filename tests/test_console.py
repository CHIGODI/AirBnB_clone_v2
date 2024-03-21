#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.state import State
from models import storage
from console import HBNBCommand
from models import storage
from unittest.mock import patch
from io import StringIO
import MySQLdb
from os import environ

db_url = {
    'user': environ.get('HBNB_MYSQL_USER'),
    'passwd': environ.get('HBNB_MYSQL_PWD'),
    'db': environ.get('HBNB_MYSQL_DB'),
    'host': environ.get('HBNB_MYSQL_HOST')
}


class test_console(unittest.TestCase):
    """ Class to test the HBNBCommand console"""

    def setUp(self):
        """ Set up test environment """
        self.conn = MySQLdb.connect(**db_url)
        self.cur = self.conn.cursor()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            self.cur.close()
            self.onn.close()
        except Exception:
            pass

    def test_do_create(self):
        """Tests if an object is created by the console"""
        printed_id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Carlifonia" id="1xef"')
            printed_id = f.getvalue().strip()

        self.cur.execute(
            'SELECT id FROM states;'
        )
        stored_state = self.cur.fetchone()[0]

        self.assertIn('1xef', printed_id)
        self.assertEqual('1xef', stored_state)
        storage.delete()
        storage.save()

    def test_do_all(self):
        """Tests all in the cmd """
        state_1 = State(name="Carlifonia")
        state_2 = State(name="New York")

        state_1.save()
        state_2.save()

        output_dict = None
        with patch('sys.stdout', new=StringIO()) as o:
            HBNBCommand().onecmd('all State')
            output_dict = o.getvalue().strip()
        self.assertIn('Carlifonia', output_dict)
        self.assertIn('New York', output_dict)
        state_1.delete()
        state_2.delete()
        storage.save()
