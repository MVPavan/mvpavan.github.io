
###### Resources:
	- https://hanlab.mit.edu/courses/2023-fall-65940 lectures 17,18.
	- https://huggingface.co/docs/transformers/v4.20.1/en/perf_train_gpu_many

Types of distributed training:
- Data Parallel: Replicate model across gpu and distribute data across each gpu.
	- DP
	- DDP
	- Deepspeed:
		- Zero - 1, 2, 3(=FSDP in pytorch)
- Pipeline Parallel:
- Tensor Parallel:


## Data Parallel:

| Feature                  | DataParallel (DP)                           | DistributedDataParallel (DDP)                                                          |
| ------------------------ | ------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Process Model**        | Single process, multiple threads            | Multiple processes, each handling one or more GPUs                                     |
| **Model Replication**    | Replicated on each GPU at each forward pass | Replicated once per process                                                            |
| **Input Data Handling**  | Splits input data across GPUs               | Splits input data across processes                                                     |
| **Gradient Aggregation** | Gradients averaged on the CPU/Single GPU    | Gradients synchronized across processes using NCCL                                     |
| **Performance**          | Better for smaller models.                  | More efficient, better scaling across multiple GPUs and nodes.                         |
| **Scalability**          | Best for single-node, multi-GPU setups      | Scales well across multiple nodes and GPUs                                             |
| **Synchronization**      | Implicit, handled by the framework          | Explicit, requires setting up distributed process groups                               |
| **Code Example**         | `model = nn.DataParallel(model).cuda()`     | `dist.init_process_group(backend='nccl'); model = DDP(model, device_ids=[local_rank])` |

![[Pasted image 20240703173906.png]]

![[Pasted image 20240703171020.png]]

![[Pasted image 20240703174204.png]]

Conclusion:
- The only communication DDP performs per batch is sending gradients, whereas DP does 5 different data exchanges per batch.
- Under DP gpu 0 performs a lot more work than the rest of the gpus, thus resulting in under-utilization of gpus.
- By default pytorch recommends DDP over DP, even for single node, multi gpu setup due to python GIL restrictions over multi threading.

![[Pasted image 20240703171554.png]]