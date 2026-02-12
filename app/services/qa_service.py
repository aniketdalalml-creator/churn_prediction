from app.services.sql_service import fetch_query
from app.core.llm import ask_llm


def answer_question(question: str):

    if "churn" in question.lower():

        query = """
            SELECT month,
                   COUNT(*) AS total_customers,
                   SUM(CASE WHEN churn_flag THEN 1 ELSE 0 END) AS churned_customers,
                   ROUND(
                       SUM(CASE WHEN churn_flag THEN 1 ELSE 0 END)::numeric
                       / COUNT(*) * 100, 2
                   ) AS churn_rate
            FROM telecom_simulation
            GROUP BY month
            ORDER BY month;
        """

        columns, data = fetch_query(query)

        context = "Telecom churn monthly summary:\n\n"
        context += " | ".join(columns) + "\n"

        for row in data:
            context += " | ".join(str(item) for item in row) + "\n"

        prompt = f"""
        You are a telecom data analyst.

        Here is the data:

        {context}

        Question: {question}

        Provide a clear business explanation.
        """

        return ask_llm(prompt)

    return ask_llm(question)
