
### SIMD
- Single Instruction multiple data, stores.
- SIMD allows a single instruction to be executed across the multiple data elements of the vector.
- `SIMD[dtype, size]`
- `dtype = Dtype.int/ Dtype.float64 ....`
- size = The size of the SIMD vector to be positive and a power of 2.

### Types

[Types | Modular Docs](https://docs.modular.com/mojo/manual/types)

Basic numerical types defined in Mojo are actually SMID's of size 1.
`Int8 = Scalar[DType.int8]`
`Float64 = SMID[DType.float64, 1]` 
`Scalar = SIMD[size=1]`



### Variables
[Variables | Modular Docs](https://docs.modular.com/mojo/manual/variables)
- declared -` var k = 3`
- undeclared - `k = 3`
- declared follow lexical scoping - with in a function declared variable in inner scope is not accessible outside of inner scope.
- undeclared follow python function scope.
- all varaiables are strongly typed, so no different datatype assignment.

### Value ownership
[Ownership | Modular Docs](https://docs.modular.com/mojo/manual/values/ownership)
- owned - has unique mutable access to this variable.
	- Technically, the `owned` keyword does not guarantee that the received value is _the original value_—it guarantees only that the function gets unique ownership of a value (enforcing [value semantics](https://docs.modular.com/mojo/manual/values/value-semantics)). This happens in one of three ways:
	- The caller passes the argument with the `^` transfer operator, which ends the lifetime of that variable (the variable becomes uninitialized) and ownership is transferred into the function without making a copy of any heap-allocated data.
	- The caller **does not** use the `^` transfer operator, in which case, the value is copied into the function argument and the original variable remains valid. (If the original value is not used again, the compiler may optimize away the copy and transfer the value).
	- The caller passes in a newly-created "owned" value, such as a value returned from a function. In this case, no variable owns the value and it can be transferred directly to the callee.
- inout - shared ownership, modifications reflect across scope.
	- no default values for inout
	- in subsequent fn no inout on borrowed variables
- borrowed - no modifications allowed
	- Small values like `Int`, `Float`, and `SIMD` are passed directly in machine registers instead of through an extra indirection.


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
- default ownership - borrowed, read-only
- default only supports declared variables.
- inputs and outputs are also strongly typed


#### def
```
def function_name():
	
```
- default ownership - borrowed, but if the function mutates the argument, it makes a mutable copy
- default supports declared and undeclared variables.


### Memory

### Arc
Reference-counted smart pointers
#### Reference
Defines a non-nullable safe reference
`Reference[type:AnyType, is_mutable:bool, lifetime: usually varibale lifetime, AddressSpace: generic = 0]`
- Use subscript syntax `ref[]` to access the element.


### Loops

### for
- iterating through for loop creates var variable and assigns reference to object, use `[]` to access value.

