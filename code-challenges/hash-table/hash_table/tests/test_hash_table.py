from hash_table.hash_table import *



def test_add():
  test=HashTable()
  test.add('ahmad',555)
  assert test.contains('ahmad')==True
