
# PEFT

## LORA

![](attachments/Pasted%20image%2020250131085440.png)

![](attachments/Pasted%20image%2020250131095705.png)

![](attachments/Pasted%20image%2020250131095717.png)

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

## RLHF: Reinforcement Learning from Human Feedback

![](attachments/Pasted%20image%2020250131092813.png)

![](attachments/Pasted%20image%2020250131092822.png)

![](attachments/Pasted%20image%2020250131093144.png)


## DPO: Direct preference optimization

![](attachments/Pasted%20image%2020250131094907.png)

![](attachments/Pasted%20image%2020250131094918.png)

![](attachments/Pasted%20image%2020250131094934.png)

## ORPO: Odds Ratio Preference Optimization

![](attachments/Pasted%20image%2020250204203001.png)


![](attachments/Pasted%20image%2020250205092824.png)

![](attachments/Pasted%20image%2020250205092846.png)

![](attachments/Pasted%20image%2020250205092907.png)

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


![](attachments/Pasted%20image%2020250205120542.png)



















# end



















































