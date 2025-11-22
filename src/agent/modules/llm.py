from langchain_google_genai import ChatGoogleGenerativeAI
from agent.modules.classes import ExpenseRecord

global_llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
expense_extraction_llm = global_llm.with_structured_output(ExpenseRecord)