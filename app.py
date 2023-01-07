from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
from pytube import YouTube

@st.experimental_memo
def load_summarizer():
    model = pipeline("summarization", device=0)
    return model

def get_video_metadata(video_url):
    yt = YouTube(video_url)
    st.image(yt.thumbnail_url)
    st.header(yt.title)

def get_video_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    return result

def generate_text_chunks(text):
    res = []
    num_iters = int(len(text)/1000)
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        res.append(text[start:end])
    return res


st.markdown("<h1 style='text-align: center; color: white;'>Youtube Video Summarizer</h1><br>", unsafe_allow_html=True)
st.markdown("View a summary of any Youtube video using its url.")

video_url  = st.text_input("Enter YouTube video URL")
video_id = video_url.split("=")[1]

button = st.button("Summarize")

with st.spinner("Generating Summary.."):
    if button and video_url:
        get_video_metadata(video_url)
        video_transcript = get_video_transcript(video_id)
        text_chunks = generate_text_chunks(video_transcript)
        res = summarizer(text_chunks)
        video_summary = ' '.join([summ['summary_text'] for summ in res])
        st.write(video_summary)

