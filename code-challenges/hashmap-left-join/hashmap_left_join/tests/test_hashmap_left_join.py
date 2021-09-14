from hashmap_left_join.hashmap_left_join import *
import pytest

def test_happy_path(prepared_hash1,prepared_hash2):

    actual=left_join(prepared_hash1,prepared_hash2)
    expected=[['outfit', 'grap', None], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse']]
    assert actual==expected



def test_edge_case():
    hashmap1 = Hashtable()
    hashmap2 = Hashtable()

    actual=left_join(hashmap1,hashmap2)
    expected='The hashtable are empty'
    assert actual==expected


def test_expected_failure(prepared_hash1):
    hashmap2 = Hashtable()
    hashmap2.add('hi', 'averse')
    hashmap2.add('wrath', 'delight')
    hashmap2.add('diligent', 'idle')
    hashmap2.add('guide', 'follow')
    hashmap2.add('flow', 'jam') 
    actual=left_join(prepared_hash1,hashmap2)
    expected=[['wrath', 'anger', 'delight'], ['outfit', 'grap', None], ['diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]
    assert actual!=expected


@pytest.fixture
def prepared_hash1():
    hashmap1 = Hashtable()
    hashmap1.add('fond', 'enamored')
    hashmap1.add('wrath', 'anger')
    hashmap1.add('diligent', 'employed')
    hashmap1.add('outfit', 'grap')
    hashmap1.add('guide', 'usher')
    return hashmap1

@pytest.fixture
def prepared_hash2():
    hashmap2 = Hashtable()
    hashmap2.add('fond', 'averse')
    hashmap2.add('wrath', 'delight')
    hashmap2.add('diligent', 'idle')
    hashmap2.add('guide', 'follow')
    hashmap2.add('flow', 'jam')
    return hashmap2