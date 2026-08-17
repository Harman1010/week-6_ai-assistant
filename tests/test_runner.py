import requests

from tests.test_cases import TEST_CASES


API_URL = "http://127.0.0.1:8000/chat/"


def run_tests():
    for test_case in TEST_CASES:
        print(f"\n{'=' * 60}")
        print(f"{test_case['id']}: {test_case['question']}")
        print("=" * 60)

        response = requests.post(
            API_URL,
            json={
                "question": test_case["question"]
            },
        )

        print(f"Status: {response.status_code}")

        if response.ok:
            result = response.json()

            print("\nAnswer:")
            print(result["answer"])

            print("\nSources:")
            for source in result.get("sources", []):
                print(
                    f"  - {source['document']} "
                    f"(distance={source['score']})"
                )
        else:
            print("\nError:")
            print(response.text)


if __name__ == "__main__":
    run_tests()