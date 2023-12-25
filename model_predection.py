import torch
from transformers import PegasusTokenizer, PegasusForConditionalGeneration
import os

model_path= "model"
model = PegasusForConditionalGeneration.from_pretrained(model_path)
tokenizer = PegasusTokenizer.from_pretrained(model_path)

def predict(text:str,length:int=100):
    test_summaries = []
    single_input_encoding = tokenizer(text, return_tensors='pt', max_length=1000, truncation=True, padding=True)
    with torch.no_grad():
        generated_ids_single = model.generate(single_input_encoding['input_ids'], max_length=length, num_beams=4, length_penalty=2.0, early_stopping=True)
        generated_summary_single = tokenizer.decode(generated_ids_single[0], skip_special_tokens=True)
    return generated_summary_single