# Linkedin Crew

Welcome to the Linkedin Crew project, powered by [crewAI](https://crewai.com). This project automates the process of generating LinkedIn content, and follows Lara Acosta's strategy that you can find in this video: https://www.youtube.com/watch?v=wYBObTusysQ. So you can either follow the advice in her video, which may be a bit tedious, or just run this program and generate the content yourself, with nothing more than a description of yourself/personal brand. Thus, in a way, this project allows you to create an AI Lara Acosta who will write viral LinkedIn content based on her own advice.

The way it works is it uses 3 different AI agents to perform 3 different tasks. It sequentially runs through this process and ends with markdown files containing your viral LinkedIn posts that you can then edit yourself. See the image below for a graphical representation. Also, to make this even better, try cloning this repo and changing the prompts yourself - there are some example posts (for few-shot learning) that could be improved by catering to your niche.

<img src="LinkedInAutomationImage.png" alt="AI Agents Framework" width="600">


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/linkedin/config/agents.yaml` to define your agents
- Modify `src/linkedin/config/tasks.yaml` to define your tasks
- Modify `src/linkedin/crew.py` to add your own logic, tools and specific args
- Modify `src/linkedin/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
poetry run linkedin
```

This command initializes the linkedin Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The linkedin Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Linkedin Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
