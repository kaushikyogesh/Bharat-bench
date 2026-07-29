# Bharat-Bench

Bharat-Bench is an evaluation benchmark designed to assess AI models on Indian-context tasks.

The project focuses on evaluating model performance across different domains using a structured evaluation harness and multiple scoring methods.

## Project Goals

- Evaluate AI models on Indian-context questions.
- Support multiple benchmark domains.
- Use different scoring methods for different question types.
- Calculate overall benchmark performance.
- Calculate domain-wise performance.
- Store evaluation results in JSON format.

## Benchmark Domains

Bharat-Bench currently supports the following domains:

1. Compliance
2. Schemes
3. Mobility
4. Curriculum

## Question Types

The benchmark supports different types of questions:

- MCQ
- Short Factual
- Numerical
- Open Answer
- Unanswerable

## Scoring System

Different question types use different scoring methods.

### Exact Match

Used for:

- MCQ
- Short factual questions

### Numeric Tolerance

Used for:

- Numerical questions

### Rubric Scoring

Used for:

- Open-ended answers

### Refusal Checking

Used for:

- Unanswerable questions

## Evaluation Pipeline

The Bharat-Bench evaluation process works as follows:

Dataset
    ↓
Load JSONL Questions
    ↓
Get Model Answer
    ↓
Identify Question Type
    ↓
Apply Appropriate Scorer
    ↓
Calculate Individual Score
    ↓
Calculate Domain-wise Score
    ↓
Calculate Overall Score
    ↓
Save Results

## Project Structure

Bharat-Bench/
│
├── compliance/
│   └── questions.jsonl
│
├── schemes/
│   └── questions.jsonl
│
├── mobility/
│   └── questions.jsonl
│
├── curriculum/
│   └── questions.jsonl
│
├── harness/
│   ├── run.py
│   ├── results.json
│   └── scorers/
│       ├── exact_match.py
│       ├── numeric_tolerance.py
│       ├── rubric.py
│       └── refusal.py
│
├── items/
│   └── schema.json
│
├── spec/
│   └── taxonomy.md
│
└── README.md

## Running the Evaluation

Open the terminal in the harness directory.

Run:

    python run.py

The evaluation harness loads benchmark questions, evaluates model answers, calculates scores, and saves the final output in:

    results.json

## Output

The evaluation results contain:

- Total number of evaluated items
- Overall benchmark score
- Domain-wise scores
- Individual question results
- Question type
- Evaluation status

## Future Improvements

Future versions of Bharat-Bench can include:

- Direct AI model API integration
- Automated model evaluation
- Multiple model comparison
- Leaderboard generation
- Advanced reporting and visualizations
- Human evaluation support

## Conclusion

Bharat-Bench provides a structured framework for evaluating AI models on Indian-context tasks. It combines domain-specific benchmark datasets with question-type-specific scoring methods to provide detailed and interpretable evaluation results.