from test import documents, get_all_doc_owners_names, directories
from test import add_new_doc, delete_doc
import unittest

def docs_parse():
  docs = set()
  for item in documents:
    docs.add(item.get("name"))
  return docs

def shelf_parse():
  shelf = set()
  for item in directories:
    for number in (directories.get(item)):
      shelf.add(number)
  return shelf


class TestSec(unittest.TestCase):
  def setUp(self):
    pass
  def test_ap(self):
    self.assertEqual(get_all_doc_owners_names(), docs_parse())
  def test_a(self):
    add_new_doc()
    self.assertIn('', docs_parse())
  def test_d(self):
    delete_doc()
    self.assertNotIn('11-2', shelf_parse())
    
if __name__ == "__main__":
  unittest.main()
