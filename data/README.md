#Instruction on Data

We need two type of data to use this code, the stop word list and the word vector. Both of them can be download from the web. 

For stop word list, we obtain it from http://xpo6.com/wp-content/uploads/2015/01/stop-word-list.txt

For word vector, we obtain it from [GloVe](http://www-nlp.stanford.edu/projects/glove/). 
We use 6 version of word vector, which from:

* Wikipedia 2014 + Gigaword 5 (6B tokens): 
[50d](http://www-nlp.stanford.edu/data/glove.6B.50d.txt.gz) 
[100d](http://www-nlp.stanford.edu/data/glove.6B.100d.txt.gz)
[200d](http://www-nlp.stanford.edu/data/glove.6B.200d.txt.gz)
[300d](http://www-nlp.stanford.edu/data/glove.6B.300d.txt.gz)
* Common Crawl (42B tokens): [300d](http://www-nlp.stanford.edu/data/glove.42B.300d.txt.gz)
* Common Crawl (840B tokens): [300d](http://www-nlp.stanford.edu/data/glove.840B.300d.txt.gz) 

After get them, unzip them into the data directory.

It is no need to use all of the word vector. In our experiments, the [Common Crawl (42B tokens): 300d](http://www-nlp.stanford.edu/data/glove.42B.300d.txt.gz) is the best one.

UNIX-like users can obtain all the data via `download_data.sh`.