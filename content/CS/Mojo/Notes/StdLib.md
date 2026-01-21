
## Algorithm

- functional
- memory
- reduction

### Functional

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
  var shape = Index(10, 10)  # 2D: 10x10
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
> [!note] `func` has to be compile time parameter.


#### `map`

- **Purpose**: Simple index-based iteration with functional interface
- **Signature**: `map[func: fn(Int) capturing [origins] -> None](size: Int)`
- **Use Case**: Cleaner than raw `for` loops when capturing context
- **Example**:
```mojo
var data = alloc[Int](10)

@parameter
fn worker(idx: Int):
	data[idx] += 1
	
map[worker](10)
```
