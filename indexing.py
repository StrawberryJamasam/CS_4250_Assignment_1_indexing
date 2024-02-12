#-------------------------------------------------------------------------
# AUTHOR: Jane Barnett
# FILENAME: indexing.py
# SPECIFICATION: This code will read data from collection.csv and will
#                create a document-term matrix from each sentence.
# FOR: CS 4250- Assignment #1
# TIME SPENT: 4 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. 
# You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"i", "me", "my", "mine", "myself",
             "he", "him", "his", "himself",
             "she", "her", "hers", "herself",
             "it", "its", "itself",
             "you", "your", "yours", "yourselves",
             "we", "us", "our", "ours", "ourselves",
             "they", "them", "their", "theirs", "themselves",
             "for", "and", "nor", "but", "or", "yet", "so"}

modDocuments = []

for row, sentence in enumerate(documents):
  modDocuments.append(documents[row].split())
  for idx, word in enumerate(modDocuments[row]):
    checkTerm = True
    while checkTerm:
      if modDocuments[row][idx].lower() in stopWords:
        modDocuments[row].remove(word)
      else:
        checkTerm = False

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {"loves": "love", "loved": "love", "loving": "love", "luv": "love", "lov": "love", "lve": "love",
            "cats": "cat", "cts": "cat",
            "dogs": "dog", "dg": "dog", "dgs": "dog", "ogs": "dog"}

for row, sentence in enumerate(modDocuments):
  for idx, word in enumerate(modDocuments[row]):
    if modDocuments[row][idx] in stemming:
      modDocuments[row][idx] = stemming.get(modDocuments[row][idx])
      
#Identifying the index terms.
#--> add your Python code here
terms = []

for row, sentence in enumerate(modDocuments):
  for idx, word in enumerate(modDocuments[row]):
    if modDocuments[row][idx] not in terms:
      terms.append(modDocuments[row][idx])

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
numDocs = len(modDocuments)
docTermMatrix = [[0 for x in range(len(terms))] for y in range(numDocs)]

# tf
for row, sentence in enumerate(modDocuments):
  for idx, word in enumerate(modDocuments[row]):
    for i, term in enumerate(terms):
      if modDocuments[row][idx] == terms[i]:
        docTermMatrix[row][i] += 1

for row, sentence in enumerate(modDocuments):
  for idx, word in enumerate(docTermMatrix[row]):
    if docTermMatrix[row][idx] != 0:
      docTermMatrix[row][idx] = docTermMatrix[row][idx] / len(modDocuments[row])
 
# idf / tf-idf
for idx, word in enumerate(modDocuments[0]):
  count = 0
  for row, sentence in enumerate(modDocuments):
    if docTermMatrix[row][idx] != 0:
      count += 1
  idf = math.log10(numDocs/count)
  for row, sentence in enumerate(modDocuments):
    docTermMatrix[row][idx] = (docTermMatrix[row][idx] * idf)

#Printing the document-term matrix.
#--> add your Python code here
print()
print("      ", terms)
print()
for row, sentence in enumerate(docTermMatrix):
  print(" d", row, " ", sentence)
print()