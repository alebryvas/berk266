'''
This code is used to create article and summary files from the csv file.
The output of the file will be a directory of text files representing seoarate articles and their summaries.
Each summary line starts with tag "@summary" and the article is followed by "@article".
'''
import pandas as pd
import os
import re

# read data from the csv file (from the location it is stored)
Data = pd.read_csv(r'cleaned_transcripts.csv')
Data = Data.astype(str)
rows, columns = Data.shape

# create a file to record the file names. This can be later used to divide the dataset in train/dev/test sets
title_file = open('titles.txt', 'wb')

# The path where the articles are to be saved
path = "articles"
if not os.path.exists(path): os.makedirs(path)

# go over the all the articles in the data file
for row in range(rows):
    abstract = Data.loc[row,'summary']      # headline is the column representing the summary sentences # Bryan changed from ix to loc
    article = Data.loc[row,'transcript']           # text is the column representing the article

    #  a threshold is used to remove short articles with long summaries as well as articles with no summary
    if len(article) > 20:

        # remove extra commas in abstracts
        abstract = abstract.replace(".,",".")
        abstract = abstract.encode('utf-8')
        # remove extra commas in articles
        article = article.replace('-', ' ')
        article = article.replace('[Music]', ' ')
        article = article.replace('[Applause]', ' ')
        article = re.sub(r'[.]+[\n]+[,]',".\n", article)
        article = article.encode('utf-8')


        # a temporary file is created to initially write the summary, it is later used to separate the sentences of the summary
        with open('temporaryFile.txt','wb') as t:
            t.write(abstract)

        # file names are created using the alphanumeric charachters from the article titles.
        # they are stored in a separate text file.
        filename = Data.loc[row,'title']
        filename = "".join(x for x in filename if x.isalnum())
        filename1 = filename + '.txt'
        filename = filename.encode('utf-8')
        title_file.write(filename+b'\n')


        with open(path+'/'+filename1,'wb') as f:
            # summary sentences will first be written into the file in separate lines
            with open('temporaryFile.txt','r', encoding="utf8") as t: # Bryan added encoding
                for line in t:
                    line=line.lower()
                    if line != "\n" and line != "\t" and line != " ":
                        f.write(b'@summary'+b'\n')
                        f.write(line.encode('utf-8'))
                        f.write(b'\n')

            # finally the article is written to the file
            f.write(b'@article' + b'\n')
            f.write(article)

title_file.close()
