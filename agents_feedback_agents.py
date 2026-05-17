from crewai import Agent
from agents.config import get_llm

llm_instance = get_llm()

classifier_agent = Agent(role="Feedback Classifier", goal="Categorize user feedback.", backstory="Expert triager.", llm=llm_instance, verbose=True)
bug_analyzer_agent = Agent(role="Bug Analyzer", goal="Extract tech details.", backstory="Senior QA.", llm=llm_instance, verbose=True)
feature_extractor_agent = Agent(role="Feature Extractor", goal="Extract feature requests.", backstory="Product Manager.", llm=llm_instance, verbose=True)
ticket_creator_agent = Agent(role="Ticket Creator", goal="Generate Jira tickets.", backstory="Scrum Master.", llm=llm_instance, verbose=True)
quality_critic_agent = Agent(role="Quality Critic", goal="Review tickets.", backstory="QA Director.", llm=llm_instance, verbose=True)