from src.rag import ask_question

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

expected_answers = {
    "What is the minimum internal temperature for a Langstroth Hive in winter?":
        "Above 40 degrees Fahrenheit.",

    "Why are entrance reducers used?":
        "To prevent field mice from entering.",

    "How do beekeepers control condensation?":
        "By using insulated wraps and moisture quilt boxes."
}

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

scores = []

for question, expected in expected_answers.items():

    result = ask_question(question)

    generated = result["answer"]

    emb1 = model.encode([expected])
    emb2 = model.encode([generated])

    score = cosine_similarity(
        emb1,
        emb2
    )[0][0]

    scores.append(score)

    print("\nQuestion:", question)
    print("Expected:", expected)
    print("Generated:", generated)
    print("Similarity:", round(score, 4))

print("\nAverage Score:", round(sum(scores)/len(scores), 4))