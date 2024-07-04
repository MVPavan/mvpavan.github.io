Terminology:
- Pruning - Making weight/activations to zero such that specific hardware can make use of it.
- Pruning ratio - Percentage of weights/neurons to be pruned. 60% pruning implies 60% of total neurons are pruned.
- N:M Sparsity - In each contiguous M elements, N of them are pruned.

![](attachments/Pasted%20image%2020240704110201.png)

Two types of pruning:
1. Synapses pruning
2. Neuron pruning

![](attachments/Pasted%20image%2020240704105958.png)


![](attachments/Pasted%20image%2020240704110036.png)
Iterative pruning:
- Prune pre trained model.
- finetune pruned model for 1-5 epochs.
- Iterate pruning and finetuning as requirement.

![](attachments/Pasted%20image%2020240704110219.png)

Fine grained Pruning:
- Flexible pruning indices
- Usually results in larger pruning ratios.
- Needs custom hardware.

Pattern-based pruning:
- N:M Sparsity, 2:4 sparsity (50% sparsity)
- supported from Ampere GPU architecture
- Maintains accuracy
![](attachments/Pasted%20image%2020240704125201.png)
![](attachments/Pasted%20image%2020240704125326.png)

Channel Pruning:
- Smaller compression ratio
- Direct speed up due to reduced channels in NN.

![](attachments/Pasted%20image%2020240704125646.png)
![](attachments/Pasted%20image%2020240704125721.png)

## Pruning Criteria:

#### Magnitude based:
- Element wise pruning using absolute magnitude threshold
- vector wise pruning using vector wise L1/L2/Lp norms

#### Scaling-based:
- Used for channel (filter) pruning
- Trainable scaling factor is multiplied to each output channel and channels with small scaling factor are pruned.
- Scaling factors can be reused from Batch norm layers.
![](attachments/Pasted%20image%2020240704130512.png)


## Automatic Pruning:

Layer wise pruning:
- Sensitivity analysis for per layer pruning ratio, by observing accuracy degrade with each pruning ratio.
![](attachments/Pasted%20image%2020240704151409.png)

AMC: Auto ML for model compression:
- Pruning 