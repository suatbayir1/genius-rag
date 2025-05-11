from app.models.llm.enums import LLMTaskType


class PromptBuilder:
    PROMPT_TEMPLATES: dict[str, str] = {
        LLMTaskType.QA: """
            Answer the question based only on the following context:

            Context:
            {context}

            ---

            Answer the question based on the above context:
            {query}

            Answer:
        """,
        LLMTaskType.SUMMARIZATION: """
            Summarize the following content clearly and concisely for software engineers.

            Content:
            {context}

            Summary:
            {query}
        """,
        LLMTaskType.EXPLAIN: """
            Explain the following code to a junior developer. Be concise but educational.

            Code:
            {context}

            Explanation:
            {query}
        """,
        LLMTaskType.DETECT_QUERY_TYPE: """
            You are a helpful and knowledgeable software engineer assistant.
            You will be provided with a user question.

            Your task is to determine the type of the question and respond with **only one** of the following options.
            Return the exact string, **nothing more**, no explanation, no punctuation.

            The possible types are:
            {context}

            Respond with only one of the above types.

            User Question:
            {query}
        """,
    }

    @staticmethod
    def build(task_type: LLMTaskType, context: str, query: str) -> str:
        template = PromptBuilder.PROMPT_TEMPLATES.get(task_type)
        if not template:
            return "Invalid task type"
        return template.format(context=context, query=query)
