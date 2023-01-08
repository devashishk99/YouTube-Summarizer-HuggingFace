# YouTube Video Summarizer using HuggingFace 

## In this project, a summary is generated for any YouTube video given its url.

### The following steps are followed to get the required result:
+ Based on the video id, the youtube-transcript-api is used to extract the transcript/subtitles of the video.
+ On compilation of the entire transcript, it is divided into smaller chunks as LLMs can summarize text only upto certain threshold.
+ HuggingFace Pipeline model (sshleifer/distilbart-cnn-12-6) is used to generate the transcript summary

The code is also hosted on Streamlit Cloud and can be accessed using the link:
https://devashishk99-youtube-summarizer-huggingface-app-02ennk.streamlit.app/
