[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/abstractive-summarization-of-spoken/text-summarization-on-wikihow)](https://paperswithcode.com/sota/text-summarization-on-wikihow?p=abstractive-summarization-of-spoken)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/abstractive-summarization-of-spoken/abstractive-text-summarization-on-wikihow)](https://paperswithcode.com/sota/abstractive-text-summarization-on-wikihow?p=abstractive-summarization-of-spoken)

# Abstractive Summarization of Spoken and Written Instructions with BERT
KDD Converse 2020 paper:  http://arxiv.org/abs/2008.09676

## Source Code:

We took the original BERTSUM paper and it is available at code/bertsumabs folder. **This code is for EMNLP 2019 paper [Text Summarization with Pretrained Encoders](https://arxiv.org/abs/1908.08345)**. The original source code had compliation errors when we compiled them in a Ubuntu VM machine. We made multiple changes for compliation. In addition we added the preprocessing logic and removed shuffle logic. Shuffle logic randomly shuffles the input datafiles. We wanted to train the model in a specific order.

Furthermore, we used python scripts from downloading the youtube transcripts, descriptions, title etc and the source code for that is checked in to the code/datacollection/ folder
#### Changed files:
For Preprocessing:
2 files have been changed - code/bertsumabs/src/preprocess.py and code/bertsumabs/src/prepro/data_builder.py
For shuffle logic:code/bertsumabs/src/models/data_loader.py

## Preprocessed data
We have already preprocessed the data for CNN/Dailymail, WikiHow, How2 and How2 100million datasets and they are available in the repo at the below locations:

* CNN/DM - cnndm/

* How2 dataset - how2_all/ and how2dataset/

* WikiHow datasets - wikihow all/ and wikihow_train/

* How2 100million - 100million/



If you want to preprocess the data yourself, please check out our paper at the url https://github.com/alebryvas/berk266/blob/master/paper/draft/neurips_2020.pdf.

You can train/validate and test datasets from the above folders and apply them to the models directly using the code below.

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


