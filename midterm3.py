import sys
import time
import twython
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

api_key, api_secret, access_token, token_secret = sys.argv[1:]

twitter = twython.Twython(api_key, api_secret, access_token, token_secret)

punct = [".", ",", "/", "//", "?","'", "!", "-", ":", ";", "=", "@", "<", ">", "#", "_", "(", ")"]

#function to strip punctuation
def strip(l1, l2):
	stripped = [w for w in l1 if w not in l2]
	return stripped

#get input
for line in sys.stdin:
	line = line.strip()
	if len(line) > 0:
		#search twitter based on input
		response = twitter.search(q=line, result_type='recent', count=4)
		if len(response['statuses']) > 0: 
			for tweet in response['statuses']:
				#if you get a response from twitter, store the status
				result = tweet['text']
				#tokenize it
				tokens = [word for sent in sent_tokenize(result) for word in word_tokenize(sent)]
				
				words = strip(tokens, punct)

				# VALLEY print all words, subtract to none, print one by one
				#for i in list(reversed(range(len(tokens)))) + range(len(tokens))[1:]:
				
				#PYRAMID print the status one word at a time, forwards and backwards
				for i in range(len(words)) + list(reversed(range(len(words))))[1:]:
					
					count = words[:i]
					print ' '.join(count)
					
		else:
			print line
		time.sleep(0.5)



