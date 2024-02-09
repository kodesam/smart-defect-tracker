import openai
import smtplib
from email.mime.text import MIMEText

# Set up the OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def send_email(recipient_email, subject, body):
    # Logic to send an email to the ACT product owner
    
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = 'sender@example.com'
    message['To'] = recipient_email
    
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.login('username', 'password')
        server.send_message(message)

def generate_email_content(defect_details):
    # Use OpenAI to generate the email content based on the defect details
    
    prompt = f"Defect ID: {defect_details['id']}\n\nDefect description: {defect_details['description']}\n\nDefect type: {defect_details['type']}\n\nEmail content:"
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    email_content = response.choices[0].text
    
    return email_content

def smart_assistance(defect_details, trigger_email):
    # Logic to email the ACT product owner when a defect is marked as a requirement gap using OpenAI-generated email content
    
    if trigger_email and defect_details['type'] == 'requirement_gap':
        act_product_owner_email = 'act_product_owner@example.com'
        subject = f"Defect Marked as Requirement Gap - Defect ID: {defect_details['id']}"
        email_content = generate_email_content(defect_details)
        send_email(act_product_owner_email, subject, email_content)

# Example usage
defect_details = {
    'id': 1234,
    'description': 'Some description of the defect',
    'type': 'requirement_gap'
}
trigger_email = True

smart_assistance(defect_details, trigger_email)
