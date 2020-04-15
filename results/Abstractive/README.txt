Abstractive Results

Date: 3/26/2020
Training Parameters:

Trained on:
How2Dataset - 5,000 samples
Wikihow - 10,000 samples
CNN/DM - All
Preprocessed: Alexandra, then Stanford CoreNLP
Batch Size: 800
Time to train: 3 days
Top 2 step checkpoints based on evaluation loss on validation set listed below.

1. results.21000
2. results.24000

Date: 4/2/2020
Training Parameters:

Trained on:
How2Dataset - All
Wikihow - All
CNN/DM - All
Preprocessed: Alexandra, then Stanford CoreNLP
Batch Size: 50
Time to train: 4 days

1. 195,000 candidate, gold file


Date: 4/3/2020
Training Parameters:

Trained on:
How2Dataset - All
Wikihow - All
CNN/DM - All
Preprocessed: Alexandra, then Stanford CoreNLP
Batch Size: 50
Time to train: 4 days

1. 210,000 candidate, gold and raw files
2. puncyoutuberesults.196000.candidate - 4/14/2020: This is our YouTube test with additional punctuation from spacey and '[ ]' bug removal.


Date; 4/15/2020
Testing: how2_100million
Files:
-----
Step 150000:
how2100millionresults.195000.candidate
how2100millionresults.195000.gold
how2100millionresults.195000.raw_src

Step 160000:
how2100millionresults.196000.candidate
how2100millionresults.196000.gold
how2100millionresults.196000.raw_src
