def check_expense_record(expense_record) -> tuple:
    required_fields = ["amount", "payment_method"]
    missing = []
    for field in required_fields:
        if isinstance(expense_record, dict):
            val = expense_record.get(field)
        else:
            val = getattr(expense_record, field, None)
        if val is None or (isinstance(val, str) and not val.strip()):
            missing.append(field)
    return (len(missing) == 0, missing)

def finish(state) -> dict:
    ok, missing = check_expense_record(state.get("expense_record", {}))
    return {"end_flag": ok, "missing_fields": missing}