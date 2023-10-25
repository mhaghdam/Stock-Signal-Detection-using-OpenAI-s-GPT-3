import openai
import pandas as pd

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"


def get_chat_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"]


# Load data from CSV files
mes_data = pd.read_csv('Message_Data.csv', encoding='utf_8')
messages = list(mes_data.Message)

few_shot_data = pd.read_csv('Few_Shot_Data.csv', encoding='utf_8')
few_shots_messages = list(few_shot_data.message)
few_shots_responses = list(few_shot_data.signal)

responses = []
few_shots_content = ''

# Prepare content for few_shots
for i in range(len(few_shots_messages)):
    few_shots_content += f"""
    Message: {few_shots_messages[i]}
    response: {few_shots_responses[i]}

    """

# Iterate through messages
for i in range(len(messages)):
    prompt = f'''
    Your task is to determine whether the message implies a buying or selling signal in the Iranian stock market.
    Please respond with one of the following options:
    - "Buy Signal"
    - "Sell Signal"
    - "No Signal"

    Only print the last respond.
    """{few_shots_content}

    Message: {messages[i]}
    """
    '''

    reply = get_chat_completion(prompt)
    print(reply)
    responses.append(reply)

# Create a DataFrame to store messages and signal labels
df = pd.DataFrame({
    'Messages': messages,
    'Signal_Labels': responses
})

# Save the DataFrame to a CSV file
df.to_csv(f"Messages_Signals.csv", index=False)
