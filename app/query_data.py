import os
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are SalesBot, a super helpful but chill course advisor 😎.
you work for Forethought company.You FOunders program course.
Your job is to help users discover and buy the right courses — sound friendly, casual, and keep it short & persuasive.

Context:
{context}

---

Question: {question}
Answer in 3-5 lines, use bullet points if needed, and make it sound human.
"""


def get_answer(query_text: str) -> str:
    # Prepare the DB
    embedding_function = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.environ['GEMINI_API_KEY']
    )
    db = Chroma(persist_directory=CHROMA_PATH,
                embedding_function=embedding_function)

    # Search the DB
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.3:
        return "I'm sorry, I couldn't find a relevant answer. Please try rephrasing."

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.environ["GEMINI_API_KEY"],
        temperature=1,
        top_p=0.5
    )

    response_text = model.invoke(prompt)
    return response_text.content if hasattr(response_text, "content") else str(response_text)


import re

def format_response(text: str) -> str:
    # Replace *bold* with <strong>bold</strong>
    text = re.sub(r'\*(\S(.*?\S)?)\*', r'<strong>\1</strong>', text)

    # Replace newlines with <br>
    text = text.replace("\n", "<br>")

    return text
