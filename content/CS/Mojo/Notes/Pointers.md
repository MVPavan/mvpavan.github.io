## Pointers

Pointee - value pointed by a pointer
Pointer dereferencing: `ptr[]`
### Terms

- **Safe pointers**: Memory safe    
- **Nullable pointers**: can point to an invalid memory location (typically 0, or a “null pointer”). Safe pointers aren't nullable.    
- **Smart pointers**: 
	- own their pointees, which means that the value they point to may be deallocated when the pointer itself is destroyed.
	- Non-owning pointers may point to values owned elsewhere, or may require some manual management of the value lifecycle.
- **Memory allocation**: 
	- some pointer types can allocate memory to store their pointees, while other pointers can only point to pre-existing values. 
	- Memory allocation can either be implicit (that is, performed automatically when initializing a pointer with a value) or explicit. 
- **Uninitialized memory**: Memory location that haven't been initialized with a value(contain random data). 
	- Newly-allocated memory is uninitialized. 
	- The safe pointer types don't allow users to access memory that's uninitialized. 
	- Unsafe pointers can allocate a block of uninitialized memory locations and then initialize them one at a time. Being able to access uninitialized memory is unsafe by definition.
- **Copyable types**: 
	- Implicitly copyable types: `copied_ptr = ptr`
	- Explicitly copyable types: copy, using a constructor with a keyword argument `copied_owned_ptr = OwnedPointer(other=owned_ptr)`

### Types

- `pointer`: Safer pointer to a single initialized value that is not owned
- `OwnedPointer`: Smart pointer to a single value, has exclusive ownership of the value
- `ArcPointer`: Reference counted smart pointer shared with other instances of `ArcPointer`
- `UnsafePointer`: points to one or more consecutive memory locations (can be uninitialized memory)

Note:
- Except `UnsafePointer` all other can only point to single value, not anything like array.
- except `OwnedPointer` all other are implicitly copyable.

### UnsafePointer

![[Pasted-image-20260108221717.png]]

- `init_pointee_move`: Move a value to pointer memory location
- `init_pointee_copy`: Copy a value to pointer memory location
- `UnsafePointer(to=value)`: Constructor to point to an existing value
- `take_pointee`: Moves a pointee from memory location pointed by `ptr`. Its consuming move, using `__moveinit__`
- `destroy_pointee`: Calls destructor on pointee, leaves `ptr` uninitialized
- `free`: Frees the memory allocated by `ptr`, results in `dangling pointer`


## Origin

- Every variable that lives in memory has a unique Origin. The Mojo compiler uses this to track the **Identity** and **Lifetime** of that memory.
- If you have a `String`  (which owns its memory), it has a specific origin. If you create a `StringSlice` (which is just a "window" into that string), the slice **carries the same Origin** as the original string. This tells the compiler: This slice is only valid as long as the original string is still alive.
- `origin_of()`: You can get the Origin of any variable using this built-in operator. This happens entirely during compilation.

### Types

- `MutOrigin`: A mutable origin (you can change the memory).
- `ImmutOrigin`: An immutable origin (read-only).
- `StaticConstantOrigin`: A special origin for things that **live forever** in your program's binary (like hard-coded `StringLiteral` values).