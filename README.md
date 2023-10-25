# LLM
# OpenAI Stock Signal Detection

This repository contains a Python script for detecting signals in messages related to the Iranian stock market using OpenAI's GPT-3 model.

## Prerequisites

Before running the script, you need to set up your OpenAI API key. You can obtain an API key from [OpenAI](https://beta.openai.com/).

```python
# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

Installation
1- Clone this repository to your local machine:
git clone https://github.com/YOUR_USERNAME/MyOpenAIProject.git
cd MyOpenAIProject

1- Install the required Python packages. You can use pip to install them:
pip install openai pandas

Usage
1- Prepare your message data in a CSV file named Message_Data.csv. This file should contain a column named "Message" with the messages you want to analyze.

2- Prepare your few-shot data in a CSV file named Few_Shot_Data.csv. This file should contain columns named "message" and "signal" with the message content and corresponding signals.

3- Run the Python script to analyze the messages and generate signal labels:
python stock_signal_detection.py

