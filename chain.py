import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

load_dotenv()  # take environment variables from .env.

# key = os.getenv("GROQ_API_KEY")
class Chain:
    def __init__(self) -> None:
        self.llm = ChatGroq(
                        model_name="llama-3.1-70b-versatile",
                        temperature=0,
                        groq_api_key=os.getenv('GROQ_API_KEY'),
                    )

    def extract_jobs(self, job_text: str) -> list[dict[str, str]]:
        """This function extracts the job info from the text and return its JSON"""
        prompt = """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}

        ### INSTRUCTION:
        The text above is from a career page on a website. Extract the job postings from this text and return them in JSON format with the following keys:
        - `role`: The job title or role.
        - `experience`: Required experience for the role.
        - `skills`: Skills needed for the role.
        - `description`: A brief description of the role.

        Ensure that the output is a valid JSON object with these keys, and only the JSON without any additional text.

        ### VALID JSON (NO PREAMBLE):
        """

        prompt_template = PromptTemplate.from_template(prompt)
        chain = prompt_template | self.llm
        res = chain.invoke(input={'page_data': job_text})
        try:
            json_parser = JsonOutputParser()
            json_res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs text.")
        return json_res if isinstance(json_res, list) else [json_res] #returning a list of jobs JSON, because there might come case where on a single url, we have multiple jobs - list of JSON objects
    
    def write_email(self, job_JSON: dict, links_data):
        """This function takes the extracted JSON job and all the profile links data to generate a relevant mail and returns it"""
        prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Ritu, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
        the seamless integration of business processes through automated tools. 
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
        Remember you are Mohan, BDE at AtliQ. 
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        
        """
        )
        chain_email = prompt_email | self.llm
        res_mail = chain_email.invoke({"job_description": str(job_JSON), "link_list": links_data})
        return res_mail.content

    

if __name__ == '__main__':
    print(os.getenv("GROQ_API_KEY"))
