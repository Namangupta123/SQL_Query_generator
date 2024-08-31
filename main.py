from langchain_community.llms import Replicate
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

replicate_id = "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d"
llama2_chat_replicate = Replicate(
    model=replicate_id, input={"temperature": 0.01, "max_length": 500, "top_p": 1}
)

llm = llama2_chat_replicate

template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Given an input question, convert it to a SQL query. No preamble."),
        ("human", template),
    ]
)


def get_schema():
    print("Enter the schema of the database (type 'done' when finished):")
    schema_lines = []
    while True:
        line = input()
        if line.lower() == "done":
            break
        schema_lines.append(line)
    return "\n".join(schema_lines)


def get_question():
    question = input("Enter the question: ")
    return question

schema = get_schema()
question = get_question()

input_data = {"schema": schema, "question": question}
sql_response = (
    prompt
    | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)
result = sql_response.invoke(input_data)
print("Generated SQL Query:")
print(result)
