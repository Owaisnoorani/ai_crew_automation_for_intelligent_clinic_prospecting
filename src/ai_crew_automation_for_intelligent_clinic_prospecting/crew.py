from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, ScrapeElementFromWebsiteTool, SeleniumScrapingTool
from .config.llm_config import get_llm
from .tools.search_tool import CustomWebsiteSearchTool

@CrewBase
class AiCrewAutomationForIntelligentClinicProspectingCrew():
    """AiCrewAutomationForIntelligentClinicProspecting crew"""

    @agent
    def clinic_lead_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['clinic_lead_finder'],
            tools=[CustomWebsiteSearchTool()],
            llm=get_llm()
        )

    @agent
    def clinic_web_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['clinic_web_scraper'],
            tools=[ScrapeWebsiteTool(), ScrapeElementFromWebsiteTool(), SeleniumScrapingTool()],
            llm=get_llm()
        )

    @agent
    def clinic_data_classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['clinic_data_classifier'],
            tools=[],
            llm=get_llm()
        )

    @agent
    def clinic_data_validator(self) -> Agent:
        return Agent(
            config=self.agents_config['clinic_data_validator'],
            tools=[],
            llm=get_llm()
        )

    @agent
    def clinic_data_integrator(self) -> Agent:
        return Agent(
            config=self.agents_config['clinic_data_integrator'],
            tools=[],
            llm=get_llm()
        )

    @agent
    def clinic_task_scheduler(self) -> Agent:
        return Agent(
            config=self.agents_config['clinic_task_scheduler'],
            tools=[],
            llm=get_llm()
        )

    @task
    def clinic_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['clinic_search_task'],
            tools=[CustomWebsiteSearchTool()],
            llm=get_llm()
        )

    @task
    def clinic_web_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['clinic_web_extraction_task'],
            tools=[ScrapeWebsiteTool(), ScrapeElementFromWebsiteTool(), SeleniumScrapingTool()],
            llm=get_llm()
        )

    @task
    def clinic_data_classification_task(self) -> Task:
        return Task(
            config=self.tasks_config['clinic_data_classification_task'],
            tools=[],
            llm=get_llm()
        )

    @task
    def clinic_data_validation_task(self) -> Task:
        return Task(
            config=self.tasks_config['clinic_data_validation_task'],
            tools=[],
            llm=get_llm()
        )

    @task
    def clinic_data_storage_task(self) -> Task:
        return Task(
            config=self.tasks_config['clinic_data_storage_task'],
            tools=[],
            llm=get_llm()
        )

    @task
    def clinic_prospecting_automation_task(self) -> Task:
        return Task(
            config=self.tasks_config['clinic_prospecting_automation_task'],
            tools=[],
            llm=get_llm()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiCrewAutomationForIntelligentClinicProspecting crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
