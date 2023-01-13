# YouTube Video Summarizer using HuggingFace and Youtube Transcript API

## In this project, a summary is generated for any YouTube video given its url.

## What is HuggingFace :hugs: 
> Hugging Face is an AI community and Machine Learning platform that provides immediate access to over 20,000 pre-trained models based on the state-of-the-art transformer architecture. These models can be applied to:
> + Text 
> + Speech 
> + Vision 
> + Reinforcement Learning transformers. 

## Why HuggingFace Pipeline?
The pipeline() makes it simple to use any model from the Hub for inference on any language, computer vision, speech, and multimodal tasks. That way, a person with no experience of a specific modality or the underlying code behind the models, can still use them with the pipeline()! 

## Steps followed to get the required result:
- [x] Based on the video id, the youtube-transcript-api is used to extract the transcript/subtitles of the video.
- [x] On compilation of the entire transcript, it is divided into smaller chunks as LLMs can summarize text only upto certain threshold.
- [x] HuggingFace Pipeline model (sshleifer/distilbart-cnn-12-6) is used to generate the transcript summary

The code is also hosted on Streamlit Cloud and can be accessed using the link: <br/>
https://devashishk99-youtube-summarizer-huggingface-app-02ennk.streamlit.app/
