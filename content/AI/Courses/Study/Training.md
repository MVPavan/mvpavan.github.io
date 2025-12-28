
# PEFT

## LORA

![[Pasted-image-20250131085440.png]]

![[Pasted-image-20250131095705.png]]

![[Pasted-image-20250131095717.png]]

## DORA

![[Pasted-image-20250131085638.png]]



# Continual Pre-Train

1. Simple rewarming and re-decaying lr
2. Adding a small portion (e.g., 5%) of the original pretraining data (D1) to the new dataset (D2) to prevent catastrophic forgetting. Note that smaller fractions like 0.5% and 1% were also effective.


# SFT/Instruction Tuning:

1. Obtain a pretrained base model:
  Base models are trained for next word prediction, though they are good at natural language understanding, output need not be in the format we prefer it. It would be just predicting next tokens with out any structure to follow.
2. Supervised/Instruction Finetuning:
  Using a specific structured chat template (conversation/instructions/QA) text dataset, model is supervised finetuned to align to answer in that structure. Data can be domain specific.

# Preference Alignment:

## RLHF: Reinforcement Learning from Human Feedback

![[Pasted-image-20250131092813.png]]

![[Pasted-image-20250131092822.png]]

![[Pasted-image-20250131093144.png]]


## DPO: Direct preference optimization

![[Pasted-image-20250131094907.png]]

![[Pasted-image-20250131094918.png]]

![[Pasted-image-20250131094934.png]]

## ORPO: Odds Ratio Preference Optimization

![[Pasted-image-20250204203001.png]]


![[Pasted-image-20250205092824.png]]

![[Pasted-image-20250205092846.png]]

![[Pasted-image-20250205092907.png]]

odds(p) = p/(1-p) -> prob of event happening / prob of not happening
OR(a,b) = odds(a)/odds(b)
yw -> desired response
yl -> undesired response
Aim OR(yw,yl) to be high

Lor -> is low if OR(yw,yl) is high and vice versa

Delta(Lor) = delta(d).h(d)
Aim to decrease Delta(Lor) as yw increases, yl decreases and vice versa
delta(d) -> odds(yl)/(odds(yw)+odds(yl)) --> decreases as yl decreases and yw increases
h(d) -> increase as yw increases and decreases as yw decreases
h(d) -> decreases (negative) as yl increases and increases as yl decreases

so gradient boosts yw increase and yl increase
Implementation in HF library, probabilities we get are logsoftmax so applying exp will give actual probs. 


![[Pasted-image-20250205120542.png]]



















# end



















































