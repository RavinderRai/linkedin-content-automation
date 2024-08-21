from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from linkedin.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class LinkedinCrew():
	"""Linkedin crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def content_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['content_strategist'],
			#tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def social_media_planner(self) -> Agent:
		return Agent(
			config=self.agents_config['social_media_planner'],
			verbose=True
		)
	
	@agent
	def ghostwriter(self) -> Agent:
		return Agent(
			config=self.agents_config['ghostwriter'],
			verbose=True
		)

	@task
	def content_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_generation'],
			agent=self.content_strategist()
		)
	
	@task
	def hooks_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['hooks_generation'],
			agent=self.social_media_planner(),
			output_file="hooks.md"
		)
	
	@task
	def linkedin_post_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['linkedin_post_generation'],
			agent=self.ghostwriter(),
			output_file="linkedin_posts.md"
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the Linkedin crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)