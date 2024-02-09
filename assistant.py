import openai

# Set up the OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def generate_developer_info(defect_details):
    # Use OpenAI to generate developer information based on the defect details
    
    prompt = f"Defect ID: {defect_details['id']}\n\nDefect description: {defect_details['description']}\n\nDefect resolution steps: {defect_details['resolution_steps']}\n\nDeveloper assigned:"
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=20,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    developer_info = response.choices[0].text
    
    return developer_info

# Example usage
defect_details = {
    'id': 1234,
    'description': 'Some description of the defect',
    'resolution_steps': 'Step 1: Do something\nStep 2: Do something else\nStep 3: Finalize'
}

developer_info = generate_developer_info(defect_details)
print(f"Developer assigned: {developer_info}")
