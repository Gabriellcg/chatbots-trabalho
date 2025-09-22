import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# --- 1. SETUP DO MODELO E TOKENIZADOR ---
model_name = "pierreguillou/gpt2-small-portuguese"
print(f"Carregando o modelo '{model_name}'. Aguarde...")
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
except Exception as e:
    exit()

def gerar_resposta(prompt, params):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    with torch.no_grad():
        output_sequences = model.generate(
            input_ids=input_ids,
            pad_token_id=tokenizer.eos_token_id,
            **params
        )
    
    generated_text = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
    return generated_text

meu_prompt = "A inteligência artificial está transformando o mundo porque"

print("-" * 50)
print(f"PROMPT: '{meu_prompt}'")
print("-" * 50)

params_criativo = {
    "max_new_tokens": 80,
    "do_sample": True,     
    "temperature": 0.9,
    "top_p": 0.95,
}

print("\n[VERSÃO CRIATIVA]")
print(f"Parâmetros: {params_criativo}")
resposta = gerar_resposta(meu_prompt, params_criativo)
print(f"\nRESPOSTA:\n{resposta}\n")