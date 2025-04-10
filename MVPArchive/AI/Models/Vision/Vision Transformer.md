
## VIT

![](attachments/Pasted%20image%2020250127162012.png)


## DETR

- Has fixed 100 object queries

![](attachments/Pasted%20image%2020250410090245.png)
![](attachments/Pasted%20image%2020250410090241.png)
## DINO

[Emerging Properties in Self-Supervised Vision Transformers (DINO) — Paper Summary | by Anuj Dutt | Medium](https://medium.com/@anuj.dutt9/emerging-properties-in-self-supervised-vision-transformers-dino-paper-summary-4c7a6ed68161)
##### Traditional Knowledge Distillation:
- Teacher Model: A pre-trained, larger model, usually frozen during training.
- Student Model: A smaller model, trained via back-propagation to mimic the teacher’s predictions.
- Objective: Transfer knowledge from the teacher’s weight distribution to the student.
- Model Diversity: Teacher and student can be different models, e.g., ResNet50 (Teacher) and SqueezeNet (Student).
- Loss Function: Typically uses KL Divergence loss on the output logits of both models.

##### SSL with DINO (DIstillation of NOisy labels)
DINO introduces a unique approach to knowledge distillation.

1. **Multi-crop Strategy:** DINO generates various distorted views (crops) from an image, including two global views and several lower-resolution local views, using different augmentations.
2. **Local-to-Global Learning:** All crops are passed through the student model, but only global views are processed by the teacher model. This teaches the student to relate local image patches with the global context from the teacher.
3. **Loss Minimization:** The goal is to minimize a loss function measuring the similarity of representations from the student and teacher for different views of the same image, without using labeled data.

![](attachments/Pasted%20image%2020250409150743.png)



## Deformable DETR

##### Deformable Convolution
![](attachments/Pasted%20image%2020250410090157.png)

![](attachments/Pasted%20image%2020250410091610.png)


![](attachments/Pasted%20image%2020250410102412.png)






