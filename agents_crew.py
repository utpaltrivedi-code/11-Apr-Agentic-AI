from crewai import Crew, Process
from agents.feedback_agents import classifier_agent, bug_analyzer_agent, feature_extractor_agent, ticket_creator_agent, quality_critic_agent
from agents.tasks import create_pipeline_tasks

def run_feedback_crew(feedback_text: str, source_type: str):
    tasks = create_pipeline_tasks(feedback_text, source_type)
    crew = Crew(
        agents=[classifier_agent, bug_analyzer_agent, feature_extractor_agent, ticket_creator_agent, quality_critic_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    return crew.kickoff()