```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

## Introduction

- INT8 (1S-7B) = 1 bytes (for INT there is not exponent and mantissa only bits)
- FP32 (1 sign, 8 exponent, 23 mantissa - 1S-8E-23M) - requires 32 bits to store = 4x8 bits = 4 bytes
- FP16 (1S-5E-10M) = 2 bytes
- BF16 (1S-8E-7M) = 2 bytes
- Subnormal values -  E = 0
- Normal Values - E != 0

> If any kernels are not implemented in fp16 try in bf16 as it is compatible with fp32 for same E
 
| Data Type    | Size (bits) | Sign Bits | Exponent | Mantissa | Precision | Range  |
| ------------ | ----------- | --------- | -------- | -------- | --------- | ------ |
| **Float32**  | 32          | 1         | 8        | 23       | Best      | ~10^38 |
| **Float16**  | 16          | 1         | 5        | 10       | Better    | ~10^4  |
| **BFloat16** | 16          | 1         | 8        | 7        | Good      | ~10^38 |
| **Int8**     | 8           | 1         | N/A      | N/A      | Avg       | ~2^7   |

## Types of Quantization:

Quantization can happen in two ways:
- Activation Quantization (Calibration)
	- Range of activations varies with input
	- Use sample input, infer and calculate range of activations for linear quantization. 

- Weight Quantization
	1. K-Means-based Weight Quantization
	2. Linear Quantization
		1. AWQ: Activation aware weight quantization
		2. GPTQ: GPT Quantized
		3. BNB: Bits and Bytes Quantized

### K-Means-based Weight Quantization

![](attachments/Pasted%20image%2020240704184537.png)
- cluster weights

### Linear Quantization
- Symmetric 
- Asymmetric

An affine mapping of integers to real numbers ==r = S(q-Z)

![](attachments/Pasted%20image%2020240704184804.png)

Full Connected Layer and Conv Layer:
![](attachments/Pasted%20image%2020240704185026.png)

Symmetric vs Asymmetric:
![](attachments/Pasted%20image%2020240704185237.png)![](attachments/Pasted%20image%2020240704185253.png)


## Quantization in Training:
- Post Training Quantization (PTQ) - All methods above
- Quantization aware Training (QAT)

### Quantization aware Training (QAT):
- Quantize:
	- Quantize weight and hold both quantized (BF16) and unquantized (FP32) weights. 
- Forward Pass:
	- Use Quantized version of model for inference (BF16)
- Back Prop:
	- Use original unquantized version of model weights (FP32)


One of the famous QAT method is QLoRA:
- Pretrained weights in 4-bit precision.
- LoRA in full precision

  

