#!usr/bin/python
import re
import sys
# open a file
try:
    filename = "/home/pavas/IIITD/NLP/Handa-Pavas-assign1-MT16040/Test Set 1.txt"
    fileobject = open(filename, "r")
except IOError:
    print 'Cannot open file %s for reading' % filename
    sys.exit(0)


with open(filename, 'r') as f:
    content = f.read()
    content = re.sub(r'"|;|\(|\)|:|,|-', '', content)
    content = re.sub(r'\n\n', ' ', content)
    content = re.sub(r'\n', ' ', content)
    word_list = content.split()
print "Number of words in an article are: ", len(word_list)

# Setting pointer to the start of the file
fileobject.seek(0)

# Counting "paragraphs" in an article

paragraph_count = 0
lines = fileobject.read().splitlines()
for i in range(1, len(lines)):
    line = lines[i]
    prev_line = lines[i - 1]
    if not line.split() and prev_line.split():
        paragraph_count += 1
if lines[-1].split():
    paragraph_count += 1
print "Number of paragraphs in an article are: ", paragraph_count

# Close opened file
fileobject.close()

# Counting "sentences" in an article
sentence_count = 0
with open(filename, 'r') as f:
    content = f.read()

    # removes all 'lines' in the file
    sentences = re.sub(r'\n(?<!\s\n)', '', content)

    # removes all 'blank lines' in the file
    sentences = re.sub(r'\n\s*\n', '\n', sentences)

    # removes all 'special characters except ? and ! and .' in the file
    sentences = re.sub(r'"|;|\(|\)|:|-', '', sentences)

    # classes any period after Mr/Mrs/Ms/Dr as ('not sentence boundaries')
    sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)

    # creates new line after exclamation mark
    sentences = re.sub(r'!\s([A-Z])', r'!\n\1', sentences)

    # creates new line after question mark
    sentences = re.sub(r'\?\s([A-Z])', r'?\n\1', sentences)

print "Number of sentences in an article are : ", len(sentences.split('\n'))
