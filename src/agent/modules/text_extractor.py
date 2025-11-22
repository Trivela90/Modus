from pydoc import text
from langchain_core.prompts import PromptTemplate
from agent.modules.prompts import basic_extraction_prompt, extraction_from_unstructured_prompt
from agent.modules.llm import expense_extraction_llm

_prompt = PromptTemplate.from_template(extraction_from_unstructured_prompt)
_chain = _prompt | expense_extraction_llm

def input_expense_extraction(state):
    _prompt = PromptTemplate.from_template(basic_extraction_prompt)
    _chain = _prompt | expense_extraction_llm

    user_input = state.get("user_input", "")
    if user_input == "": 
        return {"expense_record": None}
    response = _chain.invoke({"input": user_input})
    return {"expense_record": response}

def text_expense_extraction(state):
    _prompt = PromptTemplate.from_template(extraction_from_unstructured_prompt)
    _chain = _prompt | expense_extraction_llm
    
    text = state.get("extracted_text", "")
    if text == "" or text is None: 
        return None
    response = _chain.invoke({"extracted_text": text})
    return response