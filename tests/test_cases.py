TEST_CASES = [
    {
        "id": "q1",
        "question": "What is pollution?",
        "expected_concepts": [
            "introduction of substances or energy",
            "natural environment",
            "harmful to humans, animals, and plants",
        ],
        "answerable": True,
    },
    {
        "id": "q2",
        "question": "What are the three major categories of pollution?",
        "expected_concepts": [
            "water pollution",
            "air pollution",
            "land pollution",
        ],
        "answerable": True,
    },
    {
        "id": "q3",
        "question": "How can land pollution become water pollution?",
        "expected_concepts": [
            "runoff",
            "rain or wind",
            "storm drains",
            "streams",
            "rivers",
            "ocean",
        ],
        "answerable": True,
    },
    {
        "id": "q4",
        "question": "What are the sources of air pollution and water pollution?",
        "expected_concepts": [
            "cars and trucks",
            "factories",
            "dust",
            "smog",
            "plastics",
            "chemicals",
            "pesticides",
            "fertilizers",
        ],
        "answerable": True,
    },
    {
        "id": "q5",
        "question": "How do pollutants move through the food chain and affect organisms?",
        "expected_concepts": [
            "accumulate",
            "plants and animals",
            "ingest",
            "food chain",
            "increasing concentration",
            "health problems",
            "death",
        ],
        "answerable": True,
    },
    {
        "id": "q6",
        "question": "Why can plastic pollution remain in ecosystems for a long time, and how can it harm animals?",
        "expected_concepts": [
            "durable",
            "remain in ecosystems",
            "wind and water",
            "entangled",
            "ingest plastic",
        ],
        "answerable": True,
    },
    {
        "id": "q7",
        "question": "How much money does pollution cost the government every year?",
        "expected_concepts": [],
        "answerable": False,
    },
]


if __name__ == "__main__":
    print(f"Loaded {len(TEST_CASES)} RAG test cases.")
    for case in TEST_CASES:
        print(f"{case['id']}: {case['question']}")