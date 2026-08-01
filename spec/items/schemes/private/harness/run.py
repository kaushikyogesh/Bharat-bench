from dotenv import load_dotenv
import os
import json
from pathlib import Path

from scorers.exact_match import exact_match
from scorers.numeric_tolerance import numeric_tolerance
from scorers.rubric import rubric_score
from scorers.refusal import refusal_check


# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

API_KEY = os.getenv("API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "default-model"
)


# ============================================================
# 2. AI MODEL FUNCTION
# ============================================================

def get_model_answer(question):
    """Get an answer from the AI model."""

    if not API_KEY:
        raise ValueError(
            "API_KEY is not configured. "
            "Please add it to the .env file."
        )

    # Actual AI API integration will be added later.
    return ""


# ============================================================
# 3. LOAD JSONL DATASET
# ============================================================

def load_jsonl(file_path):
    """Load benchmark questions from a JSONL file."""

    items = []

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            line = line.strip()

            if line:

                items.append(
                    json.loads(line)
                )

    return items


# ============================================================
# 4. EVALUATE ONE QUESTION
# ============================================================

def evaluate_item(item, predicted_answer):
    """Evaluate a single benchmark item."""

    question_type = item["question_type"]

    # --------------------------------------------------------
    # MCQ / SHORT FACTUAL
    # --------------------------------------------------------

    if question_type in [
        "mcq",
        "short_factual"
    ]:

        score = exact_match(
            item["answer"],
            predicted_answer
        )

        return {
            "id": item["id"],
            "domain": item["domain"],
            "question_type": question_type,
            "score": score,
            "status": (
                "correct"
                if score == 1
                else "incorrect"
            )
        }


    # --------------------------------------------------------
    # NUMERICAL
    # --------------------------------------------------------

    elif question_type == "numerical":

        score = numeric_tolerance(
            item["answer"],
            predicted_answer
        )

        return {
            "id": item["id"],
            "domain": item["domain"],
            "question_type": question_type,
            "score": score,
            "status": (
                "correct"
                if score == 1
                else "incorrect"
            )
        }


    # --------------------------------------------------------
    # OPEN ANSWER
    # --------------------------------------------------------

    elif question_type == "open_answer":

        score = rubric_score(
            item["answer"],
            predicted_answer
        )

        return {
            "id": item["id"],
            "domain": item["domain"],
            "question_type": question_type,
            "score": score,
            "status": "evaluated"
        }


    # --------------------------------------------------------
    # UNANSWERABLE
    # --------------------------------------------------------

    elif question_type == "unanswerable":

        score = refusal_check(
            predicted_answer
        )

        return {
            "id": item["id"],
            "domain": item["domain"],
            "question_type": question_type,
            "score": score,
            "status": (
                "appropriate_refusal"
                if score == 1
                else "incorrect"
            )
        }


    # --------------------------------------------------------
    # UNKNOWN QUESTION TYPE
    # --------------------------------------------------------

    else:

        return {
            "id": item["id"],
            "domain": item["domain"],
            "question_type": question_type,
            "score": None,
            "status": "unknown_question_type"
        }


# ============================================================
# 5. CALCULATE DOMAIN-WISE SCORES
# ============================================================
def calculate_domain_scores(results):
    domain_data = {}

    for result in results:
        domain = result["domain"]
        score = result["score"]

        if score is None:
            continue

        if domain not in domain_data:
            domain_data[domain] = {
                "obtained": 0,
                "maximum": 0
            }

        domain_data[domain]["obtained"] += score

        if result["question_type"] == "open_answer":
            domain_data[domain]["maximum"] += 2
        else:
            domain_data[domain]["maximum"] += 1

    final_scores = {}

    for domain, data in domain_data.items():
        final_scores[domain] = round(
            (data["obtained"] / data["maximum"]) * 100,
            2
        )

    return final_scores


# ============================================================
# 6. CALCULATE OVERALL SCORE
# ============================================================

def calculate_overall_score(results):
    obtained = 0
    maximum = 0

    for result in results:
        score = result.get("score")

        if score is None:
            continue

        obtained += score

        if result["question_type"] == "open_answer":
            maximum += 2
        else:
            maximum += 1

    if maximum == 0:
        return 0

    return round((obtained / maximum) * 100, 2)

