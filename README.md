# genius-rag


##  Description

Genius-RAG is a Retrieval-Augmented Generation (RAG) system that allows users to query and extract insights from codebase/repository using LLMs (Large Language Models)

###  Features

-  Testing & Coverage

-  REST API support

-  Automatic API documentation

-  Pre-Commit Code Linting & Formatting

##  Getting Started

```shell script
# Clone the repository
git clone git@github.com:suatbayir1/genius-rag.git

# cd into project root
cd genius-rag

# Launch the project
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Afterwards, the project will be live at [http://localhost:8000](http://localhost:8000).

## Documentation

FastAPI automatically generates documentation based on the specification of the endpoints you have written. You can find the docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## Testing

```shell script
# run below commands under root directory
pytest tests
```

# Code Formatting & Linting

To activate pre-commit formatting and linting all you need to do is run `pre-commit install` from the root of your local git repository. Now
every time you try to make a commit, the code will be formatted and linted for errors first.
