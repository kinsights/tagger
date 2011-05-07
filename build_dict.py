#!/usr/bin/env python


# Copyright (C) 2011 by Alessandro Presta

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE


'''
Usage: build_dict.py -o <output file> -s <stopwords file> <list of files>
'''

import collections
import getopt
import math
import pickle
import sys

from tagger import Reader, Stemmer


if __name__ == '__main__':

    try:
        options = getopt.getopt(sys.argv[1:], 'o:s:')
        output_file = options[0][0][1]
        stopwords_file = options[0][1][1]
        corpus = options[1]
    except:
        print __doc__
        exit(1)
    
    reader = Reader()
    stemmer = Stemmer()

    print 'Reading stopwords... '
    with open(stopwords_file, 'r') as f:
        stopwords = reader(f.read())
        
    words = []

    print 'Reading corpus... '
    for doc in corpus:
        with open(doc, 'r') as f:
            words += reader(f.read())

    print 'Processing tags... '
    words = map(stemmer, words)
    stopwords = map(stemmer, stopwords)

    term_count = collections.Counter(words)
    total_count = len(words)

    dictionary = {}

    print 'Building dictionary... '
    for w, cnt in term_count.iteritems():
        dictionary[w.stem] = 1.0 - \
            math.log(float(cnt) + 1) / math.log(total_count)

    for w in stopwords:
        dictionary[w.stem] = 0.0

    print 'Saving dictionary... '
    with open(output_file, 'wb') as f:
        pickle.dump(dictionary, f, -1)        