# ============================================================
# 7. SAVE RESULTS
# ============================================================

def save_results(
    results,
    output_file
):
    """Save evaluation results as JSON."""

    output = {

        "benchmark":
            "Bharat-Bench",

        "model":
            MODEL_NAME,

        "total_items":
            len(results),

        "overall_score":
            calculate_overall_score(
                results
            ),

        "domain_scores":
            calculate_domain_scores(
                results
            ),

        "results":
            results
    }

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
## ============================================================
# 8. DATASET SELECTION
# ============================================================

def get_benchmark_datasets(dataset_path=None):
    """Return selected Bharat-Bench dataset path."""

    if dataset_path:
        return [
            Path(dataset_path)
        ]

    return [
        Path(
            "spec/items/schemes/questions.jsonl"
        )
    ]

# ============================================================
# 9. MAIN PROGRAM
# ============================================================

def main():

    print(
        "=" * 60
    )

    print(
        "        Bharat-Bench Evaluation Harness"
    )

    print(
        "=" * 60
    )

    print(
        f"Model: {MODEL_NAME}"
    )

    import sys

    dataset_path = None

    if len(sys.argv) > 1:
        dataset_path = sys.argv[1]

    dataset_paths = get_benchmark_datasets(
        dataset_path
    )

    # Store all evaluation results

    all_results = []

    # --------------------------------------------------------
    # PROCESS EACH DATASET
    # --------------------------------------------------------

    for dataset_path in dataset_paths:

        print(
            "\n"
            + "=" * 60
        )

        print(
            f"Dataset: {dataset_path}"
        )

        print(
            "=" * 60
        )


        # Check dataset exists

        if not dataset_path.exists():

            print(
                f"Dataset not found: "
                f"{dataset_path}"
            )

            print(
                "Skipping this dataset..."
            )

            continue


        # Load dataset

        items = load_jsonl(
            dataset_path
        )


        print(
            f"Total questions: "
            f"{len(items)}"
        )


        # ----------------------------------------------------
        # EVALUATE QUESTIONS
        # ----------------------------------------------------

        for item in items:

            print(
                "\n"
                + "-" * 60
            )

            print(
                f"Question ID   : "
                f"{item['id']}"
            )

            print(
                f"Domain        : "
                f"{item['domain']}"
            )

            print(
                f"Question Type : "
                f"{item['question_type']}"
            )

            print(
                f"Question      : "
                f"{item['question']}"
            )


            # ------------------------------------------------
            # MANUAL ANSWER FOR NOW
            # ------------------------------------------------

            predicted_answer = input(
                "Enter model answer: "
            )


            # Evaluate answer

            result = evaluate_item(
                item,
                predicted_answer
            )


            # Store result

            all_results.append(
                result
            )


            # Show result

            print(
                "\nEvaluation Result"
            )

            print(
                "-----------------"
            )

            print(
                f"Score  : "
                f"{result['score']}"
            )

            print(
                f"Status : "
                f"{result['status']}"
            )


    # ========================================================
    # SAVE FINAL RESULTS
    # ========================================================

    output_path = Path(
        "results.json"
    )


    save_results(
        all_results,
        output_path
    )


    # ========================================================
    # FINAL SUMMARY
    # ========================================================

    print(
        "\n"
        + "=" * 60
    )

    print(
        "Evaluation completed successfully."
    )

    print(
        f"Total Evaluated Items: "
        f"{len(all_results)}"
    )

    print(
        f"Overall Score: "
        f"{calculate_overall_score(all_results)}%"
    )

    print(
        "Domain Scores:"
    )

    domain_scores = (
        calculate_domain_scores(
            all_results
        )
    )


    for domain, score in domain_scores.items():

        print(
            f"  {domain}: {score}%"
        )


    print(
        f"Results saved to: "
        f"{output_path}"
    )

    print(
        "=" * 60
    )


# ============================================================
# 10. RUN PROGRAM
# ============================================================

if __name__ == "__main__":

    main()