
## CPU

- Physical cores: 20
- Physical + Logical cores: 40
```
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   46 bits physical, 48 bits virtual
CPU(s):                          40
On-line CPU(s) list:             0-39
Thread(s) per core:              2
Core(s) per socket:              10
Socket(s):                       2
NUMA node(s):                    2
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           85
Model name:                      Intel(R) Xeon(R) Silver 4210R CPU @ 2.40GHz
Stepping:                        7
CPU MHz:                         2400.000
CPU max MHz:                     3200.0000
CPU min MHz:                     1000.0000
```

> Mojo is using only physical cores where as numpy utilizing all 40 cores
## Python (Using Lists) 😀
- `512x256 @ 256x512`
```
Matmul : 512x256 @ 256x512
Iterations :  2
Total GFLOPS :  0.134217728
Total time in sec :  77.04722635447979
GFLOP/sec :  0.001742018945399663
```

- `2048x1024 @ 1024x2048` - My system got tired!

> All the operations from here are in FP32
## Numpy

- `512x256 @ 256x512`
```
Matmul : 512x256 @ 256x512
Iterations : 10000
Total GFLOPS :  0.134217728
Total time in sec :  0.0010287985601928084
GFLOP/sec :  130.46064914286632
speedup over python: 74890
```

- `2048x1024 @ 1024x2048`
```
Matmul : 2048x1024 @ 1024x2048
Iterations : 10000
Total GFLOPS :  8.589934592
Total time in sec :  0.019497849141806363
GFLOP/sec :  440.55805999554434

Matmul : 2048x1024 @ 1024x2048
Iterations :  200
Total GFLOPS :  8.589934592
Total time in sec :  0.018091672335285695
GFLOP/sec :  474.80047354419173
```


## Mojo

