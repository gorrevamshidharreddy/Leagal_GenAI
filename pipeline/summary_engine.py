def generate_contract_summary(
    contract_type,
    entities,
    high_risk_count,
    medium_risk_count,
    language
):
    summary = []

    summary.append(f"Contract Type: {contract_type}")
    summary.append(f"Detected Language: {language}")

    if entities["parties"]:
        summary.append(
            "Parties involved: " + ", ".join(entities["parties"])
        )

    if entities["dates"]:
        summary.append(
            "Key dates mentioned: " + ", ".join(entities["dates"])
        )

    if entities["amounts"]:
        summary.append(
            "Financial amounts referenced: " + ", ".join(entities["amounts"])
        )

    summary.append(
        f"High-risk clauses: {high_risk_count}, Medium-risk clauses: {medium_risk_count}"
    )

    if high_risk_count > 0:
        summary.append(
            "The contract contains high-risk clauses that should be renegotiated before signing."
        )
    elif medium_risk_count > 0:
        summary.append(
            "The contract has moderate risks and should be reviewed carefully."
        )
    else:
        summary.append(
            "The contract appears low risk based on automated analysis."
        )

    return summary
