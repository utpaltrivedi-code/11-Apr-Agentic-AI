import pandas as pd
import os

def load_feedback_data():
    feedback_items = []
    if os.path.exists("data/app_store_reviews.csv"):
        df = pd.read_csv("data/app_store_reviews.csv").fillna("")
        for _, row in df.iterrows():
            feedback_items.append({"source_id": row["review_id"], "source_type": "App Store Review", "text": row["review_text"], "platform": row.get("platform", "Unknown")})
    if os.path.exists("data/support_emails.csv"):
        df = pd.read_csv("data/support_emails.csv").fillna("")
        for _, row in df.iterrows():
            feedback_items.append({"source_id": row["email_id"], "source_type": "Support Email", "text": f"Subject: {row.get('subject', '')} | Body: {row['body']}", "platform": "Email"})
    return feedback_items