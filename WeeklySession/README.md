# Agent Orchestration

> Quickstart example to build a single-agent LLM-powered application using AgentChat.This example uses the OpenAI Large Language Models.
---
1. Python Installation
2. Create and Activate a Virtual Environment
3. Install Packages
4. Set an environment variable called `OPENAI_API_KEY`

### [1]-Python Installation



#### Windows
1. **Download Python** from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Run the installer** and check the box **"Add Python to PATH"** before proceeding with the installation.

3. **Check Python Version**
   ```sh
   python --version
   ```

---

### [2]-Create and Activate a Virtual Environment


1. **Navigate to your project directory**
   ```sh
   cd C:\path\to\your\project
   ```

2. **Create a virtual environment**
   ```sh
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   ```sh
   .venv\Scripts\activate
   ```

4. **Verify that the virtual environment is active** (Command Prompt should show `(venv)` before the directory path).


### [3]-Package Installation


```sh
pip install -r requirements.txt
pip install -U "autogen-agentchat" "autogen-ext[openai, azure]"
```

---

## Exiting the Virtual Environment
Simply run:
```sh
deactivate
```

### [4]-OpenAI API Key


#### 1. Setting Up OpenAI Secret Key  
1. Create an OpenAI Account[OpenAI's API Keys page](https://platform.openai.com/signup/)
2. Go to [OpenAI's API Keys page](https://platform.openai.com/settings/organization/api-keys).
3. Click **Create new secret key** and copy it. 
4. Keep it safe.

####  2. Set Up the API Key Locally  
You can open .env.example file, copy your key there and then rename the file to .env


### -Start the app

```sh
python main.py
```

