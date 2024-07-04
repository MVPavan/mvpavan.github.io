Contents:
- [Introduction](#Introduction)

# Introduction

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


# Types of Quantization:

1. K-Means-based Weight Quantization
2. Linear Quantization

### K-Means-based Weight Quantization

![](attachments/Pasted%20image%2020240704184537.png)
- cluster weights 
