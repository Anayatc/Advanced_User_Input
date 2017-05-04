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


def test_peek():
    word_list = lexicon.scan('princess')
    assert_equal(parser.peek(word_list), 'noun')
    assert_equal(parser.peek(None), None)


def test_match():
    word_list = lexicon.scan('princess')
    assert_equal(parser.match(word_list, 'noun'), ('noun', 'princess'))
    assert_equal(parser.match(word_list, 'stop'), None)
    assert_equal(parser.match(None, 'noun'), None)


def test_skip():
    word_list = lexicon.scan('bear eat door')
    assert_equal(word_list, [('noun', 'bear'), ('verb', 'eat'), ('noun', 'door')])
    parser.skip(word_list, 'noun')
    assert_equal(word_list, [('verb', 'eat'), ('noun', 'door')])


def test_parse_verb():
    word_list = lexicon.scan('it eat door')
    assert_equal(parser.parse_verb(word_list), ('verb', 'eat'))
    word_list = lexicon.scan('bear eat door')
    assert_raises(parser.ParserError, parser.parse_verb, word_list)