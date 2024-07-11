
### SIMD
- Single Instruction multiple data, stores.
- SIMD allows a single instruction to be executed across the multiple data elements of the vector.
```
	SIMD[dtype, size]
```
- dtype = Dtype.int/ Dtype.float64 ....
- size = The size of the SIMD vector to be positive and a power of 2.

### Types

[Types | Modular Docs](https://docs.modular.com/mojo/manual/types)

Basic numerical types defined in Mojo are actually SMID's of size 1.

```
Float64 = SMID[DType.float64, 1]
``` 


### Variables
[Variables | Modular Docs](https://docs.modular.com/mojo/manual/variables)
- declared - var k = 3
- undeclared - k = 3
- declared follow lexical scoping - with in a function declared variable in inner scope is not accessible outside of inner scope.
- undeclared follow python function scope.
- all varaiables are strongly typed, so no different datatype assignment.

### Value ownership
- owned - has exclusive ownership, no other scope of mojo has access to this variable.
- inout - shared ownership, modifications reflect across scope.
- borrowed - no modifications allowed


### Alias
compile time temporary value that cant change at runtime

### Struct
- @value will synthesize the essential lifecycle methods so your object provides full value semantics. Specifically, it generates the `__init__()`, `__copyinit__()`, and `__moveinit__()`
- immediately it will be compatible with List etc.
- methods inside structs are fn.

### Functions

#### fn
```
fn function_name(k:dtype) -> dtype:
	
```
- default ownership - owned
- default only supports declared variables.
- inputs and outputs are also strongly typed


#### def
```
def function_name():
	
```
- default ownership - borrowed
- default only supports declared variables.

