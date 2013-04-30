#!/usr/bin/python

# TODO: unicode support?
# TODO: split out into a class
# TODO: use Liang hyphenation: http://nedbatchelder.com/code/modules/hyphenate.html
# TODO: use PyHyphen https://pypi.python.org/pypi/PyHyphen/0.9.3
# TODO: other splitting algorithms? (nltk?)

def smush (a, b):
    return [ ''.join(a[:len(a)-i]) + ''.join(b[j:])
            for i in xrange(len(a))
            for j in xrange(len(b)) ]

import sys

# TODO: more arg validation
if len(sys.argv) != 3:
    raise SystemExit("usage: %s <word> <word>" % (sys.argv[0]));

(pre, post) = sys.argv[1:]

words = smush(pre, post)
# TODO: nice formatting
print words
