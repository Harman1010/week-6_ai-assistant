from core.rag.vectorstore import get_vectorstore
from tests.test_cases import TEST_CASES


def run_retrieval_tests():
    vectorstore = get_vectorstore()

    for test_case in TEST_CASES:
        question = test_case["question"]

        print("\n" + "=" * 70)
        print(f"{test_case['id']}: {question}")
        print("=" * 70)

        results = vectorstore.similarity_search_with_score(
            question,
            k=4,
        )

        for i, (document, score) in enumerate(results, start=1):
            print(f"\n--- Retrieved Chunk {i} ---")
            print(f"Distance: {score}")
            print(f"Metadata: {document.metadata}")
            print(f"Content:\n{document.page_content}")


if __name__ == "__main__":
    run_retrieval_tests()