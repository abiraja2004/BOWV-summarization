# BOWV-summarization

BOWV-summarization is a automatic summarization system, which base on the bag of word vectors (BOWV) representation.

BOWV is a semantic representation, which can represent words, phrases, sentences, paragraphs and documents in a same vector space. In the BOWV space, we can approximately measure the semantic similarity with the distance between BOWV representations. We utilize it for extractive automatic summarization.

##Usage

    summarization.py [-k sentence-num] [-v word-vector-version] file
        file: the text file to be obtained a summary
	    sentence-num: the number of extracted sentence, default is 5
	    word-vector-version: 0-5, default is 0 ...
		    0	 glove.6B.50d.txt
		    1	 glove.6B.100d.txt
		    2	 glove.6B.200d.txt
		    3	 glove.6B.300d.txt
		    4	 glove.42B.300d.txt
		    5	 glove.840B.300d.txt

##Examples

    $python summarization.py example/dlbook-c1.txt

The automatic extractive summary of the [1st chapter](example/dlbook-c1.txt) in the [deep learning book from Yoshua Bengio](http://www-labs.iro.umontreal.ca/~bengioy/dlbook/).

>Deep learning is a particular kind of machine learning that achieves great power and flexibility by learning to represent the world as a nested hierarchy of concepts, with each concept defined in relation to simpler concepts.

>Fig 1 shows how a deep learning system can represent the concept of an image of a person by combining simpler concepts, such as corners and contours, which are in turn defined in terms of edges.

>Deep learning solves this central problem in representation learning by introducing representations that are expressed in terms of other, simpler representations.

>A major source of difficulty in many real-world artificial intelligence applications is that many of the factors of variation influence every single piece of data we are able to observe.

>The introduction of machine learning allowed computers to tackle problems involving knowledge of the real world and make decisions that appear subjective.

