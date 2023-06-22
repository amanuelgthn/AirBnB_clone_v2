#!/usr/bin/python3
"""
unittest for console.py
"""
import os
from unittest.mock import patch, mock_open, MagicMock
from io import StringIO
import unittest
import models
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Testing the HBNBCommand class"""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "filetest.json")
        except FileNotFoundError:
            pass
        cls.hbnb = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        try:
            os.rename("filetest.json", "file.json")
        except FileNotFoundError:
            pass
        del cls.hbnb

    def setUp(self):
        """Set up the test"""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down the test"""
        try:
            os.remove("file.json")
            os.remove("filetest.json")
        except FileNotFoundError:
            pass

    def test_emptyline(self):
        """Testing the emptyline method"""
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.hbnb.emptyline()
            self.assertEqual(fake_stdout.getvalue(), "")
