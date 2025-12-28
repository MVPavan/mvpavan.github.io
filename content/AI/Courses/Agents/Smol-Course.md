https://github.com/huggingface/smol-course


## SFT/Instruction Tuning:

1. Obtain a pretrained base model:
  Base models are trained for next word prediction, though they are good at natural language understanding, output need not be in the format we prefer it. It would be just predicting next tokens with out any structure to follow.
2. Supervised/Instruction Finetuning:
  Using a specific structured chat template (conversation/instructions/QA) text dataset, model is supervised finetuned to align to answer in that structure. Data can be domain specific.

## Preference Alignment:
#### DPO: Direct preference optimization

#### RLHF: Reinforcement Learning from Human Feedback
