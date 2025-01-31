
# PEFT

## LORA

![](attachments/Pasted%20image%2020250131085440.png)

## DORA

![](attachments/Pasted%20image%2020250131085638.png)



# Continual Pre-Train

1. Simple rewarming and re-decaying lr
2. Adding a small portion (e.g., 5%) of the original pretraining data (D1) to the new dataset (D2) to prevent catastrophic forgetting. Note that smaller fractions like 0.5% and 1% were also effective.


# SFT/Instruction Tuning:

1. Obtain a pretrained base model:
	Base models are trained for next word prediction, though they are good at natural language understanding, output need not be in the format we prefer it. It would be just predicting next tokens with out any structure to follow.
2. Supervised/Instruction Finetuning:
	Using a specific structured chat template (conversation/instructions/QA) text dataset, model is supervised finetuned to align to answer in that structure. Data can be domain specific.

# Preference Alignment:
## DPO: Direct preference optimization

## RLHF: Reinforcement Learning from Human Feedback











# end



















































