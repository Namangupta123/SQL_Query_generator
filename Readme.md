# SQL Query Generator

The `main.py` script in this project is a powerful tool for generating SQL queries from a given database schema and a user's question. It effectively utilizes the `langchain_community`, `langchain_core`, and `replicate` libraries to create a sophisticated language model. This model can accurately interpret the provided schema and question, and generate the corresponding SQL query with high precision. The script is designed to be user-friendly, prompting users for necessary inputs and seamlessly integrating with the environment variables for secure API token management.

## Requirements

Make sure you have the following dependencies installed:

- `langchain_community`
- `langchain_core`
- `python-dotenv`
- `replicate`
- `StrOutputParser`
- `ChatPromptTemplate`

## Usage

To use the SQL query generator, you need to set up your environment with the correct API keys and tokens. Here's how to do it:

1. Clone the repository:
   ```
   git clone https://github.com/Namangupta123/SQL_Query_generator.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with the correct API keys and tokens. You can use the `.env.example` file as a template.

4. Run the `main.py` script:

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

