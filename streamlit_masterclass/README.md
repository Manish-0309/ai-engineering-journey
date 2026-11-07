# Streamlit — Complete Learning Journey

A hands-on journey to learning Streamlit, starting from the fundamentals and progressing towards building production-ready data science, machine learning and Generative AI applications.

This repository contains my Streamlit learning notes, code examples, practical exercises and projects.

The goal is not just to learn Streamlit functions but to understand how Streamlit works internally, how its components interact, and how to build useful applications with Python.

---

# Table of Contents

1. [Introduction to Streamlit](#1-introduction-to-streamlit)
2. [Why Streamlit?](#2-why-streamlit)
3. [How Streamlit Works](#3-how-streamlit-works)
4. [Environment Setup](#4-environment-setup)
5. [Understanding the Streamlit Execution Model](#5-understanding-the-streamlit-execution-model)
6. [Understanding Reruns](#6-understanding-reruns)
7. [Normal Python Variables vs Session State](#7-normal-python-variables-vs-session-state)
8. [Introduction to Session State](#8-introduction-to-session-state)
9. [Practical Projects](#9-practical-projects)
10. [Streamlit Files in This Folder](#10-streamlit-files-in-this-folder)
11. [Common Mistakes and Troubleshooting](#11-common-mistakes-and-troubleshooting)
12. [Important Commands](#12-important-commands)
13. [Learning Roadmap](#13-learning-roadmap)

---

# 1. Introduction to Streamlit

Streamlit is an open-source Python framework used to build interactive web applications.

It is particularly useful for data scientists, machine learning engineers and AI engineers who want to convert Python scripts, data analysis workflows and ML models into interactive web applications.

Traditionally, building a web application requires knowledge of multiple technologies:

- HTML for page structure.
- CSS for styling.
- JavaScript for frontend interactions.
- Backend frameworks such as Flask, Django or FastAPI.
- APIs to connect the frontend and backend.

Streamlit simplifies much of this process.

Instead of manually creating a frontend, we can write Python code and use Streamlit's built-in functions to generate the web interface.

For example:

```python
import streamlit as st

st.title("My First Streamlit Application")

st.write("Hello, welcome to Streamlit!")
```

That's enough to create a simple webpage.

**The biggest advantage:** We can build interactive applications without needing to become frontend developers first.

# 2. Why Streamlit?

Streamlit is useful in several areas.

| Domain | Application |
|---|---|
| Data Science | Exploratory Data Analysis dashboards |
| Machine Learning | Model prediction applications |
| Deep Learning | Image classification interfaces |
| Generative AI | LLM-powered chatbots |
| RAG | Document question-answering applications |
| Business Analytics | Interactive business dashboards |
| Data Engineering | Data monitoring interfaces |

### Example: Machine Learning Application

Imagine we have trained a house price prediction model.

The model accepts:

- Area of the house.
- Number of bedrooms.
- Location.
- Other relevant features.

It returns a predicted house price.

Instead of asking users to execute Python scripts, we can create an interface where they enter these values and receive predictions.

Streamlit makes building this interface straightforward.

**Important limitation:** Streamlit is particularly good for data applications, internal tools, demonstrations and AI prototypes. However, applications requiring highly customized frontend experiences or complex web architectures may be better served by dedicated frontend and backend frameworks.

# 3. How Streamlit Works

At a high level, Streamlit applications follow this architecture:

```text
Python Script
     |
     v
Streamlit Server
     |
     v
Web Browser
```

### Step-by-step execution

1. We write Python code in a `.py` file.
2. Streamlit executes the Python script.
3. Streamlit converts the output into an interactive web interface.
4. The browser displays the application.
5. Users interact with widgets.
6. Streamlit normally reruns the Python script when widgets change.

The important thing to remember is that Streamlit manages much of the communication between Python and the browser.

We primarily focus on writing Python code and defining application behaviour.

# 4. Environment Setup

Our development environment:

- Operating System: Windows 11
- Code Editor: Visual Studio Code
- Programming Language: Python
- Framework: Streamlit
- Terminal: PowerShell

## 4.1 Verify Python installation

Open the VS Code terminal.

Shortcut:

```text
Ctrl + `
```

Check Python:

```powershell
python --version
```

Check pip:

```powershell
python -m pip --version
```

Python must be installed before proceeding.

Use a Python version currently supported by the Streamlit release you intend to install.

## 4.2 Create a project directory

```powershell
mkdir streamlit-masterclass
cd streamlit-masterclass
```

Open the project in VS Code:

```powershell
code .
```

## 4.3 Create a virtual environment

A virtual environment isolates dependencies belonging to a particular project.

For example, two projects might require different versions of Pandas.

Without isolated environments, package conflicts can occur.

Create a virtual environment:

```powershell
python -m venv .venv
```

Here:

- `python`: Executes Python.
- `-m`: Executes a Python module.
- `venv`: Python's built-in virtual environment module.
- `.venv`: Name of the environment directory.

## 4.4 Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

After activation, the terminal should display something similar to:

```text
(.venv) PS C:\projects\streamlit-masterclass>
```

The `(.venv)` prefix indicates that the environment is active.

If PowerShell blocks activation, troubleshoot the execution policy rather than unnecessarily changing system-wide security settings. Command Prompt activation is another option.

## 4.5 Install Streamlit

First, upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install Streamlit:

```powershell
python -m pip install streamlit
```

Verify the installation:

```powershell
python -m streamlit version
```

## 4.6 Test the installation

Streamlit provides a built-in demonstration application.

Run:

```powershell
python -m streamlit hello
```

The browser should open the Streamlit demonstration.

The default local address is generally:

```text
http://localhost:8501
```

`localhost` refers to your own computer.

`8501` is Streamlit's default application port.

Stop the application using:

```text
Ctrl + C
```


# 5. Understanding the Streamlit Execution Model

This is one of the most important concepts in Streamlit.

In a regular Python script, code executes from top to bottom.

Example:

```python
print("Hello")

x = 10

print(x)
```

The script executes and finishes.

Streamlit behaves differently because it needs to respond to user interactions.

**Streamlit normally reruns the entire Python script when a user interacts with a widget.**

This behaviour is called a rerun.

# 6. Understanding Reruns
Streamlit normally reruns the script.

During the new execution:

### What triggers reruns?

| User action | Behaviour |
|---|---|
| Enter text in a text input | Rerun |
| Change a slider | Rerun |
| Select a checkbox | Rerun |
| Click a button | Rerun |
| Change a select box | Rerun |

An important exception is widgets inside forms.

Individual changes inside a form generally do not trigger a script rerun. The values are submitted together when the form is submitted.

We will study forms in a later lesson.

# 7. Normal Python Variables vs Session State

Let's understand a common beginner mistake.

Consider this counter:

```python
import streamlit as st

st.title("Counter Application")

count = 0

if st.button("Increment"):
    count = count + 1

st.write("Count:", count)
```

Expected behaviour might be:

- First click: 1
- Second click: 2
- Third click: 3

But the counter displays 1 after every click.

### Why?

Because every button click triggers a rerun.

During every execution:

```python
count = 0
```

runs again.

Then the button increments it to 1.

Therefore, the value never accumulates.

**Important lesson:** Normal Python variables do not automatically preserve their values across Streamlit reruns.

# 8. Introduction to Session State

Streamlit provides Session State to preserve values across reruns within a user's session.

We access it using:

```python
st.session_state
```

Think of Session State as a temporary storage area associated with an individual user's application session.

| Normal Python variable | Session State |
|---|---|
| Exists during script execution | Persists across reruns |
| Can be reinitialized during reruns | Retains stored values |
| Not suitable for persistent counters | Suitable for counters |
| Regular Python variable | Streamlit-managed state |

**Important:** Session State is not permanent storage. Its values can be lost when a session ends or is recreated.

For permanent storage, we need databases or other persistent storage solutions.



# 9. Practical Projects

These exercises are the first practical applications built while learning Streamlit.

## Project 1: Personal Profile Dashboard
This project focuses on basic user input, profile creation and simple dashboard design.

Key files:

- `profile_generator.py` — collects user details such as name, age, role, skills and experience, then displays a generated profile.
- `personal_profile_dashboard.py` — creates a personal dashboard with about-me text, skills and a small project summary.

## Project 2: Counter Application
This project demonstrates why normal Python variables are not enough in Streamlit.

Key file:

- `counter.py` — uses `st.session_state` to store and update a count across reruns.

## Project 3: Input Widgets and Data Display
This project explores widgets and data presentation.

Key files:

- `input_widgets.py` — shows `text_input()`, `text_area()`, `number_input()`, `slider()`, `selectbox()`, `multiselect()`, `checkbox()`, `radio()` and `button()`.
- `data_practice.py` — builds a mini sales dashboard using Pandas and `st.metric()`, `st.dataframe()` and `st.table()`.
- `displaying_data.py` — demonstrates `st.dataframe()`, `st.table()`, `st.image()` and `st.json()`-style data display patterns.

## Project 4: First Streamlit App
The first application used to validate that Streamlit is correctly installed and running.

Key file:

- `app.py` — minimal "Hello, welcome to Streamlit" app with a success message.

# 10. Streamlit Files in This Folder

This folder contains the core learning files for the Streamlit masterclass.

| File | Purpose |
|---|---|
| `app.py` | First working Streamlit app and installation verification |
| `counter.py` | Session state counter example |
| `input_widgets.py` | Demonstrates common user input widgets |
| `data_practice.py` | Basic analytics dashboard with sales metrics |
| `displaying_data.py` | Data presentation using tables, images and text |
| `profile_generator.py` | User profile generator app |
| `personal_profile_dashboard.py` | Personal portfolio/profile dashboard |
| `requirements.txt` | Python dependencies required for this project |
| `.gitignore` | Ignores local virtual environments and cache files |

Run an app using:

```powershell
python -m streamlit run app.py
```

Or run a specific exercise:

```powershell
python -m streamlit run counter.py
python -m streamlit run input_widgets.py
python -m streamlit run profile_generator.py
```

# 11. Common Mistakes and Troubleshooting

| Problem | Explanation / Solution |
|---|---|
| Streamlit command not recognized | Use `python -m streamlit` |
| No module named streamlit | Activate the correct environment and install Streamlit |
| Counter resets after every click | Use Session State |
| Application port already in use | Run on another port |
| PowerShell blocks activation | Troubleshoot activation or use Command Prompt |
| VS Code uses the wrong Python | Select the `.venv` interpreter |
| Dependencies missing | Install from requirements.txt |

### Running on another port

```powershell
python -m streamlit run app.py --server.port 8502
```
# 12. Important Commands

| Command | Purpose |
|---|---|
| `python --version` | Check Python version |
| `python -m pip --version` | Check pip version |
| `python -m venv .venv` | Create virtual environment |
| `.venv\Scripts\Activate.ps1` | Activate environment in PowerShell |
| `python -m pip install streamlit` | Install Streamlit |
| `python -m streamlit version` | Check Streamlit version |
| `python -m streamlit hello` | Run built-in demo |
| `python -m streamlit run app.py` | Run application |
| `python -m pip install -r requirements.txt` | Install project dependencies |
| `Ctrl + C` | Stop running application |

---

# 13. Learning Roadmap

This is the roadmap we'll follow throughout the course.

## Phase 1: Streamlit Fundamentals

- [x] Lesson 1: Introduction to Streamlit
- [x] Lesson 2: Installation and Environment Setup
- [x] Lesson 3: Your First Streamlit Application
- [x] Lesson 4: Execution Model and Reruns
- [x] Lesson 5: Displaying Text, Data and Messages
- [x] Lesson 6: Buttons, Checkboxes and User Inputs

## Phase 2: Layout and UI Components

- [ ] Columns and Containers
- [ ] Sidebar
- [ ] Tabs, Expanders and Popovers
- [ ] Forms
- [ ] Session State in Depth
- [ ] Callbacks

## Phase 3: Working with Data

- [ ] DataFrames and Tables
- [ ] Charts and Visualizations
- [ ] File Upload and Download
- [ ] Working with CSV, Excel and JSON
- [ ] Interactive Filters
- [ ] Caching with `st.cache_data` and `st.cache_resource`

## Phase 4: Advanced Streamlit

- [ ] Multipage Applications
- [ ] Navigation and Routing
- [ ] Custom CSS and HTML
- [ ] Themes and UI Customization
- [ ] API Integration
- [ ] Database Integration
- [ ] Authentication and Authorization
- [ ] Error Handling and Debugging

## Phase 5: AI and Production Applications

- [ ] Integrating Machine Learning Models
- [ ] Integrating Deep Learning Models
- [ ] Building LLM Applications
- [ ] Vector Database Integration
- [ ] RAG Applications
- [ ] Deployment
- [ ] Performance Optimization
- [ ] Security and Production Best Practices

## Phase 6: End-to-End Projects

- [ ] Data Analysis Dashboard
- [ ] Machine Learning Prediction Application
- [ ] PDF Question-Answering Application
- [ ] LLM Chatbot
- [ ] RAG-Based Document Assistant
- [ ] End-to-End AI Application

---

# Useful Resources

- [Official Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Installation Guide](https://docs.streamlit.io/get-started/installation)
- [Streamlit API Reference](https://docs.streamlit.io/develop/api-reference)
- [Streamlit Community](https://discuss.streamlit.io/)
- [Streamlit GitHub Repository](https://github.com/streamlit/streamlit)

---

# Final Note

The idea behind this repository is simple: learn by building.

We will cover one topic at a time, understand the concepts, write code, build small applications and gradually move towards real-world AI applications.

Rather than memorizing Streamlit functions, the focus will be on understanding why and when to use them.

**One lesson, one concept, one practical implementation at a time.**
