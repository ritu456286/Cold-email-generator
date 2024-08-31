import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from utils import clean_text
from chain import Chain
from portfolio import Portfolio

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Email Generator")
    url_input = st.text_input(label="Enter a URL: ", value="https://jobs.nike.com/job/R-36827?from=job%20search%20funnel")
    submit_button = st.button(label="Submit") #return True if button is clicked


    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job['skills']
                links = portfolio.query_links(skills)
                email = llm.write_email(job, links)
                st.code(email,language='markdown', wrap_lines=True)
        except Exception as e:
            st.error(f"An Error occurred: {e}")



if __name__ == '__main__':
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout='wide',
                       page_title="Cold Email Generator",
                       page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)