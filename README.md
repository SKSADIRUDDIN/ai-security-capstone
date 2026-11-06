# AI Security Capstone – Vulnerable-by-Design AI Chatbot

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-white)
![OWASP](https://img.shields.io/badge/OWASP-LLM_Top_10-red)

## 1. Project Overview

This project is a locally hosted AI-powered chatbot developed using Python Flask and Ollama.

The application uses the Llama 3.2 1B large language model to generate AI responses through a simple web-based chat interface.

This project was developed as part of an AI Application Security Capstone to understand, evaluate and test security risks associated with Large Language Model (LLM) applications.

The security assessment follows the OWASP Top 10 for LLM Applications 2023–2024 (Version 1.1).

## 2. Project Objectives

- Build and deploy a locally hosted AI chatbot.
- Integrate a locally running LLM using Ollama.
- Understand common security risks in LLM applications.
- Perform security testing using OWASP LLM Top 10 categories.
- Observe AI behaviour against different security test prompts.
- Document security findings and recommend remediation measures.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Ollama | Local LLM runtime |
| Llama 3.2 1B | Language model |
| HTML | Webpage structure |
| CSS | User interface styling |
| JavaScript | Chat functionality |
| Requests | Communication with Ollama API |
| Kali Linux | Security testing environment |
| Oracle VirtualBox | Virtual machine environment |

## 4. Project Structure

```text
ai-security-capstone/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

| File | Description |
|---|---|
| app.py | Flask application and chatbot interface |
| requirements.txt | Python dependencies |
| README.md | Project documentation |

## 5. Prerequisites

Before running the application, ensure that the following are installed:

- Python 3
- pip
- Ollama
- Llama 3.2 1B model
- Web browser

The application is designed for local execution.

## 6. Installation and Setup

### Step 1: Install Ollama

Download and install Ollama:

https://ollama.com/

Verify the installation:

```bash
ollama --version
```

### Step 2: Download the AI Model

Pull the Llama 3.2 1B model:

```bash
ollama pull llama3.2:1b
```

Verify the downloaded model:

```bash
ollama list
```

### Step 3: Clone the GitHub Repository

```bash
git clone https://github.com/SKSADIRUDDIN/ai-security-capstone.git
```

Navigate to the project directory:

```bash
cd ai-security-capstone
```

### Step 4: Create a Python Virtual Environment

```bash
python3 -m venv ai-lab
```

Activate the virtual environment on Linux or macOS:

```bash
source ai-lab/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Start Ollama

Ensure the Ollama service is running.

On systems where Ollama is managed as a service:

```bash
ollama serve
```

If Ollama is already running in the background, do not start another instance.

### Step 7: Run the Flask Application

```bash
python app.py
```

The application will run locally at:

http://127.0.0.1:5000

Open the URL in your web browser to access the chatbot.

## 7. API Configuration

The application communicates with the local Ollama API.

Default API endpoint:

```text
http://127.0.0.1:11434/api/generate
```

Default model:

```text
llama3.2:1b
```

The model and API endpoint can be configured using environment variables:

```bash
export OLLAMA_MODEL=llama3.2:1b
export OLLAMA_URL=http://127.0.0.1:11434/api/generate
```

## 8. Security Testing Methodology

The assessment involved:

1. Designing test prompts for the OWASP categories.
2. Submitting prompts through the chatbot interface.
3. Recording the exact prompts and model responses.
4. Observing whether the expected security behaviour occurred.
5. Evaluating the results and assigning severity.
6. Documenting recommended remediation measures.

**Note:** Prompt-based testing alone cannot establish the security of every underlying component. Some categories require additional source-code, dependency, configuration, permission or infrastructure reviews.

## 9. Security Observations

The application is a deliberately limited educational lab environment.

The following areas require additional security hardening:

- Input validation and request-size restrictions.
- Rate limiting and resource consumption controls.
- Safe handling of backend errors.
- Authentication and authorization where required.
- Dependency vulnerability scanning.
- Protection of model files and configuration.
- Secure management of external integrations.

## 10. Recommended Security Improvements

| OWASP Category | Recommended Improvement |
|---|---|
| LLM01 | Implement prompt-injection defences and input handling controls |
| LLM02 | Sanitize or safely encode untrusted output |
| LLM03 | Validate and protect training data pipelines |
| LLM04 | Apply rate limits, token limits and resource controls |
| LLM05 | Audit dependencies and pin trusted package versions |
| LLM06 | Prevent exposure of secrets and sensitive information |
| LLM07 | Apply strict permissions to external tools and plugins |
| LLM08 | Enforce least privilege and human approval for sensitive actions |
| LLM09 | Verify AI-generated information using trusted sources |
| LLM10 | Restrict access to model files and model download interfaces |

## 11. Troubleshooting

### Ollama connection error

Verify that Ollama is running:

```bash
ollama list
```

### Model not found

Download the model:

```bash
ollama pull llama3.2:1b
```

### Flask module not found

Activate the virtual environment and install dependencies:

```bash
source ai-lab/bin/activate
pip install -r requirements.txt
```

### Application not opening

Check that Flask is running and visit:

```text
http://127.0.0.1:5000
```

## 12. Project Deliverables

- Flask-based AI chatbot application.
- Python dependency file.
- Local Ollama model integration.
- OWASP LLM Top 10 security assessment.
- Security testing screenshots.
- Lab setup and installation documentation.
- Security findings and remediation recommendations.
