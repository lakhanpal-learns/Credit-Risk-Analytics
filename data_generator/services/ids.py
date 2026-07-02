def generate_ids(loan_number: int) -> dict:
    return {
        "loan_id": f"LOAN{loan_number:06d}",
        "application_id": f"APP{loan_number:06d}"
    }