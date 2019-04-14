from nose.tools import *
from ex48.parser import *

def test_implied_subject():
    result = parse_sentence([('verb', 'run'), ('direction', 'west')])
    assert_equal(result.subject, 'player')
    result = parse_sentence([('verb', 'eat'), ('noun', 'bear')])
    assert_equal(result.subject, 'player')


def test_normal_sentence():
    result = parse_sentence([('noun', 'princess'),
                             ('verb', 'go'),
                             ('direction', 'down')])
    assert_equal(result.subject, 'princess')
    assert_equal(result.verb, 'go')
    assert_equal(result.object, 'down')
    result = parse_sentence([('noun', 'door'),
                             ('verb', 'kill'),
                             ('noun', 'cabinet')])
    assert_equal(result.subject, 'door')
    assert_equal(result.verb, 'kill')
    assert_equal(result.object, 'cabinet')


def test_stop_word_removal():
    result = parse_sentence([('stop', 'the'),
                             ('noun', 'bear'),
                             ('verb', 'eat'),
                             ('stop', 'the'),
                             ('noun', 'princess')])
    assert_equal(result.subject, 'bear')
    assert_equal(result.verb, 'eat')
    assert_equal(result.object, 'princess')


def test_parser_error():
    assert_raises(ParserError, parse_sentence, [])
    assert_raises(ParserError, parse_sentence,
                  [('verb', 'go'), ('verb', 'go')])
    assert_raises(ParserError, parse_sentence,
                  [('noun', 'princess'), ('noun','bear')])
