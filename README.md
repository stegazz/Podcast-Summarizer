# Podcast-Summarizer

I will use this project to experiment with the knowledge I have learned about prompt engineering and langchain

Main Program Documentation
Project Description
The "main" program is a tool designed to summarize podcast transcriptions using artificial intelligence models provided by OpenAI. It takes a detailed transcription of a podcast as input and generates a concise and comprehensive summary that allows readers to grasp all the essential information covered in the podcast without having to listen to it.

Getting Started
Prerequisites
Before running the program, ensure you have the following:

Python installed on your system.
The required Python packages installed. You can install the necessary packages using pip:
Copy code
pip install langchain
Installation and Usage
Clone this repository to your local machine.

Place the API key for OpenAI in a file named "openaikey.txt" in the same directory as the "main.py" script. The program will read the key from this file to authenticate the OpenAI API.

Prepare the podcast transcription you want to summarize and save it in a file named "transcription.txt" in the same directory as the "main.py" script.

Run the script using the following command:

css
Copy code
python main.py


The program will prompt you to choose the version of GPT to use (gpt-3.5-turbo or gpt-4). Enter the corresponding number (1 or 2) to proceed.

Next, enter the main topic or topics of the transcription when prompted. Other topics will be ignored during the summarization process.

The program will then start the summarization process and generate a summarized output.

The final summarized output will be saved in a file named "output.txt" in the same directory as the "main.py" script.

Program Workflow
The program loads the podcast transcription from the file "transcription.txt" and splits it into smaller parts for efficient processing.

It then customizes the Langchain prompt using the provided main topic of the podcast.

The summarization process begins, and the AI generates a detailed and comprehensive summary of the podcast.

After the initial summary is generated, the program further refines it using additional context to create a final and improved version of the summary.

The final summary is saved to the file "output.txt".

Note
This program utilizes the Langchain library for the summarization process and requires an active internet connection to interact with the OpenAI API.

For more information on Langchain and OpenAI, refer to the official documentation.

Contributing
If you find any issues or have suggestions for improvements, please feel free to contribute to this project by opening pull requests or submitting issues on the GitHub repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to the developers of the Langchain library and OpenAI for providing powerful tools for natural language processing and summarization.
