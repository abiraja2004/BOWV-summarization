import os, sys, getopt

non_char = '~!@#$%^&*()_+{}|:"<>?`1234567890-=[]\\;\',./\n'

# load the word vector
def load_dict(wv_file):
	# word vector
	wv_file = 'data/' + wv_file
	if not os.path.isfile(wv_file):
		print 'Cannot find file "' + wv_file + '"'
		print 'Get it following the instruction under the "data" directory'
		return None

	# stop word
	if not os.path.isfile('data/stop-word-list.txt'):
		print 'Cannot find file "data/stop-word-list.txt"'
		print 'Get it following the instruction under the "data" directory'
		return None
	f = open('data/stop-word-list.txt')
	lst = f.readlines()
	f.close()
	lst = [x.strip() for x in lst]

	f = open(wv_file)
	txt = f.readlines()
	f.close()
	the_dict = dict()

	for i in range(len(txt)):
		print '\rloading ',i,'/',len(txt),
		l = txt[i]
		ls = l.split()
		# filt out words with non-character 
		if any([(x in non_char) for x in ls[0]]):
			continue
		# filt out stop word
		if not (ls[0] in lst):
			the_dict[ls[0]] = [float(x) for x in ls[1:]]
	print '\r',
	return the_dict

# convert the word/phrase/sentence/paragraph/document 
# into the bag of word vectors (BOWV) representation.
def semantic_representation(s):
	n = 0
	v = [0]*len(word_dict[word_dict.keys()[0]])
	# split the input into words
	ss = s.split()
	# filt out non-character 
	
	ss = [filter(lambda x: not (x in non_char), x) for x in ss]
	# sum of all word vector in the input 
	for s in ss:
		if word_dict.has_key(s.lower()):
			if n == 0:
				v = word_dict[s.lower()]
			else:
				v = map((lambda x,y: x+y),v,word_dict[s.lower()])
			n += 1
	# mean of the sum
	if n > 1: 
		v = map(lambda x: x/n, v)
	return v

# get the BOWV of sentences
# input: the list of sentences
# output: a list of (BOWV, text)
def convert_sentence(sentence):
	vs = dict()
	for i in range(len(sentence)):
		s = sentence[i]
		v = semantic_representation(s)
		vs[i] = [v,s]
	return vs

# distance
def MSE(a,b):
	return reduce(lambda x,y: x+y, map(lambda x,y: (x-y)**2, a, b), 0)

# find the closest sentences to the document
def find_closest(sentence_vec,traget_vec):
	dist = {}

	for i in sentence_vec.keys():
		dist[i] = MSE(traget_vec,sentence_vec[i][0])

	t = sorted(dist.keys(), key=lambda k: dist[k])

	return t

# the document BOWV, it is the mean of the BOWV of sentences in the document
def gen_global_vec(sentence_vec):
	a = []
	for k in sentence_vec.keys():
		if len(a) == 0:
			a = [0 for x in sentence_vec[k][0]]
		for i in range(len(sentence_vec[k][0])):
			a[i] += sentence_vec[k][0][i]
	a = [x/len(sentence_vec) for x in a]
	return a

# split the document into sentences, split by '.' (period)
def split_sentence(txt):
	sentence = []
	for t in txt:
		t = t.strip()
		if len(t) > 0:
			ts = t.split('.')
			ts = filter((lambda s: len(s)>0), ts) 
			ts = [s.strip()+'.' for s in ts]
			sentence.extend(ts)
	return sentence

def main(fn,k):
	f = open(fn)
	txt = f.readlines()
	sentence = split_sentence(txt)

	sentence_vec = convert_sentence(sentence)
	global_vec = gen_global_vec(sentence_vec)

	t = find_closest(sentence_vec, global_vec)
	t = t[:k]
	t.sort(reverse=True)
	
	for i in t:
		print sentence_vec[i][1]

word_vector_version = [	'glove.6B.50d.txt',
						'glove.6B.100d.txt',
						'glove.6B.200d.txt',
						'glove.6B.300d.txt',
						'glove.42B.300d.txt',
						'glove.840B.300d.txt']

def usage():
	print '%s is a automatic summarization system'%sys.argv[0]
	print 'USAGE:'
	print '%s [-k sentence-num] [-v word-vector-version] file'%sys.argv[0]
	print '\t file: the text file to be obtained a summary'
	print '\t sentence-num: the number of extracted sentence, default is 5'
	print '\t word-vector-version: 0-5, default is 0 ...'
	for v in range(len(word_vector_version)):
		print '\t\t%d\t %s'%(v,word_vector_version[v])

if __name__ == '__main__':
	k = 5
	v = 0

	opt = getopt.getopt(sys.argv[1:],'hk:v:')
	for i in opt[0]:
		if i[0] == '-v':
			v = int(i[1])
		elif i[0] == '-k':
			k = int(i[1])
		elif i[0] == '-h':
			usage()
			sys.exit(0)

	if len(opt[1]) < 1:
		print 'input file is need.'
		usage()
		sys.exit(1)

	word_dict = load_dict(word_vector_version[v])
	if not word_dict:
		sys.exit(1)

	main(opt[1][0],k)
