def get_entry_type(state):
    entry = state.get("entry", {})
    return {"flow_type": entry.get("type", "text"), 
            "user_input": entry.get("content", ""), 
            "image_path": entry.get("image_path", "")}