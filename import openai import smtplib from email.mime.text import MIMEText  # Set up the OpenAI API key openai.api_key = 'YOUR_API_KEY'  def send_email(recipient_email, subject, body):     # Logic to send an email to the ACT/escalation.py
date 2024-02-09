import openai
import smtplib
from email.mime.text import MIMEText

# Set up the OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def send_email(recipient_email, subject, body):
    # Logic to send an email to the ACT/PCT owners
    # Example implementation using smtplib
    
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = 'sender@example.com'
    message['To'] = recipient_email
    
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.login('username', 'password')
        server.send_message(message)

def escalate_issue(defect_details, occurrence_count, threshold):
    # Logic to escalate the issue if it occurs more than a configured number of times
    
    if occurrence_count > threshold:
        act_owner_email = 'act_owner@example.com'
        pct_owner_email = 'pct_owner@example.com'
        subject = f"Issue Escalation - Defect ID: {defect_details['id']}"
        body = f"Defect ID: {defect_details['id']}\n\nDefect description: {defect_details['description']}\n\nOccurrence count: {occurrence_count}\n\nPlease review the defect and take necessary action."
        send_email(act_owner_email, subject, body)
        send_email(pct_owner_email, subject, body)

# Example usage
defect_details = {
    'id': 1234,
    'description': 'Some description of the defect'
}
occurrence_count = 5
threshold = 3

escalate_issue(defect_details, occurrence_count, threshold)
