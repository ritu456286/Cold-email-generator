# Cold Email Generator

## Overview

The Cold Email Generator is a Python-based application designed to automate the creation of cold emails. It leverages various technologies to generate, manage, and optimize cold email content. The application uses a combination of modern libraries and APIs to provide a seamless experience for generating personalized cold emails.

## Tech Stack

- **Python**: The primary programming language used for developing the application.
- **Streamlit**: A framework for creating interactive web applications for data science and machine learning projects.
- **ChromaDB**: A database used to store and query tech stack links based on relevance.
- **Groq API**: An API used for interacting with advanced AI models.
- **Llama3**: An AI model utilized for generating text based on prompts.
- **LangChain**: A framework that integrates with Llama3 and other tools to manage and enhance language model interactions.

## Features

- **Generate Cold Emails**: Create personalized cold emails using advanced language models.
- **Tech Stack Querying**: Store tech stack links in ChromaDB and query for relevant links based on the tech stack.
- **Interactive UI**: Use Streamlit to interact with the application and manage email generation tasks.

## Setup

### Prerequisites

1. **Python**: Ensure that Python is installed on your system.
2. **Anaconda**: Install Anaconda to manage Python environments and packages.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ritu456286/Cold-email-generator.git
   cd Cold-email-generator
   ```

2. **Navigate to the Project Directory**

    ```bash
    cd Cold-email-generator
    ```

3. **Create and Activate a Conda Environment**

    ```bash
    conda create --name GenAiLearning python=3.8
    conda activate GenAiLearning
    ```

4. **Install Required Packages**

    Install the necessary libraries using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, you can install packages individually using conda or pip.

5. **Set Up Environment Variables**

    Create a `.env` file in the root of the project directory with the following content:

    ```plaintext
    GROQ_API_KEY=your_groq_api_key_here
    ```

    Replace `your_groq_api_key_here` with your actual GROQ API key. The API key is necessary for the project to access the GROQ services.

## Usage

1. **Run the Application**

    To start the application, run the following command:

    ```bash
    streamlit run app.py
    ```

    Make sure to have Streamlit installed in your environment.

2. **Access the Application**

    Open a web browser and navigate to `http://localhost:8501` to interact with the Cold Email Generator.

## Project Structure

- **`app.py`**: The main application script that runs the Cold Email Generator.
- **`requirements.txt`**: A file listing the Python dependencies required for the project.
- **`.env`**: Environment file where sensitive information such as API keys are stored.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. Thanks to Codebasics for teaching this!

## Contact

For any questions or feedback, please contact the repository owner via GitHub.

---

**Note**: Ensure you have set up your `.env` file correctly with a valid GROQ API key before running the application.
