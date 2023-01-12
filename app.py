from transformers import pipeline #the holy grail of all pre-trained LLMs
from youtube_transcript_api import YouTubeTranscriptApi #the python API which allows you to get the transcripts/subtitles for a given YouTube video 
import streamlit as st #open-source framework to build quick webapps
from pytube import YouTube #library for downloading YouTube Videos
import re #provides regular expression matching operations

#runs the function and stores the model in a local cache
#helpful when working large ml models
@st.cache(allow_output_mutation=True)
def load_summarizer():
    model = pipeline("summarization")
    return model

#takes the video url as input and returns video id along with displaying thumbnail & title of video
def get_video_metadata(url):
    yt = YouTube(url)
    st.image(yt.thumbnail_url)
    st.header(yt.title)
    id = extract.video_id(url)
    return id

#generates transcript using the api 
def get_video_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    return result

#breaks down large text blob into chunks so LLMs have limited processing capability
def generate_text_chunks(text):
    res = []
    num_iters = int(len(text)/1000)
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        res.append(text[start:end])
    return res

#execution starts from here-
st.markdown("<h1 style='text-align: center; color: white;'>Youtube Video Summarizer</h1><br>", unsafe_allow_html=True)
st.markdown("View a summary of any Youtube video using its url.")

#user input of video url is stored
video_url = st.text_input("Enter YouTube video URL", "https://www.youtube.com/watch?v=yxsoE3jO8HM")

#flag to toggle 'Summary' button based on validity of url
summ_flag = False

#check if video url is valid and matches the pattern using regex
url_regex = r"^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+"
url_check = re.search(url_regex,video_url)
if url_check == None:
    st.error('Please provide a valid YouTube url!', icon="🚨")
    summ_flag = True

#invokes the task to generate summary
button = st.button("Summarize", disabled=summ_flag)

#loads the pipeline model
summarizer = load_summarizer()

#displays spinner as a feedback to user by the time summary is being generated
with st.spinner("Generating Summary.."):
    if button and video_url:
        video_id = get_video_metadata(video_url)
        video_transcript = get_video_transcript(video_id)
        text_chunks = generate_text_chunks(video_transcript)
        res = summarizer(text_chunks)
        video_summary = ' '.join([summ['summary_text'] for summ in res]) #summaries of all the chunks are put together
        st.write(video_summary) #displays the final summary

