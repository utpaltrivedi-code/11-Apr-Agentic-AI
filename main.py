import json
from utils.csv_reader import load_feedback_data
from utils.logger import log_action, init_logger
from utils.db_setup import init_db, get_session, Ticket
from agents.crew import run_feedback_crew

def process_all_feedback():
    print("🚀 Initializing Database and Logs...")
    init_db()
    init_logger()
    session = get_session()

    print("📥 Loading Feedback from CSVs...")
    feedback_items = load_feedback_data()
    print(f"Found {len(feedback_items)} items to process.")

    for item in feedback_items:
        source_id = item["source_id"]
        source_type = item["source_type"]
        text = item["text"]
        
        print(f"\n--- Processing {source_type}: {source_id} ---")
        log_action("System", source_id, "Started Processing")
        
        try:
            result = run_feedback_crew(text, source_type)
            raw_output = result.raw.strip().strip('```json').strip('```')
            ticket_data = json.loads(raw_output)
            
            db_ticket = Ticket(
                source_id=source_id,
                source_type=source_type,
                category=ticket_data.get("category", "Unknown"),
                priority=ticket_data.get("priority", "Medium"),
                title=ticket_data.get("title", "Untitled Ticket"),
                description=ticket_data.get("description", ""),
                technical_details=str(ticket_data.get("technical_details", "")),
                status="open"
            )
            session.add(db_ticket)
            session.commit()
            
            log_action("Ticket Creator Agent", source_id, "Ticket Saved to DB", f"Title: {db_ticket.title}")
            print(f"✅ Successfully created ticket: {db_ticket.title}")
            
        except Exception as e:
            print(f"❌ Error processing {source_id}: {str(e)}")
            log_action("System", source_id, "Error", str(e))

    session.close()
    print("\n🎉 All feedback processed successfully!")

if __name__ == "__main__":
    process_all_feedback()