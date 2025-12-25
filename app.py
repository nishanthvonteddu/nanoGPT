import torch
import gradio as gr
import tiktoken
from model import GPT, GPTConfig

device = "cpu"

# load checkpoint
checkpoint = torch.load(
    "best_model.pt",
    map_location=device,
    weights_only=False
)
config = checkpoint["config"]

model = GPT(config)
model.load_state_dict(checkpoint["model_state_dict"])
model.eval()

enc = tiktoken.get_encoding("gpt2")

@torch.no_grad()
def generate_text(prompt, max_tokens=100, temperature=1.0):
    tokens = enc.encode(prompt)
    x = torch.tensor(tokens, dtype=torch.long)[None, :]

    for _ in range(max_tokens):
        logits = model(x)
        logits = logits[:, -1, :] / temperature
        probs = torch.softmax(logits, dim=-1)
        next_token = torch.multinomial(probs, 1)
        x = torch.cat([x, next_token], dim=1)

    return enc.decode(x[0].tolist())


gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Slider(10, 200, value=100, label="Max tokens"),
        gr.Slider(0.5, 1.5, value=1.0, label="Temperature"),
    ],
    outputs="text",
    title="GPT From Scratch (Practice)",
    description="A GPT-2 style model trained from scratch on a small custom dataset."
).launch()