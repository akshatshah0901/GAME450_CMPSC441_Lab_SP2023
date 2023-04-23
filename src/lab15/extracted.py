import torch
from sentence_transformers import SentenceTransformer, util

question = "What is the capital of France?"
response = "The capital of France is Paris."

model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
question_embedding = model.encode(question, convert_to_tensor=True)
response_embedding = model.encode(response, convert_to_tensor=True)

cosine_score = util.pytorch_cos_sim(question_embedding, response_embedding)
print(cosine_score)
