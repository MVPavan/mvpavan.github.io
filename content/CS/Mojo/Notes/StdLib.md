
## Algorithm

- functional
- memory
- reduction

### Functional

> [!note] Most APIs in `fucntional` take `func` as a compile time parameter.

#### `elementwise` 

- **Purpose**: N-dimensional iteration with automatic SIMD vectorization
- **Key Features**:
  - Abstracts loop nesting and vectorization
  - Supports CPU and GPU targets
  - Handles boundary conditions automatically
  - Chunks inner dimension by SIMD width
- **Signature**: `elementwise[func, simd_width](shape: IndexList[rank])`
- **Example**:
  ```mojo
  var shape = Index(10, 10)  # 2D: 10x10
  alias simd_width = 4
  @parameter
  fn worker[width: Int, rank: Int, alignment: Int](idx: IndexList[rank]):
      # idx: starting coordinates [row, col]
      # width: elements to process in inner dimension
      pass
  elementwise[worker, simd_width](shape)
  ```
- **Chunking Behavior**: For a 10-element dimension with SIMD width 4:
  - Processes: 4 + 4 + 1 + 1 (vectorized + cleanup) per row

#### `map`

- **Purpose**: Simple index-based iteration with functional interface
- **Signature**: `map[func: fn(Int) capturing [origins] -> None](size: Int)`
- **Use Case**: Cleaner than raw `for` loops when capturing context
- **Example**:
```mojo
var data = alloc[Int](10)

@parameter
fn worker(idx: Int):
  data[idx] += 1
  
map[worker](10)
```

#### `parallelize`  

- **Purpose**: Multi-threaded work distribution for CPU-intensive tasks
- **Signature**: `parallelize[func: fn(Int) capturing [origins] -> None](num_work_items: Int)`
- **Use Case**: Heavy independent computations (e.g., image processing, scientific calc)
- **Example**:
```mojo
var results = List[Int](capacity=1000)
# ... (fill list) ...
@parameter
fn process(idx: Int):
  # Heavy computation on independent index
  results[idx] = expensive_calc(results[idx])
parallelize[process](1000)
```   
- **Variants**: `parallelize` (async), `sync_parallelize` (blocking)


#### `tile`

- **Purpose**: Loop tiling (blocking) for cache locality
- **Signature**: `tile[func, tile_size_list](offset, limit)`
- **Key Note**: Static tiling requires explicit cleanup tile (e.g., `VariadicList(4, 1)`)
- **Example**:
```mojo
@parameter
fn worker[width: Int](off: Int): ...

# Tile with 4, fallback to 1 for remainder
tile[worker, VariadicList(4, 1)](0, 10)
```

##### `unswitch`
- **Purpose**: Hoists boolean checks out of functions ("compile-time if" at runtime)
- **Signature**: `unswitch[func](dynamic_bool)`
- **Use Case**: Selecting optimized/safe paths without branching inside the loop
- **Example**:
```mojo
unswitch[worker](is_fast_mode) # Compiles 2 versions, picks 1
```

##### `tile_and_unswitch`
- **Purpose**: Fused optimization (Fast path for main tiles, Safe path for cleanup)
- **Use Case**: Aligned SIMD for main loop, unaligned/masked for cleanup
- **Example**:
```mojo
# 0..8 runs with True (Fast), 8..10 runs with False (Safe)
tile_and_unswitch[worker, 4](0, 10)
```

##### `tile_middle_unswitch_boundaries`
- **Purpose**: Specialized 3-part tiling for convolutions (Left, Middle, Right)
- **Signature**: `tile_middle_unswitch_boundaries[func, tile_size, size]()`
- **Use Case**: Avoiding padding checks in the center of an image/tensor
- **Behavior**:
  - **Left**: `func[..., True, False]` (Left Edge Check)
  - **Middle**: `func[..., False, False]` (No Edge Checks - FAST)
  - **Right**: `func[..., False, True]` (Right Edge Check)

