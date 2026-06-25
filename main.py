from src.rag import ask_question

questions = [
    "What is the minimum internal temperature for a Langstroth Hive in winter?",
    "Why are entrance reducers used?",
    "How do beekeepers control condensation?"
]

for q in questions:

    result = ask_question(q)

    print("\n" + "=" * 50)

    print("QUESTION:")
    print(q)

    print("\nCONTEXT:")
    print(result["context"])

    print("\nANSWER:")
    print(result["answer"])

    print("=" * 50)