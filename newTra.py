import streamlit as st
from dotenv import load_dotenv

# load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

# transcript_list = YouTubeTranscriptApi.list_transcripts('Y9Um-8nPnVQ')
# for transcript in transcript_list:
#      print(transcript.fetch())
#      german = transcript.translate('mr').fetch()
#      print(transcript.translate('mr').fetch())

# new things added above it 
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """



## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):

    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text


st.title("PPAS Summary :- YouTube Transcript to Detailed Notes Converter")
#subheader
st.subheader("get YouTube transcript and use AI to summerize YouTube videos in one click for free online with PPAS YouTube Summary tool")
st.subheader("want to summarize YouTube videos??")
youtube_link = st.text_input("Enter YouTube Video Link:")


if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
# thumbnail
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)
    
st.subheader("Why Use YouTube Video Summerizer?")
st.markdown("    1) Fast And Accurate")
st.markdown("    2) Free Of charge")
st.markdown("    3) Multilanguage Support")  

st.subheader("How It Works")
st.write("1)  Using PPAS YouTube Video Summerizer is a breeze. Follow these simple steps toget your transcript in no time")
st.write("2)  Click Get Detailed Notes: Hit the button, and we will swiftly process the video to produce a text-based transcript")
st.write("3) Copy and Use: With just a click, the transcript will be copied to your clipboard")


if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(transcript_text)
        # st.markdown("## Detailed Notes in Marathi :")
        # st.write(german)
        # Fetch the Marathi translation (YouTube Transcript API)
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        german = None
        for transcript in transcript_list:
                german = transcript.translate('mr').fetch()

        if german:
            # Concatenate the Marathi transcript into a single paragraph
            marathi_text = " ".join([line['text'] for line in german])
            st.markdown("## Detailed Notes in Marathi:")
            st.write(marathi_text)
        else:
            st.write("Marathi translation not available for this video.")
   




