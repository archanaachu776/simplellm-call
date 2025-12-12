from transformers import pipeline

generator = pipeline("text-generation",model ="distilgpt2")

result=  generator(
    "AI is the future because",
    max_length = 50,
    num_return_reference = 1
)

print(result)
