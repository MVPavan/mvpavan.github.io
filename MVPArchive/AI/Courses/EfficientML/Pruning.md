Terminology:
- Pruning - Making weight/activations to zero such that specific hardware can make use of it.
- Pruning ratio - Percentage of weights/neurons to be pruned. 60% pruning implies 60% of total neurons are pruned.

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




