# Tutorial: Creating an AI Workflow with `crewai`

This tutorial demonstrates how to use the `crewai` library to set up a workflow involving AI agents, tasks, and a crew process to execute sequential actions.

---

## Prerequisites

1. **Python 3.10 or later** installed on your system.
2. An **OpenAI API Key** to interact with OpenAI's models or any other local model suitable for task.
3. The `crewai` library installed. Refer to the [Installation Guide](#installation).

---

## Step 1: Set Up Your Python Environment

### Install Required Packages
If you don’t have `crewai` installed, use the following command to install it:

```
pip install crewai

```
## Step 2: Configure your API Key

Add your OpenAI API Key to the environment:

```
import os

os.environ["OPENAI_API_KEY"] = "API_KEY"

```

Important: Replace "API_KEY" with your actual OpenAI API Key. Never share your API key publicly

## Step 3: Define your Agents

Agents are entities that handle specific tasks. In this example:

**Researcher**: Analyzes and researches AI trends.
**Reporting Analyst**: Converts research insights into a detailed report.

```
from crewai import Agent

researcher = Agent(
    role='Researcher',
    goal='Research new AI insights',
    backstory='You are an AI Research assistant',
    verbose=True,
    allow_delegation=False
)

Reporting_analyst = Agent(
    role='Reporting Analyst',
    goal='Create detailed reports based on latest AI insights, data analysis, and research findings',
    backstory='You are a meticulous analyst with a keen eye for detail.',
    verbose=True,
    allow_delegation=False
)

```

### Agent Class:

Represents an entity responsible for a specific role in the workflow.

### Parameters:

- role: Describes the agent's role in the process (e.g., "Researcher").
- goal: The primary objective the agent aims to achieve.
- backstory: A narrative that provides context for the agent's behavior or actions.
- verbose: If True, enables detailed logging of the agent's activities.
- allow_delegation: If False, prevents the agent from delegating its tasks to others.


## Step 4: Define Tasks

Tasks describe what each agent must accomplish.

```
from crewai import Task

task1 = Task(
    description='Investigate the latest AI trends',
    agent=researcher,
    expected_output='A comprehensive analysis of current AI trends and developments'
)

task2 = Task(
    description='Write a compelling blog post based on the latest AI trends',
    agent=Reporting_analyst,
    expected_output='A well-written blog post summarizing the AI trends research'
)

```

### Task Class:

Represents a specific job to be performed by an agent.

Parameters:

- description: A short description of the task.
- agent: Specifies which agent is responsible for this task.
- expected_output: Describes the expected result of the task.

Two Tasks:

- Task 1: Research the latest AI trends (assigned to the Researcher).
- Task 2: Write a blog post based on the research (assigned to the Reporting Analyst).



## Step 5: Create and Run the Crew Process

Combine agents and tasks into a crew. Define a process (e.g., sequential or parallel execution).

```
from crewai import Crew, Process

crew = Crew(
    agents=[researcher, Reporting_analyst],
    tasks=[task1, task2],
    verbose=True,
    process=Process.sequential
)

result = crew.kickoff()

```

### Crew Class:

Combines agents and tasks into a workflow.

Parameters:

- agents: A list of agents participating in the process.
- tasks: A list of tasks to be completed.
- verbose: Enables detailed logging of the crew's activities.
- process: Defines how tasks are executed. Here, Process.sequential ensures tasks are executed one after the other.

### crew.kickoff():

- Starts the workflow and executes tasks as defined by the process.


## Installation Guide: Setting Up Environment and Installing `crewai`

This guide walks you through setting up a virtual environment, installing `crewai`, and configuring your system for development.

---

## Step 1: Install Python 3.10 or Later

1. Check if Python is installed:
   ```
   python3 --version

   ```
   If Python is not installed, [Download Python](https://www.python.org/downloads/) and follow the installation instructions.


## Step 2: Set Up a Virtual Environment

Using a virtual environment ensures that your project dependencies are isolated from the global Python environment.

Create a virtual environment:

```
python3 -m venv myenv

```

Activate the virtual environment:

On macOS and Linux:
```
source myenv/bin/activate

```
On Windows:
```
myenv\Scripts\activate

```
Verify the virtual environment is active. Your terminal prompt should now display (myenv).


## Step 3: Install crewai

Install the crewai library using pip

```
pip install crewai

```

## Step 4: Verify Installation

Check if crewai and its dependencies were installed correctly:

```
pip list

```
You should see crewai and related packages listed.

## Step 5: Deactivate the Virtual Environment
```
deactivate

```
## Troubleshooting

Virtual Environment Not Found: Ensure you’re using the correct Python version:

```
python3 -m venv myenv

```

Permission Issues: Use the --user flag for installations:

```
pip install --user crewai

```

# Conclusion

In this tutorial, we explored how to set up and use the `crewai` library to design and execute AI-powered workflows. Here's a quick recap of what we covered:

1. **Installation**: Setting up a virtual environment and installing `crewai` along with its dependencies.
2. **Configuration**: Configuring your OpenAI API key to enable interaction with OpenAI's services.
3. **Defining Agents**: Creating AI agents with specific roles and goals to handle tasks.
4. **Defining Tasks**: Assigning well-defined tasks to agents, with clear objectives and expected outputs.
5. **Executing Workflows**: Using the `Crew` class to combine agents and tasks into a workflow, executed sequentially or in parallel.
6. **Reviewing Results**: Analyzing the outputs generated by the agents after task execution.

## Key Takeaways
- **Modular Design**: `crewai` provides a modular and intuitive framework to manage AI-based workflows, enabling you to focus on the logic and objectives.
- **Flexibility**: The ability to define roles, goals, and tasks allows for customization to suit diverse use cases.
- **Scalability**: With features like sequential and parallel task execution, `crewai` is suitable for workflows of varying complexity.

## Next Steps
You can now:
- Experiment with additional agents and tasks to create more complex workflows.
- Explore advanced features of `crewai`, such as delegation or custom process execution strategies.
- Integrate `crewai` into larger projects, automating repetitive tasks and enhancing productivity.

## Final Thoughts
The `crewai` library empowers developers to leverage AI in an organized and efficient manner. By breaking down workflows into manageable components, it simplifies the process of creating intelligent systems. Whether you're conducting research, generating reports, or building AI-driven applications, `crewai` can be a valuable addition to your toolkit.

Happy coding!









