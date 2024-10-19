import streamlit as st
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Cohere
from dotenv import load_dotenv

load_dotenv()

cohere_api = os.getenv["COHERE_API_KEY"]

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
cohere_llm = Cohere(model="command", temperature=0.1, cohere_api_key=cohere_api)


st.set_page_config(
    page_title="SQL Gen",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': 'Hello'
    }
)

def main():
    st.title("SQL Gen")
    st.write("A simple tool to generate SQL queries")
    schema = st.text_area("Enter schema", key="schema")
    if schema:
        generate(schema)

def generate(schema):
    question = st.text_input("Enter your query", key="query")

    if st.button("Generate SQL"):
        if not question:
            st.error("Please enter question !!")
        else:
            with st.spinner("Please wait for a few seconds :)"):
                try:
                    input_data = {"schema": schema, "question": question}
                    
                    # Use LangChain with Cohere to generate the SQL query
                    sql_response = (
                        prompt
                        | cohere_llm.bind(stop=["\nSQLResult:"])
                        | StrOutputParser()
                    )
                    result = sql_response.invoke(input_data)
                    
                    st.success("SQL query generated successfully.")
                    st.code(result, language="sql")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.error(f"Details: {str(e)}")

    if st.button("RESET"):
        try:
            st.rerun()
        except Exception as e:
            st.error(f"An error occurred while resetting the page: {e}")

if __name__ == "__main__":
    main()
