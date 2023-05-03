import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
#from torchvision.models import BigGAN
#from torchvision.utils import save_image

#import torchvision.models as models

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#biggan_model = models.BigGAN.from_pretrained('biggan-deep-256').to(device)

def generate_journal_entry(city_name):
    prompt = f"I arrived in {city_name} today. "
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
    output = model.generate(input_ids=input_ids, max_length=200, do_sample=True)
    journal_entry = tokenizer.decode(output[0], skip_special_tokens=True)
    return journal_entry


#def generate_image():
    #noise = torch.randn(1, 128).to(device)
    #class_vector = torch.randint(0, 1000, (1,), dtype=torch.long).to(device)
    #with torch.no_grad():
        #output = biggan_model(noise, class_vector, truncation=0.4)
    #save_image(output[0], 'generated_image.png')

#city_name = "Paris"
#journal_entry = generate_journal_entry(city_name)
#generate_image()


