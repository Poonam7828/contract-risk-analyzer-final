import streamlit as st
import os
from openai import OpenAI

# TEMPORARY: paste your API key here (for local hackathon demo)
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Contract Risk Analyzer")

st.title("Contract Analysis & Risk Assessment Bot")

contract_text = st.text_area(
    "Paste your contract text here",
    height=300
)

def detect_contract_type(text):
    text = text.lower()
    if "salary" in text or "employee" in text:
        return "Employment Contract"
    elif "rent" in text or "lease" in text:
        return "Lease Agreement"
    elif "service" in text or "vendor" in text:
        return "Service Contract"
    else:
        return "General Contract"

def detect_risk(text):
    text = text.lower()
    risks = []

    if "penalty" in text:
        risks.append("Penalty clause detected")
    if "terminate anytime" in text or "without notice" in text:
        risks.append("Unilateral termination clause")
    if "non-compete" in text:
        risks.append("Non-compete clause")

    if "Penalty clause detected" in risks or "Unilateral termination clause" in risks:
        overall = "High"
    elif "Non-compete clause" in risks:
        overall = "Medium"
    else:
        overall = "Low"

    return overall, risks

def ai_explain(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Explain the contract in very simple business English."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    except Exception:
        return "⚠️ AI explanation is temporarily unavailable due to API quota limits."


if st.button("Analyze Contract"):
    if contract_text.strip() == "":
        st.warning("Please paste a contract first.")
    else:
        st.subheader("Analysis Result")

        contract_type = detect_contract_type(contract_text)
        risk_level, risk_details = detect_risk(contract_text)

        st.write(f"**Contract Type:** {contract_type}")
        st.write(f"**Overall Risk Level:** {risk_level}")

        if risk_details:
            st.markdown("### Risk Details")
            for r in risk_details:
                st.write("•", r)

            st.markdown("### 🤖 AI Explanation")
            explanation = ai_explain(contract_text)
            st.write(explanation)
        else:
            st.success("No major risks detected.")
