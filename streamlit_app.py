import streamlit as st
#title
st.title("PPAS SUMMARY :- YOUTUBE VIDEO SUMMARIZER")
#subheader
st.subheader("get YouTube transcript and use AI to summerize YouTube videos in one click for free online with PPAS YouTube Summary tool")
st.subheader("want to summarize YouTube videos??")
youtube_link = st.text_input("Enter YouTube Video Link:")
if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
#thumbnail
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

with st.sidebar:
    st.header("features")
#with st.form("my_form"):
        #st.write("Inside the form")
       # st.text_input("text input")
        #st.text_area("text area")
       # st.button("submit form")
st.feedback("stars")

#st.balloons()
#with st.sidebar:
 #   with st.form(key='My Form'): 
  #  name=st.text_input("Name")
  #  email=st.text_input("E-mail")
   # st.form_submit_button("Sign up")
