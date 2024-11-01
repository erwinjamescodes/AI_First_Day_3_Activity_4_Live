import streamlit as st
from streamlit_option_menu import option_menu

from summarize import ArticleSummarizer


# Sidebar for navigation and API key input
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
air = ArticleSummarizer(api_key=api_key)

with st.sidebar:
    page = option_menu(
        "Dashboard",
        ["Home", "About Me", "AWS Doc Summarizer"],
        icons=['house', 'info-circle',  'file-text'],
        menu_icon="list",
        default_index=0,
    )

if not api_key:
    st.warning("Please enter your OpenAI API Key in the sidebar to use the application.")

else:
    if page == "Home":
        st.title("AWS Documentation Summarizer")
        st.write("Welcome to the AWS Documentation Summarizer! This platform lets you summarize a very long and boring AWS Documentation into a short and comprehensible digest!")

        st.write("## How It Works")
        st.write("### AWS Documentation Summarization")
        st.write("1. **Input the Article Link:** Provide the link to the documentation.")
        st.write("2. **Analyze and Extract Information:** The tool scans the article, identifying key services involved and how these services work.")

        st.write("## Ideal Users")
        st.write("This tool is perfect for:")
        st.write("- AWS Solutions Architects and Professionals who would like to understand AWS services better and faster.")
        st.write("- Students and professionals who would like to have a digital study buddy while preparing for their AWS Certification Exams.")
        st.write("- IT Managers who would like to have a high-level overview of AWS services but do not have the pleasure of time to go over long documentations.")

        st.write("Start using the AWS Document Summarizer today to boost your AWS knowledge!")

    elif page == "About Me":
        st.header("About Me")
        st.markdown("""
        Hi! I'm Erwin Caluag! I am a Software Engineer / Web Developer and an AWS Solutions Architect Associate. Currently, I am venturing into the world of Artificial Intelligence.
                    
        This project is one of the projects I am building to try and apply the learnings I have acquired from the AI First Bootcamp from AI Republic. 
                    
        Any feedback would be greatly appreciated!
        """)

    elif page == "AWS Doc Summarizer":
        st.header("AWS Documentation Summarizer")
        text = st.text_input("Enter the link to the AWS Documentation you would like to summarize:")
        if st.button("Summarize"):
            docu = air.get_aws_doc(text)
            response = air.news_summarizer(docu.text)
            st.success("Summary generated successfully!")
            st.subheader(docu.title)
            st.write(response)