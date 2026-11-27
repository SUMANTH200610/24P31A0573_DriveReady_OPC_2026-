
"""
Day 1 - SmartLib AI Library Assistant.
Fictional library catalogue for learning.
Set GROQ_API_KEY in environment or Colab secrets.
Run: python task.py --help
"""

import argparse
import os

MODEL = "openai/gpt-oss-20b"
BASE_URL = "https://api.groq.com/openai/v1"

SYSTEM = """
ROLE: You are SmartLib, a friendly college library assistant.

FACTS:
- Python Crash Course - Eric Matthes - 3 copies
- Clean Code - Robert C. Martin - 2 copies
- Atomic Habits - James Clear - 1 copy
- Introduction to Algorithms - Thomas H. Cormen - 0 copies
- Data Structures and Algorithms in Python - Michael T. Goodrich - 2 copies
- Artificial Intelligence: A Modern Approach - Russell and Peter Norvig - 1 copy
- Java: The Complete Reference - Herbert Schildt - 2 copies

Students can search by title, author or category.
Borrowing requests require library staff processing.

RULES:
- Never invent book details or availability.
- Never claim unavailable books are available.
- Admit when information is missing.
- Never confirm unprocessed borrowing requests.
- Never invent borrowing policies or fines.

FORMAT:
Reply politely in under 50 words.
Use simple English or Telugu based on the student.
"""

SYSTEM_NO_FACTS = SYSTEM.split("FACTS:")[0] + SYSTEM.split("RULES:")[1].join(["RULES:", ""])

QUESTIONS = [
    "Do you have Python programming books?",
    "Is Clean Code available?",
    "Who is the author of Atomic Habits?",
    "Show me Artificial Intelligence books.",
    "Can I borrow a Java programming book?",
    "Which books are available for Data Structures?",
    "How many Python books are available?",
    "Can I request Clean Code for borrowing?",
    "Suggest beginner programming books.",
    "Is Introduction to Algorithms available?"
]


def create_client():
    from openai import OpenAI

    key = os.getenv("GROQ_API_KEY")
    if not key:
        try:
            from google.colab import userdata
            key = userdata.get("GROQ_API_KEY")
        except Exception:
            raise SystemExit("Set GROQ_API_KEY first.") from None

    if not key:
        raise SystemExit("GROQ_API_KEY is empty.")

    return OpenAI(api_key=key, base_url=BASE_URL)


def ask(client, question, system=None, temperature=0.2):
    messages = ([{"role": "system", "content": system}] if system else [])
    messages.append({"role": "user", "content": question})
    return client.chat.completions.create(
        model=MODEL, temperature=temperature, messages=messages
    )


def first_call(client):
    for prompt in [
        "You are a friendly assistant.",
        "You are a college library assistant. Suggest programming books."
    ]:
        r = ask(client, "Suggest five books for students.", prompt)
        print(r.choices[0].message.content)


def temperature_experiment(client):
    for temp in [0.2, 1.2]:
        print("\nTemperature:", temp)
        for i in range(3):
            r = ask(client, "Write a SmartLib tagline.", SYSTEM, temp)
            print("Attempt", i + 1, r.choices[0].message.content)


def hallucination_experiment(client):
    q = "Do you have Advanced Quantum Programming?"
    for label, prompt in [("Without facts", SYSTEM_NO_FACTS), ("With facts", SYSTEM)]:
        print(label, ask(client, q, prompt).choices[0].message.content)


def memory_experiment(client):
    intro, q = "My name is Ravi.", "What is my name?"
    reply = ask(client, intro).choices[0].message.content
    print("Without history:", ask(client, q).choices[0].message.content)

    messages = [
        {"role": "user", "content": intro},
        {"role": "assistant", "content": reply or "Hello Ravi!"},
        {"role": "user", "content": q}
    ]
    r = client.chat.completions.create(model=MODEL, messages=messages)
    print("With history:", r.choices[0].message.content)


def token_experiment(client):
    for lang, q in [
        ("English", "Is Clean Code available?"),
        ("Telugu", "లైబ్రరీలో క్లీన్ కోడ్ అందుబాటులో ఉందా?")
    ]:
        r = ask(client, q, SYSTEM)
        print("\n", lang, "\nResponse:", r.choices[0].message.content)
        print("Prompt:", r.usage.prompt_tokens,
              "Completion:", r.usage.completion_tokens,
              "Total:", r.usage.total_tokens)


def business_experiment(client):
    for q in QUESTIONS:
        r = ask(client, q, SYSTEM)
        print("Student:", q, "\nSmartLib:", r.choices[0].message.content, "\n")


def main():
    tasks = {
        "first": first_call,
        "temperature": temperature_experiment,
        "hallucination": hallucination_experiment,
        "memory": memory_experiment,
        "tokens": token_experiment,
        "business": business_experiment
    }

    parser = argparse.ArgumentParser(description="SmartLib Day 1 practicals")
    parser.add_argument("task", nargs="?", default="business",
                        choices=[*tasks, "all"])
    args = parser.parse_args()
    client = create_client()

    selected = tasks.items() if args.task == "all" else [(args.task, tasks[args.task])]
    for name, function in selected:
        print("\n===", name.upper(), "===")
        function(client)


if __name__ == "__main__":
    main()

