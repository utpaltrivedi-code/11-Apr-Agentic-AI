from crewai import Task
from agents.feedback_agents import classifier_agent, bug_analyzer_agent, feature_extractor_agent, ticket_creator_agent, quality_critic_agent

def create_pipeline_tasks(feedback_text: str, source_type: str):
    t1 = Task(description=f"Classify this {source_type}: '{feedback_text}' into Bug, Feature Request, Praise, Complaint, or Spam.", expected_output="JSON with 'category' and 'confidence'.", agent=classifier_agent)
    t2 = Task(description=f"If Bug, extract device, OS, steps, severity from: '{feedback_text}'. Else 'N/A'.", expected_output="JSON with tech details.", agent=bug_analyzer_agent)
    t3 = Task(description=f"If Feature Request, extract summary and impact from: '{feedback_text}'. Else 'N/A'.", expected_output="JSON with feature details.", agent=feature_extractor_agent)
    t4 = Task(description=f"Using previous analysis, create a structured ticket for '{feedback_text}'.", expected_output="JSON with title, description, category, priority, technical_details.", agent=ticket_creator_agent)
    t5 = Task(description="Review the generated ticket for clarity.", expected_output="Final JSON ticket with quality_score.", agent=quality_critic_agent)
    return [t1, t2, t3, t4, t5]