import streamlit as st

# page_bg_img= """
# <style>
# [data-testeid="AppViewerContainer"]{
#         background-image: url("https://images.app.goo.gl/Qo468P2jpDiiMfaH9")
#         background-size: cover;
#     }
#     </style>
#     """

# Custom CSS
st.markdown("""
    <style>
    
        # /* Main container styling */
        # .container {
        #     max-width: 1000px;
        #     margin: auto;
        #     padding: 20px;
        #     text-align: center;
        #     background-color: #f8f9fc;
        #     border-radius: 8px;
        # }


        /* Header styling */
        h1 {
            font-size: 2.5em;
            color: White;
        }
        
        .header {
            font-size: 1.2em;
            color: #666;
            margin-bottom: 20px;
        }

        /* Input and button styling */
        .input-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }
        
        input[type="text"] {
            padding: 10px;
            font-size: 1em;
            width: 60%;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        .button {
            padding: 10px 20px;
            font-size: 1em;
            margin-left: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        

        .button:hover {
            background-color: #0056b3;
        }
        
        # .button {
        #     padding: 10px 20px;
        #     font-size: 1em;
        #     margin-left: 10px;
        #     background-color: #007bff;
        #     color: white;
        #     border: none;
        #     border-radius: 5px;
        #     cursor: pointer;
        # }
        

        # .button:hover {
        #     background-color: #0056b3;
        # }

        
        /* Tabs styling */
        .tab {
            display: inline-block;
            padding: 10px;
            margin-right: 5px;
            cursor: pointer;
            border-radius: 5px;
            color: #007bff;
            border: 1px solid #ddd;
        }
        
        .tab.active {
            background-color: #007bff;
            color: white;
        }

        /* Transcript box styling */
        .transcript-box {
            max-height: 300px;
            overflow-y: auto;
            background-color: #f1f1f1;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

# st.markdown(page_bg_img, unsafe_allow_html=True)
# Main container
st.markdown('<div class="container">', unsafe_allow_html=True)

# Header
st.markdown("<h1>YouTube Video Summarizer</h1>", unsafe_allow_html=True)
st.markdown('<div class="header">Get YouTube transcript and use AI to summarize YouTube videos in one click for free online with our\'s YouTube summary tool.</div>', unsafe_allow_html=True)

# Input box and button
st.markdown('<div class="input-container">', unsafe_allow_html=True)
video_url = st.text_input("Paste YouTube video link here", placeholder="https://www.youtube.com/watch?v=xxxxxxx")
if video_url:
    st.video(video_url)
with st.spinner("loading.."):
    (
st.button("Get Transcript"))
if st.button("Generate Summary"):
    st.write("Summary generation feature is coming soon!")
st.markdown('</div>', unsafe_allow_html=True)


# Tabs
tab_names = ["Transcript", "Summary","AI Chat"]
selected_tab = st.radio("Select Tab", tab_names, horizontal=True)

# Display content based on selected tab
if selected_tab == "Transcript":
    st.markdown('<div class="transcript-box">[Music] [Music] Transcript content here...</div>', unsafe_allow_html=True)
elif selected_tab == "Summary":
    st.markdown("Summary content will appear here.")
elif selected_tab == "MindMap":
    st.markdown("MindMap content will appear here.")
elif selected_tab == "AI Chat":
    st.markdown("AI Chat interface will appear here.")

# End of container
st.markdown('</div>', unsafe_allow_html=True)

with st.sidebar:
    (
        st.write("YouTube")
    )
    
with st.sidebar:
    (
     
st.markdown(
    """
    <a href="https://www.youtube.com" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" width="40">
    </a>
    """,
    unsafe_allow_html=True
    
    
)
    )

