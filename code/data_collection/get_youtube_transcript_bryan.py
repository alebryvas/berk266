import requests
import csv
import json
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi

data = pd.read_csv('data_with_index.csv')
transcript = []

with open('Youtube_Transcripts1.csv', 'w', newline='', encoding="utf-8") as csvfile:
    youtube = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for i in data.video_id:
    # a= ["LsCUCElZli0", "3AWDKiPGsdQ"]
    # for i in a:
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(i)
            sentences=[]

            for dict in transcript_list:
                sentences.append(dict['text'])
            # print('Sentences:', sentences)
            transcript.append(' '.join(sentences))

        except:
            transcript.append('No transcript')
            pass

    for i in range(len(transcript)):
        youtube.writerow([transcript[i]])
    # print('Transcript: ', transcript[1])


# with open('Youtube_Transcripts.csv', 'w', newline='') as csvfile:
#     youtube = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#     for i in range(len(transcript)):
#         youtube.writerow([transcript[i]])
