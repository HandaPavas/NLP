#!usr/bin/python
import re
import sys
# open a file
try:
    filename = "/home/pavas/IIITD/NLP/Assignment 1/Development Set.txt"
    fileobject = open(filename, "r")
except IOError:
    print 'Cannot open file %s for reading' % filename
    sys.exit(0)

# Counting "words" in an article
wordcount = 0
lines = 0
for line in fileobject.readlines():
    if line != '\n':
        for i in range(1, len(line)):
            # extra spaces is taken care of
            if line[i] in " " and line[i - 1] not in " ":
                wordcount += 1
        wordcount += 1
# In-built function for splitting
#    word_list = words.split()
#    wordcount += len(word_list)

print "Number of words in an article are: ", wordcount

# Setting pointer to the start of the file
fileobject.seek(0)

# Counting "paragraphs" in an article
paragraph_count = 0
for line in fileobject.readlines():
    if line == '\n':
        paragraph_count += 1
print "Number of paragraphs in an article are: ", paragraph_count

# Setting pointer to the start of the file
fileobject.seek(0)

# Counting "sentences" in an article
sentence_count = 0
for content in fileobject.readlines():
    match_object = re.search("^(?!Mr|Ms|Mrs|Dr).*\.(\n|\s([A-Z]))|^([0-9].+\.\s[0-9]).*|(!|\?)\s([A-Z])", content)
    if match_object:
        sentence_count += 1
print "Number of sentences in an article are: ", sentence_count

# Close opened file
fileobject.close()
