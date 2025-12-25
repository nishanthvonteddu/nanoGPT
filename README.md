---
title: nanoGPT From Scratch
emoji: 🧠
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: "4.44.0"
app_file: app.py
pinned: false
---

# nanoGPT From Scratch (Practice Project)

This Space runs **inference only** for a GPT-2–style language model
implemented and trained **from scratch** using PyTorch.

⚠️ This model was trained on a **small custom dataset** for learning purposes.
It is **not** a production-grade language model.

## How to use
- Enter a short prompt
- Adjust generation parameters
- Click **Generate**
- Wait a few seconds (CPU inference)

## Notes
- Training was done locally / on Colab
- This Space only loads `best_model.pt` and runs inference
- Model weights are stored using **Git LFS**