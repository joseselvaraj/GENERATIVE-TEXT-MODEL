from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

prompt = "The importance of education in modern society"

result = generator(prompt, max_length=100, num_return_sequences=1)

print("Generated Text:\n")
print(result[0]['generated_text'])
