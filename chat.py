
"""

DO NOT MODIFY 

This is the chat function I have provided for you.  You are welcome
to look at it but do all your work in main.py

"""
import sys, os

model_name = "Qwen/Qwen3-0.6B"
# load the tokenizer and the model
tokenizer = None
model = None

CALL_FROM_PYTEST = (
    any("pytest" in arg for arg in sys.argv)
    or "pytest" in sys.modules
)

def chat(prompt =  "Give me a short introduction to large language model.", temperature = 1.0):

    global model_name
    global tokenizer
    global model
    
    if CALL_FROM_PYTEST:
        return "Test Response"
    
    from transformers import AutoModelForCausalLM, AutoTokenizer

    if tokenizer == None:
        tokenizer = AutoTokenizer.from_pretrained(model_name)

    if model == None:
        model = AutoModelForCausalLM.from_pretrained(
            model_name
        )

    # prepare the model input    
    messages = [
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False # Switches between thinking and non-thinking modes. Default is True.
    )
    model_inputs = tokenizer([text], return_tensors="pt").to("cpu")

    # conduct text completion
    generated_ids = model.generate(
        **model_inputs,
        temperature=temperature,  # ← added parameter here
        do_sample=True,            # ← must be True for temperature to have an effect        
        max_new_tokens=128
    )
    output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

    # parsing thinking content
    try:
        # rindex finding 151668 (</think>)
        index = len(output_ids) - output_ids[::-1].index(151668)
    except ValueError:
        index = 0

    thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
    content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

    # print("thinking content:", thinking_content)
    # print("content:", content)
    return content
