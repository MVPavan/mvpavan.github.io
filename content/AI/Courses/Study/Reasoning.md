
Usual Training process:

1. Pre Training
2. SFT
3. Preference Alignment

R1 Training process:

start from base model and follow below steps

![[Pasted-image-20250211101350.png]]

-  Long chains of reasoning SFT Data: 600,000

![[Pasted-image-20250211101501.png]]

- An interim high-quality reasoning LLM (but worse at non-reasoning tasks).
![[Pasted-image-20250211101649.png]]

- Creating reasoning models with large-scale reinforcement learning (RL)
	- Large-Scale Reasoning-Oriented Reinforcement Learning (R1-Zero)
	-  Creating SFT reasoning data with the interim reasoning model

![[Pasted-image-20250211101822.png]]

## Large-Scale Reasoning-Oriented Reinforcement Learning (R1-Zero)

![[Pasted-image-20250211102318.png]]
Although DeepSeek-R1-Zero exhibits strong reasoning capabilities and autonomously develops unexpected and powerful reasoning behaviors, it faces several issues. For instance, DeepSeek-R1-Zero struggles with challenges like poor readability, and language mixing.

It is used in two places:
1. creating an interim reasoning model to generate SFT data points
2. Training the R1 model to improve on reasoning and non-reasoning problems (using other types of verifiers)
3. General RL training phase


## Creating SFT reasoning data with the interim reasoning model

![[Pasted-image-20250211103014.png]]

To prevent unstable cold start phase of RL training, CoT data is collected for SFT phase
Cold Start CoT Data:
- few-shot prompting with a long CoT as an example
- directly prompting models to generate detailed answers with reflection and verification
- gathering DeepSeek-R1- Zero outputs in a readable format
-  refining the results through post-processing by human annotators


![[Pasted-image-20250211103112.png]]

## General RL training phase

![[Pasted-image-20250211103617.png]]

# DeepSeek R1 Architecture


![[Pasted-image-20250211103737.png]]
![[Pasted-image-20250211103744.png]]

