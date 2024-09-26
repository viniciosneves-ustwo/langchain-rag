# CP FastAPI - Conversational Retrieval API

## Description

This project is an API built with FastAPI and LangChain, implementing a conversational assistant using CSV documents as the data source. The application loads content from a CSV file, processes it into chunks, and generates embeddings using the OpenAI model, storing them in a FAISS index for efficient retrieval. The language model used is `gpt-4`.

The application allows interactions via chat where the documents are used to generate contextually relevant responses.

## Technologies used

- Python 3.12
- FastAPI: A framework for building APIs
- LangChain: A library for orchestrating language models and information retrieval
- OpenAI API: Used to generate document embeddings
- FAISS: A library for indexing and searching high-dimensional vectors
- Docker: To package and run the application in a container
- Poetry: Python dependency manager
- Uvicorn: ASGI server for running FastAPI

## Requirements

- Docker installed (for running with Docker)
- Python 3.12 and Poetry installed (for local execution)
- A `.env` file with your OpenAI API key (`LANGCHAIN_API_KEY`)

## How to run the project

### Using Docker

1. Create a `.env` file in the project root with your API key:
   ```
   LANGCHAIN_API_KEY=sk-proj-TAX
   ```

2. Run the following command to start the container:
   ```
   docker-compose up --build
   ```

3. The API will be accessible at `http://localhost:8000`

### Using Poetry (local execution)

1. Install the dependencies with Poetry:
   ```
   poetry install
   ```

2. Create a `.env` file with your API key:
   ```
   LANGCHAIN_API_KEY=sk-proj-TAX
   ```

3. Run the FastAPI server:
   ```
   poetry run uvicorn rag:app --reload
   ```

4. The API will be running locally at `http://localhost:8000`

## API Endpoints

### POST /chat

This route allows interacting with the conversational assistant. The assistant will use the processed documents to provide contextually relevant responses.

## CSV File Structure

The `content.csv` file should contain the data that the assistant will use to generate responses. The format can be customized as needed.