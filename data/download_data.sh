#!/bin/bash

# stop word
wget http://xpo6.com/wp-content/uploads/2015/01/stop-word-list.txt

# word vector
wget http://www-nlp.stanford.edu/data/glove.6B.50d.txt.gz
wget http://www-nlp.stanford.edu/data/glove.6B.100d.txt.gz
wget http://www-nlp.stanford.edu/data/glove.6B.200d.txt.gz
wget http://www-nlp.stanford.edu/data/glove.6B.300d.txt.gz
wget http://www-nlp.stanford.edu/data/glove.42B.300d.txt.gz
wget http://www-nlp.stanford.edu/data/glove.840B.300d.txt.gz

gunzip glove.6B.50d.txt.gz
gunzip glove.6B.100d.txt.gz
gunzip glove.6B.200d.txt.gz
gunzip glove.6B.300d.txt.gz
gunzip glove.42B.300d.txt.gz
gunzip glove.840B.300d.txt.gz
