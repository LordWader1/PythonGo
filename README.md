# PythonGo
Learn Python From Basic To Advance

<div align="center">

# 🐍 Python Learning Journey

**Learn Python step by step: notes, exercises, and projects, all in one place.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-learning%20in%20progress-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![PRs](https://img.shields.io/badge/PRs-welcome-orange)

[Roadmap](#-roadmap) · [Progress Tracker](#-progress-tracker) · [Getting Started](#-getting-started) · [Project Structure](#-project-structure) · [Resources](#-resources) · [Contributing](#-contributing)

</div>

---

## 📖 About This Repository

This repository is my personal Python learning log. I write code here every day, keep short notes on what I learn, solve exercises, and build small projects. Everything is public so that:

- I stay **consistent** and can see my own progress over time.
- Other beginners can **follow along**, copy ideas, and learn from my mistakes.
- Anyone can **review my code** and suggest improvements.

> **Goal:** go from absolute beginner to building real Python projects, one small step at a time.

If you are new to programming too, you are in the right place. Fork this repo, follow the roadmap, and make it your own.

---

## 🗺 Roadmap

The course is split into **5 stages**. Each topic has its own folder with notes (`README.md`), examples, and exercises.

### Stage 1: Python Basics (Days 1–10)

| Day | Topic | What you will learn |
|:---:|-------|---------------------|
| 01 | [Introduction](./01_introduction) | What Python is, installing it, running your first script |
| 02 | [Variables & Data Types](./02_variables_and_data_types) | `int`, `float`, `str`, `bool`, type conversion |
| 03 | [Operators](./03_operators) | Arithmetic, comparison, logical, and assignment operators |
| 04 | [Strings](./04_strings) | Indexing, slicing, methods, f-strings |
| 05 | [Lists](./05_lists) | Creating, changing, and looping through lists |
| 06 | [Tuples & Sets](./06_tuples_and_sets) | Immutable sequences, unique collections, set operations |
| 07 | [Dictionaries](./07_dictionaries) | Key–value data, nested dictionaries |
| 08 | [Conditionals](./08_conditionals) | `if`, `elif`, `else`, ternary expressions |
| 09 | [Loops](./09_loops) | `for`, `while`, `break`, `continue`, `range()` |
| 10 | [Review & Mini Project](./10_review_project) | Putting Stage 1 together |

### Stage 2: Functions & Code Organization (Days 11–18)

| Day | Topic | What you will learn |
|:---:|-------|---------------------|
| 11 | [Functions](./11_functions) | Parameters, return values, default arguments |
| 12 | [Modules & Packages](./12_modules_and_packages) | `import`, the standard library, `pip` |
| 13 | [List Comprehensions](./13_comprehensions) | Concise list, set, and dict creation |
| 14 | [Lambda, Map, Filter](./14_functional_tools) | Higher-order functions |
| 15 | [Scope & Recursion](./15_scope_and_recursion) | Local vs global variables, recursive thinking |
| 16 | [Date & Time](./16_datetime) | `datetime`, formatting, time deltas |
| 17 | [Error Handling](./17_error_handling) | `try`, `except`, `finally`, raising errors |
| 18 | [Review & Mini Project](./18_review_project) | Putting Stage 2 together |

### Stage 3: Working with Data (Days 19–25)

| Day | Topic | What you will learn |
|:---:|-------|---------------------|
| 19 | [File Handling](./19_file_handling) | Reading and writing text files |
| 20 | [JSON & CSV](./20_json_and_csv) | Structured data formats |
| 21 | [Regular Expressions](./21_regex) | Pattern matching with `re` |
| 22 | [Virtual Environments](./22_virtual_environments) | `venv`, `requirements.txt` |
| 23 | [HTTP & APIs](./23_http_and_apis) | The `requests` library, working with web APIs |
| 24 | [Web Scraping](./24_web_scraping) | BeautifulSoup basics, scraping responsibly |
| 25 | [Review & Mini Project](./25_review_project) | Putting Stage 3 together |

### Stage 4: Object-Oriented Programming (Days 26–30)

| Day | Topic | What you will learn |
|:---:|-------|---------------------|
| 26 | [Classes & Objects](./26_classes_and_objects) | Attributes, methods, `__init__` |
| 27 | [Inheritance](./27_inheritance) | Parent/child classes, `super()` |
| 28 | [Dunder Methods & Properties](./28_dunder_and_properties) | `__str__`, `__repr__`, `@property` |
| 29 | [Decorators & Generators](./29_decorators_and_generators) | Reusable wrappers, lazy iteration |
| 30 | [Testing](./30_testing) | Writing tests with `pytest` |

### Stage 5: Projects & Beyond

| Project | Description | Skills used |
|---------|-------------|-------------|
| [Number Guessing Game](./projects/guessing_game) | Terminal game with hints and scoring | Loops, conditionals, `random` |
| [To-Do List CLI](./projects/todo_cli) | Add, list, and complete tasks, saved to a file | Functions, files, JSON |
| [Weather App](./projects/weather_app) | Fetch the forecast for any city | APIs, error handling |
| [Expense Tracker](./projects/expense_tracker) | Track spending and show summaries | OOP, CSV, `datetime` |
| [Telegram Bot](./projects/telegram_bot) | A simple chat bot | APIs, async, environment variables |

---

## ✅ Progress Tracker

Tick a box when you finish a stage. (On GitHub you can click the checkboxes in your own fork.)

- [ ] Stage 1: Python Basics
- [ ] Stage 2: Functions & Code Organization
- [ ] Stage 3: Working with Data
- [ ] Stage 4: Object-Oriented Programming
- [ ] Stage 5: Projects

**Current streak:** `0 days` · **Started on:** `YYYY-MM-DD`

---

## 🚀 Getting Started

### 1. Install Python

Download Python 3.10 or newer from [python.org/downloads](https://www.python.org/downloads/). Check that it works:

```bash
python --version
```

On some systems the command is `python3`.

### 2. Clone this repository

```bash
git clone https://github.com/aayush700/<your-repo-name>.git
cd <your-repo-name>
```

> Replace `<your-repo-name>` with the actual name of this repository.

### 3. (Recommended) Create a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 4. Install dependencies (only for later days and projects)

```bash
pip install -r requirements.txt
```

### 5. Run any example

```bash
python 01_introduction/hello.py
```

### Recommended editors

- [VS Code](https://code.visualstudio.com/) with the Python extension
- [PyCharm Community](https://www.jetbrains.com/pycharm/)
- [Thonny](https://thonny.org/) (very friendly for absolute beginners)

---

## 📁 Project Structure

```
python-learning/
│
├── 01_introduction/
│   ├── README.md        # Notes for the day
│   ├── examples.py      # Code examples
│   └── exercises.py     # Practice problems
├── 02_variables_and_data_types/
│   └── ...
├── ...
├── projects/
│   ├── guessing_game/
│   ├── todo_cli/
│   └── ...
├── cheatsheets/         # One-page summaries
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md            # You are here
```

Each topic folder follows the same pattern, so you always know where to look.

---

## 🧠 How I Study (and How You Can Too)

1. **Read** the notes for the topic.
2. **Type** every example yourself. Don't copy and paste.
3. **Change** the code and break it on purpose to see what happens.
4. **Solve** the exercises without looking at the answers.
5. **Commit** your work with a clear message.
6. **Review** the previous day for 5 minutes before starting a new topic.

Small progress every day beats a big push once a month.

### Commit message style

```bash
git add .
git commit -m "Day 05: add list exercises and notes"
git push
```

---

## 📚 Resources

**Official**
- [Python Documentation](https://docs.python.org/3/)
- [The Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8: Style Guide](https://peps.python.org/pep-0008/)

**Free courses & books**
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Python for Everybody](https://www.py4e.com/)
- [Real Python](https://realpython.com/)
- [freeCodeCamp: Python](https://www.freecodecamp.org/)

**Practice**
- [Exercism: Python Track](https://exercism.org/tracks/python)
- [HackerRank: Python](https://www.hackerrank.com/domains/python)
- [LeetCode](https://leetcode.com/)
- [Codewars](https://www.codewars.com/)

**Tools**
- [Python Tutor](https://pythontutor.com/): visualize how your code runs
- [Black](https://black.readthedocs.io/): automatic code formatter
- [pytest](https://docs.pytest.org/): testing framework

---

## 🤝 Contributing

Suggestions are very welcome. If you spot a mistake or have a better way to write something:

1. **Fork** this repository.
2. Create a branch: `git checkout -b fix/day-05-typo`
3. Make your changes and commit them.
4. Push the branch and open a **Pull Request**.

You can also open an [Issue](../../issues) for questions, ideas, or corrections.

Please keep code beginner-friendly, with clear variable names and short comments.

---

## ❓ FAQ

**Do I need any programming experience?**
No. Stage 1 starts from zero.

**How long does it take?**
About 30 days at 1–2 hours a day, but go at your own pace.

**Can I use this to teach others?**
Yes. See the license below.

**Something doesn't run on my computer. What should I do?**
Check your Python version with `python --version`, activate your virtual environment, and open an issue with the full error message.

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE). You are free to use, copy, and share it. A link back is appreciated.

---

## 👤 Author

**Aayush**
GitHub: [@LordWader1](https://github.com/LordWader1)

If this repository helps you, please give it a ⭐ and share it with a friend who is learning Python.

<div align="center">

**Happy coding! 🐍**

</div>
