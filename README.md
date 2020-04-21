# Summarization of instructional video transcripts using BERT

## Source Code:

We took the original BERTSUM paper and it is available at code\bertsumabs folder. The original source code had compliation errors when we compiled them in a Ubuntu VM machine. We made multiple changes for compliation. In addition we added the preprocessing logic and removed shuffle logic. Shuffle logic randomly shuffles the input datafiles. We wanted to train the model in a specific order.

#### Changes files:
For Preprocessing:
2 files have been changed - src/preprocess.py and src/prepro/data_builder.py
For shuffle logic:src/models/data_loader.py

## Preprocess the data

#### Step 1 Download Stories
Download and unzip the `stories` directories from [here](http://cs.nyu.edu/~kcho/DMQA/) for both CNN and Daily Mail. Put all  `.story` files in one directory (e.g. `../raw_stories`)

####  Step 2. Download Stanford CoreNLP
We will need Stanford CoreNLP to tokenize the data. Download it [here](https://stanfordnlp.github.io/CoreNLP/) and unzip it. Then add the following command to your bash_profile:
```
export CLASSPATH=/path/to/stanford-corenlp-full-2017-06-09/stanford-corenlp-3.8.0.jar
```
replacing `/path/to/` with the path to where you saved the `stanford-corenlp-full-2017-06-09` directory. 

####  Step 3. Sentence Splitting and Tokenization

```
python preprocess.py -mode tokenize -raw_path RAW_PATH -save_path TOKENIZED_PATH
```

* `RAW_PATH` is the directory containing story files (`../raw_stories`), `JSON_PATH` is the target directory to save the generated json files (`../merged_stories_tokenized`)


####  Step 4. Format to Simpler Json Files
 
```
python preprocess.py -mode format_to_lines -raw_path RAW_PATH -save_path JSON_PATH -n_cpus 1 -use_bert_basic_tokenizer false -map_path MAP_PATH
```

* `RAW_PATH` is the directory containing tokenized files (`../merged_stories_tokenized`), `JSON_PATH` is the target directory to save the generated json files (`../json_data/cnndm`), `MAP_PATH` is the  directory containing the urls files (`../urls`)

####  Step 5. Format to PyTorch Files
```
python preprocess.py -mode format_to_bert -raw_path JSON_PATH -save_path BERT_DATA_PATH  -lower -n_cpus 1 -log_file ../logs/preprocess.log
```

## Training the model
```
python train.py  -task abs -mode train -bert_data_path BERT_DATA_PATH -dec_dropout 0.2  -model_path ../models -sep_optim true -lr_bert 0.002 -lr_dec 0.2 -save_checkpoint_steps 1000 -batch_size 50 -train_steps 210000 -report_every 50 -accum_count 5 -use_bert_emb true -use_interval true -warmup_steps_bert 20000 -warmup_steps_dec 10000 -max_pos 512 -visible_gpus 0,1,2,3  -log_file ../logs/abs_bert_cnndmwikihow2
```
## Validating the model
```
python train.py -task abs -mode validate -batch_size 3000 -test_batch_size 500 -bert_data_path BERT_DATA_PATH -log_file ../logs/val_abs_bert_cnnhow2 -model_path ../models/ -sep_optim true -use_interval true -visible_gpus 1 -max_pos 512 -max_length 200 -alpha 0.95 -min_length 50 -result_path ../results -test_all -report_rouge False &
```

## Testing the model
```
python train.py -task abs -mode test -bert_data_path BERT_DATA_PATH  -batch_size 128 -test_batch_size 64 -log_file ../logs/testdata_run.log  -test_from ../models/model_step_210000.pt -sep_optim true -use_interval true -visible_gpus 0 -max_pos 512 -max_length 200 -alpha 0.95 -min_length 50 -result_path ../results -report_rouge True
```


