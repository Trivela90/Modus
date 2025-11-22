import streamlit as st

from agent.flow import call_agent
from static.translate import translator

st.set_page_config(page_title="Chatbot", page_icon="💬")


INITIAL_ASSISTANT_MSG = (
    "Olá sou a SofIA e estou aqui para te ajudar com suas finanças. 😁"
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Mock data"},
        {"role": "assistant", "content": INITIAL_ASSISTANT_MSG},
    ]

# track conversation state
if "end_flag" not in st.session_state:
    st.session_state.end_flag = False
if "texts" not in st.session_state:
    st.session_state.texts = ""

st.title("SofIA")

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Use a single chat_input with a fixed key to avoid duplicate auto-generated IDs.
user_text = st.chat_input("Descreva seu último gasto...", key="user_input")

if user_text:
    st.session_state.texts += user_text
    
    # add user message
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # call LLM
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = call_agent({"entry": {"type": "text", "content": st.session_state.texts}})
            st.session_state.end_flag = response.get("end_flag", False)

            if st.session_state.end_flag:
                assistant_text = "Ótimo! Todas as informações necessárias foram coletadas com sucesso. O gasto foi registrado."
                expense = response.get("expense_record")
                st.session_state["user_data"].append(expense.dict())
                # normalize to dict whether it's a pydantic model or a plain dict
                if hasattr(expense, "dict"):
                    rec = expense.dict()
                else:
                    rec = expense or {}

                def _to_str(v):
                    if v is None:
                        return ""
                    # handle enums with .value
                    if hasattr(v, "value"):
                        return str(v.value)
                    return str(v)

                def t(v):
                    # translate every displayed value (use original string as fallback)
                    s = _to_str(v)
                    return translator.get(s, s)

                # format amount nicely and translate the resulting string
                amount_val = rec.get("amount")
                if isinstance(amount_val, (int, float)):
                    amount_str = f"R$ {amount_val:,.2f}"
                else:
                    try:
                        amount_str = f"R$ {float(amount_val):,.2f}"
                    except Exception:
                        amount_str = _to_str(amount_val)
                amount_str = translator.get(amount_str, amount_str)

                # build display row using Portuguese labels from translator and translate all values
                display_row = {
                    translator.get("description", "description"): t(rec.get("description")),
                    translator.get("category", "category"): t(rec.get("category")),
                    translator.get("amount", "amount"): amount_str,
                    translator.get("payment_method", "payment_method"): t(rec.get("payment_method")),
                    translator.get("vendor", "vendor"): t(rec.get("vendor")),
                    translator.get("notes", "notes"): t(rec.get("notes")),
                }

                # show as a single-row table
                st.table([display_row])
                assistant_text += "Obrigado por usar a SofIA! Se precisar de mais alguma coisa, é só chamar. Até mais! 👋"
                st.session_state.texts = ""
                st.markdown(assistant_text)
            else:
                missing = response.get("missing_fields", [])
                missing_fields_pt = [translator.get(field, field) for field in missing]
                assistant_text_lines = ["Entendi. Faltam algumas informações:"]
                for field in missing_fields_pt:
                    assistant_text_lines.append(f"- **{field}**")
                assistant_text = "\n".join(assistant_text_lines)
                st.markdown(assistant_text)

    st.session_state.messages.append({"role": "assistant", "content": assistant_text})
