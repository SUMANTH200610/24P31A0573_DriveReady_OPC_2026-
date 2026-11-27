# SmartLib – AI Library Assistant

**Program:** Drive Ready – AI Agents | OPC 2026  
**Case study:** SmartLib – AI Library Assistant

## Objective

Build an AI-powered library assistant that helps students search for books, check availability, get book information and manage borrowing requests using natural language.

## Topics covered

- AI applications and LLM integration
- Natural language-based book search
- Book availability and information retrieval
- System prompts and AI assistant behaviour
- Hallucination prevention and handling missing information
- Borrowing request management

## Files

| **File** | **Purpose** |
|---|---|
| `task.py` | Python source code for the SmartLib AI Library Assistant |
| `LLM_Fundamentals.ipynb` | Original Google Colab practical work and outputs (uploaded separately) |
| `README.md` | Task description, implementation, observations and next-step preparation |

## Implementation

SmartLib uses an LLM-powered assistant to understand student queries and provide library-related information. It supports book searches, availability questions and borrowing requests.

Actual book availability and borrowing operations require integration with a library database or backend system.

### Main functionalities

| **Functionality** | **Description** |
|---|---|
| Book Search | Search by title, author or category |
| Availability Check | Check book availability |
| Book Information | Retrieve book and author details |
| Borrowing Requests | Assist students with borrowing requests |

## Preparation — Ten customer questions

1. Do you have Python programming books?
2. Is Clean Code available?
3. Who is the author of Atomic Habits?
4. Show me Artificial Intelligence books.
5. Can I borrow a Java programming book?
6. Which books are available for Data Structures?
7. How many Python books are available?
8. How can I request Clean Code?
9. Suggest beginner programming books.
10. Is the requested book available for borrowing?

## How to run

Install the required dependency:

`pip install openai`

Set the required API key securely in your environment.

Run the application:

`python task.py`

Never commit or print API keys.

**Note:** Actual book searches, availability checks and borrowing operations require library database integration.

## Learning assessment and status

- Project concept: Defined.
- Main functionalities: Identified.
- Ten customer questions: Prepared.
- AI assistant implementation: To be completed.
- Library database integration: Pending.
- Borrowing request management: Pending.
