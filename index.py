import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config, OpenAIGPTLMHeadModel, OpenAIGPTTokenizer
from transformers import pipeline

# Load pre-trained GPT-2 model and tokenizer
gpt_model = GPT2LMHeadModel.from_pretrained("gpt2")
gpt_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Create a sentiment analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis')

def chatbot_response(prompt):
    # Tokenize the input prompt
    input_ids = gpt_tokenizer.encode(prompt, return_tensors="pt")

    # Generate a response from the GPT-2 model
    output = gpt_model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    # Decode the generated response
    response = gpt_tokenizer.decode(output[0], skip_special_tokens=True)

    # Analyze sentiment of the response
    sentiment_result = sentiment_analyzer(response)
    sentiment_label = sentiment_result[0]['label']
    sentiment_score = sentiment_result[0]['score']

    return response, sentiment_label, sentiment_score

# Simple loop to get user input and generate responses
while True:
    user_input = input("You: ")

    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        break

    # Get the chatbot's response and sentiment analysis
    response, sentiment_label, sentiment_score = chatbot_response(user_input)

    print(f"ChatBot: {response}")
    print(f"Sentiment: Label - {sentiment_label}, Score - {sentiment_score}")
