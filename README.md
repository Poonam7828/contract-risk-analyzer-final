Contract Risk Analyzer (GenAI-powered)

Problem Statement :
Organizations and small to medium businesses frequently deal with complex legal contracts such as employment agreements, service contracts, and lease agreements. 
Understanding these contracts manually is time-consuming and requires legal expertise, especially when identifying risky clauses related to penalties, unilateral 
termination, and non-compete conditions.

The goal of this project is to build an **AI-powered Contract Analysis & Risk Assessment Bot** that helps users quickly analyze contracts, identify potential risks,
and understand them in simple language.

# Solution Overview
Contract Risk Analyzer is a GenAI-powered web application that:
- Classifies contract type
- Detects risky clauses
- Assigns risk levels
- Explains contracts in simple business language

The application is designed for Indian SMEs and non-legal users.

# Key Features
- Contract type classification (Employment, Service, Lease, etc.)
- Risk scoring (Low / Medium / High)
- Detection of:
  - Penalty clauses
  - Unilateral termination clauses
  - Non-compete clauses
- Clause-level risk explanation
- AI-powered plain English explanation
- Simple and clean UI

# Technologies Used
- Python
- Streamlit (UI)
- OpenAI API (GenAI explanation)
- Rule-based NLP logic
- GitHub for version control

# How It Works
1. User pastes contract text into the app
2. System analyzes keywords and clauses
3. Risk level is calculated
4. AI explains the contract risks in simple language

## How to Run Locally
```bash
pip install streamlit openai
streamlit run app.py
