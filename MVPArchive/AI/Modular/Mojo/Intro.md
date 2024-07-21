[Mojo By Example: A Comprehensive Introduction to the Mojo Programming Language (ruhati.net)](https://ruhati.net/mojo/)
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

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

### Loops

#### for
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
- alloc -> allocates n dtype contiguous blocks of memory: `var ptr = UnsafePointer[dtype].alloc(n)`
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

#### Methods
- [​`destroy_pointee`](https://docs.modular.com/mojo/stdlib/memory/unsafe_pointer/destroy_pointee): Destroy the pointed-to value.
- [​`move_from_pointee`](https://docs.modular.com/mojo/stdlib/memory/unsafe_pointer/move_from_pointee): Move the value at the pointer out.
- [​`initialize_pointee_move`](https://docs.modular.com/mojo/stdlib/memory/unsafe_pointer/initialize_pointee_move): Emplace a new value into the pointer location, moving from `value`.
- [​`initialize_pointee_copy`](https://docs.modular.com/mojo/stdlib/memory/unsafe_pointer/initialize_pointee_copy): Emplace a copy of `value` into the pointer location.
- [​`move_pointee`](https://docs.modular.com/mojo/stdlib/memory/unsafe_pointer/move_pointee): Moves the value `src` points to into the memory location pointed to by `dest`
- [free](https://docs.modular.com/mojo/stdlib/memory/unsafe_pointer/UnsafePointer#free ) : frees memory allocated by the pointer, will not call destructors on its values, use destroy pointee or any other move methods from above.

#### `DTypePointer`: handling numeric data[​](https://docs.modular.com/mojo/manual/pointers#dtypepointer-handling-numeric-data "Direct link to dtypepointer-handling-numeric-data")

A [`DTypePointer`](https://docs.modular.com/mojo/stdlib/memory/unsafe/DTypePointer) is an unsafe pointer that supports some additional methods for loading and storing numeric data. Like the [`SIMD`](https://docs.modular.com/mojo/stdlib/builtin/simd/SIMD) type, it's parameterized on [`DType`](https://docs.modular.com/mojo/stdlib/builtin/dtype/DType) as described in [SIMD and DType](https://docs.modular.com/mojo/manual/types#simd-and-dtype).

- `DTypePointer` works with are trivial types, so no copy or move or destroy methods required.
- Has [`alloc()`](https://docs.modular.com/mojo/stdlib/memory/unsafe/DTypePointer#alloc) , [`free()`](https://docs.modular.com/mojo/stdlib/memory/unsafe/DTypePointer#free) and [`address_of()`](https://docs.modular.com/mojo/stdlib/memory/unsafe/DTypePointer#address_of) 
- use subscript notation `[]` or use the [`load()`](https://docs.modular.com/mojo/stdlib/memory/unsafe/DTypePointer#load) and [`store()`](https://docs.modular.com/mojo/stdlib/memory/unsafe/DTypePointer#store) methods to access values.
- Use [`simd_strided_load()`](https://docs.modular.com/mojo/stdlib/memory/unsafe/DTypePointer#simd_strided_load) and [`simd_strided_store()`](https://docs.modular.com/mojo/stdlib/memory/unsafe/DTypePointer#simd_strided_store) methods for efficient SIMD operations

Note:  `DTypePointer` is depreciated. `UnsafePointer` can handle most things that `DTypePointer` does except for SIMD operations. In future `SIMD` type supports all these operations, so  `UnsafePointer` can just use them.


#### Safety[​](https://docs.modular.com/mojo/manual/pointers#safety "Direct link to Safety")

Unsafe pointers are unsafe for several reasons:
- Memory management is up to the user. 
- `UnsafePointer` and `DTypePointer` values are _nullable_ or can be _initialized_.
- Mojo doesn't track lifetimes for the data pointed to by an `UnsafePointer`, so managing memory and knowing when to destroy objects is user responsibility.

#### ​Reference[](https://docs.modular.com/mojo/manual/pointers#unsafepointer-and-reference "Direct link to unsafepointer-and-reference")

The [`Reference`](https://docs.modular.com/mojo/stdlib/memory/reference/Reference) type is essentially a safe pointer type.
- `Reference` is _non-nullable_. A reference always points to something.
- No alloc or free on `Reference`— only point to an existing value.
- `Reference` only refers to a single value. You can't do pointer arithmetic with a `Reference`.
- `Reference` has an associated _lifetime_, which connects it back to an original, owned value. The lifetime ensures that the value won't be destroyed while the reference exists.

The `Reference` type shouldn't be confused with the immutable and mutable references used with the `borrowed` and `inout` argument conventions. Those references do not require explicit dereferencing, unlike a `Reference` or `UnsafePointer`.

​#### Arc
Reference-counted smart pointers
