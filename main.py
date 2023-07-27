import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import TokenTextSplitter

print("Choose the version of GPT to use (recommended gpt-4):")
print("1. gpt-3.5-turbo")
print("2. gpt-4")

usr_choice = input("Enter the corresponding number (1 or 2): ")

if usr_choice == "1":
    print("You have chosen gpt-3.5-turbo")
    engine = "gpt-3.5-turbo"
    chunk_size = 2500
elif usr_choice == "2":
    print("You have chosen gpt-4")
    engine = "gpt-4"
    chunk_size = 5000
else:
    print("You entered an invalid number. Exiting...")
    exit()

topic = input("Enter the main topic or topics of the transcription (other topics will be ignored. Press Enter when finished): ")

with open("openaikey.txt") as f:
    openaikey = f.read()

os.environ["OPENAI_API_KEY"] = openaikey

llm = ChatOpenAI(temperature=0, client=engine)

text_splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=50)

# Open transcription.txt
with open("transcription.txt", "r") as f:
    transcription = f.read()

# Split the document into parts
texts = text_splitter.split_text(transcription)

docs = [Document(page_content=t) for t in texts]

# Customize the Langchain prompt with the conference topic provided as input

prompt_topic = PromptTemplate(
    input_variables=["topic", "text"],
    template="""- You are an artificial intelligence taking detailed and comprehensive notes of a podcast transcription.
- Your goal is to create a concise, well-structured, and detailed text that allows people who haven't listened to the podcast to have all the information as if they had.
- This is only the first iteration of the summary, so it's much better to be too detailed rather than too vague: it's essential to include all information that might be useful in the future, even if unsure.

PODCAST TRANSCRIPTION:

{text}

PODCAST TOPIC:

{topic}

EXTENDED SUMMARY:"""
)

prompt_template = prompt_topic.format(topic=topic, text="{text}")

PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
refine_template = (
    "Your task is to create a final, complete, and extended summary of the podcast.\n"
    "We have provided an existing summary up to this point:\n\n{existing_answer}\n\n"
    "Now, we have the opportunity to improve this existing summary"
    " (only if necessary) with more context below.\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "Given the new context, improve the existing summary."
    " If the context isn't helpful, rewrite the original summary exactly as it is."
    " Your job is to make the summary more readable. Never omit anything: always include all information."
    " If appropriate, use paragraphs, bullet points, and numbered lists to make the summary more readable."
)
refine_prompt = PromptTemplate(
    input_variables=["existing_answer", "text"],
    template=refine_template,
)
chain = load_summarize_chain(llm, chain_type="refine", return_intermediate_steps=False, question_prompt=PROMPT, refine_prompt=refine_prompt)
final_output = chain({"input_documents": docs}, return_only_outputs=True) # This starts the summarization process

# Save the result to a file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(final_output["output_text"])

