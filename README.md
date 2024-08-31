# Cold Email Generator

## Overview

The Cold Email Generator project is a tool designed to automate the process of generating cold emails. It uses various libraries and models to craft personalized emails for outreach. This repository includes the code and instructions necessary to set up and run the project.

## Features

- **Personalized Cold Emails**: Generate tailored cold emails based on input parameters.
- **Integration with GROQ API**: Utilize the GROQ API for natural language processing and content generation.
- **Flexible Configuration**: Easily configure the project with environment variables.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ritu456286/Cold-email-generator.git
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
