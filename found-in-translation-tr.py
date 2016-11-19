# coding: utf-8
import urllib
import urllib2
import json
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

PREFIX = 'O bir '
API_KEY = ''

phrase_file = open("input-tr.txt", "r")
phrases = [line.rstrip() for line in phrase_file.readlines()]
phrase_file.close()

# Change first letter to lowercase except if phrase is mixed case
phrases = [phrase[0].lower() + phrase[1:] if phrase[1:].islower() else phrase for phrase in phrases]

# Add prefix and full stop
phrases = [PREFIX + phrase + '.' for phrase in phrases]

# Prepare queries of suitable size
query = ''
queries = []
i = 0
for phrase in phrases:
	query += '&q=' + urllib.quote(phrase)
	#query = '&q=' + '&q='.join([urllib.quote(phrase) for phrase in phrases])
	i += 1
	if i == 49:
		i = 0
		queries.append(query)
		query = ''

queries.append(query)

# Perform queries using Google Translate Cloud API
translations = []
for query in queries:
	url = 'https://translation.googleapis.com/language/translate/v2?key=' + API_KEY + '&source=tr&target=en' + query
	try:
		response = urllib2.urlopen(url)
	except urllib2.URLError as e:
		print(e.read())
	except urllib2.HTTPError as e:
		print(e.read())
	response_json = response.read()
	response_parsed = json.loads(response_json)
	translations += response_parsed['data']['translations']

# Print the originals and the translations, marking female pronouns with an asterisk
translations = zip(phrases, translations)
for translation in translations:
	f = '* ' if translation[1]['translatedText'].lower()[0] == 's' else ''
	print(f + translation[0] + ' ' + translation[1]['translatedText'])

