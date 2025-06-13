# GENERATIVE-TEXT-MODEL

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : JOSIAH SELVARAJ D

*INTERN ID* : CT04DG1099

*DOMAIN* : ARTIFICIAL INTELLIGENCE

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTHOSH


# Task Title: Generative Text Model

Task Overview:

Goal: Create a text generation model using GPT or LSTM to generate coherent paragraphs based on user prompts.

Deliverable: A notebook that shows how the model generates paragraphs from user-given topics.

Why GPT-2?

Easy to use (no training required)

Generates high-quality human-like text

Suitable for real-world applications

Tools & Libraries Used:

Python 3.13

transformers library (by Hugging Face)

Google Colab / Jupyter Notebook

How It Works?

1.Install transformers (only once):

!pip install transformers

2.Import and initialize GPT-2 model:

from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')

set_seed(42)

3.Give it a topic (prompt) and generate text:

prompt = "The future of artificial intelligence"

result = generator(prompt, max_length=100, num_return_sequences=1)

print(result[0]['generated_text'])

Sample Results

Prompt 1: The importance of education

Generated Text:

The importance of education cannot be overstated. It plays a crucial role in shaping individuals, building knowledge, and developing societies. Through education, people gain the skills necessary to achieve success and contribute meaningfully to their communities...

Prompt 2: Climate change and its impact

Generated Text:

Climate change is one of the most pressing issues facing the world today. Its effects are already visible — rising sea levels, increasing temperatures, and extreme weather patterns. If action is not taken soon, the consequences could be irreversible...

Prompt 3: Technology in modern life

Generated Text:

Technology has transformed modern life in countless ways. From smartphones to artificial intelligence, it has made communication faster, information more accessible, and work more efficient. However, it also brings challenges like privacy concerns and screen addiction...

Conclusion:

GPT-2 can effectively generate human-like paragraphs based on simple prompts.

The model doesn't need training and can be used instantly.

This makes it ideal for writing assistants, chatbots, content creation, and more.

# PROGRAM

![Image](https://github.com/user-attachments/assets/f535296c-ac5b-4387-8d15-2bb45b335d81)


# OUTPUT

![Image](https://github.com/user-attachments/assets/c37598d5-9d96-4bf4-b07a-9c157e88a417)

![Image](https://github.com/user-attachments/assets/5c70d2a0-eb54-46a5-b83e-7569afa78952)
