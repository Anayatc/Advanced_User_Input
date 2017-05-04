from nose.tools import *
from ex48 import lexicon
from ex48 import parser


def test_sentence_obj():
    s = parser.Sentence(('noun', 'bear'), ('verb', 'eat'), ('number', 1), ('noun', 'door'))
    assert_equal(s.subject, 'bear')
    assert_equal(s.verb, 'eat')
    assert_equal(s.number, 1)
    assert_equal(s.object, 'door')
    assert_equal(s.to_tuple(), ('bear', 'eat', 1, 'door'))