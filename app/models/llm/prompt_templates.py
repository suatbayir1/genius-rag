from app.models.llm.enums import LLMTaskType

PROMPT_TEMPLATES: dict[str, str] = {
    LLMTaskType.QA: """
        You are a helpful and knowledgeable software engineer assistant.

        You will be provided with:
        - Relevant code snippets from a codebase.
        - Supporting documentation from technical PDFs or READMEs.

        Use this information to answer the user's question as accurately as possible.

        Always provide clear, concise, and developer-friendly responses. If relevant, include code examples.

        ---

        Relevant Code Snippets:
        {context}

        User Question:
        {question}

        Answer:
    """,
    LLMTaskType.SUMMARIZATION: """
        Summarize the following content clearly and concisely for software engineers.

        Content:
        {context}

        Summary:
    """,
    LLMTaskType.EXPLAIN: """
        Explain the following code to a junior developer. Be concise but educational.

        Code:
        {context}

        Explanation:
    """,
}
