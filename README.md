---
## Not ideal for real world use as a CHAT
## It's a very small dataset and the model specifically trained for this particular dataset so this model is not ready to use as a chat. It repeatedly replies only the text that is mentioned in the dataset irrespective of the question.
## Stricly educational purpose.
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



## These are the results of the model when trained in GOOGLE COLLAB
## It's a very small dataset and the model specifically trained for this particular dataset so this model is not ready to use as a chat. 
## This is just for educational purpose.
- Using device: cuda
step 00000 | train loss 10.9998
step 00100 | train loss 6.2425
step 00200 | train loss 5.9770
step 00300 | train loss 5.4772
step 00400 | train loss 5.0113
step 00500 | train loss 4.9466
step 00500 | val loss 5.4523
✅ Saved new best model
step 00600 | train loss 5.2371
step 00700 | train loss 5.3555
step 00800 | train loss 5.3720
step 00900 | train loss 4.3135
step 01000 | train loss 4.9143
step 01000 | val loss 5.4920
step 01100 | train loss 4.7382
step 01200 | train loss 5.0108
step 01300 | train loss 4.7219
step 01400 | train loss 4.8574
step 01500 | train loss 5.2103
step 01500 | val loss 5.2553
✅ Saved new best model
step 01600 | train loss 4.5311
step 01700 | train loss 4.9025
step 01800 | train loss 4.4274
step 01900 | train loss 4.8862
step 02000 | train loss 4.7996
step 02000 | val loss 5.1715
✅ Saved new best model
step 02100 | train loss 3.7538
step 02200 | train loss 4.7738
step 02300 | train loss 4.4911
step 02400 | train loss 4.4504
step 02500 | train loss 3.9489
step 02500 | val loss 5.0384
✅ Saved new best model
step 02600 | train loss 3.9313
step 02700 | train loss 4.2135
step 02800 | train loss 4.4448
step 02900 | train loss 3.7965
step 03000 | train loss 3.9204
step 03000 | val loss 5.0902
step 03100 | train loss 4.0841
step 03200 | train loss 3.5700
step 03300 | train loss 4.7892
step 03400 | train loss 3.6491
step 03500 | train loss 3.7517
step 03500 | val loss 4.8143
✅ Saved new best model
step 03600 | train loss 3.5012
step 03700 | train loss 3.7224
step 03800 | train loss 3.2526
step 03900 | train loss 3.8506
step 04000 | train loss 3.9597
step 04000 | val loss 4.9158
step 04100 | train loss 3.6779
step 04200 | train loss 3.0521
step 04300 | train loss 2.8347
step 04400 | train loss 4.2322
step 04500 | train loss 3.7579
step 04500 | val loss 4.6200
✅ Saved new best model
step 04600 | train loss 3.2681
step 04700 | train loss 3.7513
step 04800 | train loss 3.0898
step 04900 | train loss 3.8898
step 05000 | train loss 3.2076
step 05000 | val loss 4.7030
step 05100 | train loss 3.6788
step 05200 | train loss 3.0504
step 05300 | train loss 2.5504
step 05400 | train loss 3.1733
step 05500 | train loss 2.5223
step 05500 | val loss 4.7991
step 05600 | train loss 2.2777
step 05700 | train loss 3.1686
step 05800 | train loss 3.9210
step 05900 | train loss 3.7123
step 06000 | train loss 3.6105
step 06000 | val loss 4.7789
step 06100 | train loss 3.0127
step 06200 | train loss 3.0640
step 06300 | train loss 3.2284
step 06400 | train loss 2.2974
step 06500 | train loss 1.4333
step 06500 | val loss 4.9356
step 06600 | train loss 1.3495
step 06700 | train loss 2.0811
step 06800 | train loss 1.3768
step 06900 | train loss 1.3543
step 07000 | train loss 1.5892
step 07000 | val loss 5.0306
step 07100 | train loss 2.6009
step 07200 | train loss 1.3325
step 07300 | train loss 1.5107
step 07400 | train loss 2.1724
step 07500 | train loss 1.3440
step 07500 | val loss 5.1939
step 07600 | train loss 1.7728
step 07700 | train loss 0.7337
step 07800 | train loss 3.4360
step 07900 | train loss 1.2504
step 08000 | train loss 3.2769
step 08000 | val loss 5.4910
step 08100 | train loss 0.3671
step 08200 | train loss 1.6622
step 08300 | train loss 1.9364
step 08400 | train loss 1.1947
step 08500 | train loss 1.1553
step 08500 | val loss 5.5756
step 08600 | train loss 1.1408
step 08700 | train loss 1.1578
step 08800 | train loss 0.3493
step 08900 | train loss 1.3790
step 09000 | train loss 0.6753
step 09000 | val loss 5.6647
step 09100 | train loss 0.9958
step 09200 | train loss 0.8662
step 09300 | train loss 0.8241
step 09400 | train loss 0.4953
step 09500 | train loss 0.6441
step 09500 | val loss 5.9287
step 09600 | train loss 0.9745
step 09700 | train loss 0.6978
step 09800 | train loss 1.6112
step 09900 | train loss 0.6578
Training complete.