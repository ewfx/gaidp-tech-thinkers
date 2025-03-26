import openai
import os

def generate_report(data_summary, model_accuracy, od_flag_details):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    
    openai.api_key = openai_api_key

    report_content = f"Data Summary:\n{data_summary}\n\nModel Accuracy: {model_accuracy}\n\nOD Flag Details:\n{od_flag_details}\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": report_content}
        ],
        max_tokens=150
    )

    generated_report = response.choices[0].message['content'].strip()
    return generated_report

def save_report(report_text, filename="report.txt"):
    with open(filename, "w") as f:
        f.write(report_text)