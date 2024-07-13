- [[#SIMD|SIMD]]
- [[#Types|Types]]
- [[#Variables|Variables]]
- [[#Value ownership|Value ownership]]
- [[#Alias|Alias]]
- [[#Struct|Struct]]
- [[#Functions|Functions]]
	- [[#Functions#fn|fn]]
	- [[#Functions#def|def]]
- [[#Memory|Memory]]
- [[#Arc|Arc]]
	- [[#Arc#Reference|Reference]]
- [[#Loops|Loops]]
- [[#for|for]]
- [[#Decorators|Decorators]]
	- [[#Decorators#@parameter|@parameter]]

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
- **`^` transfer operator**: to move the value, unless the value is a trivial type (like `Int`) or a newly-constructed, "owned" value.
- owned - has unique mutable access to this variable
	- Technically, the `owned` keyword does not guarantee that the received value is _the original value_—it guarantees only that the function gets unique ownership of a value (enforcing [value semantics](https://docs.modular.com/mojo/manual/values/value-semantics)). This happens in one of three ways:
	- The caller passes the argument with the **`^` transfer operator**, which ends the lifetime of that variable (the variable becomes uninitialized) and ownership is transferred into the function without making a copy of any heap-allocated data.
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
fn function_name[p:dtype #parameter](k:dtype #argument) -> dtype:
	
```
- default ownership - borrowed, read-only
- default only supports declared variables.
- inputs and outputs are also strongly typed
- parameter is compile time variable, and argument is runtime variable.
	- parameter should be available by compile time 


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



### Decorators

#### @parameter

- add the `@parameter` decorator on an `if` statement or on a nested function to run that code at compile time.


### Pointers

- Creates an indirect reference to a location in memory. 
- `UnsafePointer` can dynamically allocate and free memory, or to point to memory allocated by some other piece of code.
- User responsible for ensuring that memory gets allocated and freed correctly

> _pointee_ : value pointed to by a pointer.
> _dereference_ : retrieve or update pointee using `ptr[]`

#### Lifecycle
- Uninitialized: `var ptr: UnsafePointer[Int]`
- Null/invalid pointer -> address 0 : `var ptr: UnsafePointer[Int]()`
- alloc -> allocates n dtype blocks of memory: `var ptr = UnsafePointer[dtype].alloc(n)`
	- after allocation memory is still uninitialized, dereferencing causes undefined behavior
- Initialization:
	```
	initialize_pointee_copy(ptr, value)  -- copy
	or  
	initalize_pointee_move(ptr, value^)  -- move
	or  
	ptr = UnsafePointer[Int].address_of(value) -- assign
	```
	- once initialized we can dereference it
- Dangling pointer -> pointer after freeing the allocated memory `ptr.free()`
	- addr still points to previous location, but that memory is no longer allocated to this pointer.
	- dereferencing causes undefined behavior

![](attachments/Pasted%20image%2020240713130310.png)


