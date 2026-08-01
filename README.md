# 🇮🇳 Bharat-Bench

**Bharat-Bench** is an AI evaluation benchmark designed for Indian public-domain tasks. It evaluates AI models across multiple domains such as government schemes, education curriculum, compliance, and mobility using standardized datasets and scoring methods.

## ✨ Features

- 📚 Multiple benchmark domains
  - Government Schemes
  - Education Curriculum
  - Compliance
  - Mobility
- ✅ Automatic evaluation harness
- 🎯 Multiple question types
  - MCQ
  - Short Factual
  - Numerical
  - Open Answer
  - Unanswerable
- 📊 Domain-wise scoring
- 📈 Overall benchmark score
- 💾 JSON result generation

## 📂 Project Structure

```
Bharat-Bench/
│
├── harness/
│   ├── run.py
│   └── scorers/
│       ├── exact_match.py
│       ├── numeric_tolerance.py
│       ├── refusal.py
│       └── rubric.py
│
├── spec/
│   └── items/
│       ├── schemes/
│       ├── curriculum/
│       ├── compliance/
│       └── mobility/
│
├── results.json
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/kaushikyogesh/Bharat-bench.git
```

Move into the project

```bash
cd Bharat-bench
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Evaluation

Example:

```bash
python harness/run.py spec/items/curriculum/questions.jsonl
```

Or

```bash
python harness/run.py spec/items/schemes/questions.jsonl
```

---

## 📊 Sample Output

```text
Evaluation completed successfully.

Total Evaluated Items: 3

Overall Score: 100%

Domain Scores:

Curriculum : 100%
```

---

## 🛠 Technologies Used

- Python
- JSONL Dataset
- AI Evaluation Harness
- Git
- GitHub

---

## 📌 Future Improvements

- Gemini API Integration
- OpenAI API Integration
- Automatic Model Evaluation
- Leaderboard
- Web Dashboard
- Multi-language Support

---

## 👨‍💻 Author

**Yogesh Kaushik**

AI/ML & Data Analytics

GitHub:
https://github.com/kaushikyogesh

LinkedIn:
https://linkedin.com/in/yogesh-kaushik-8733a8349

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.