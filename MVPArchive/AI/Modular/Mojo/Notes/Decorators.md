
## @value

Generates boilerplate lifecycle methods. `__init__`, `__copyinit__`, `__moveinit__`,`__del__`

## @register_passable

All the arguments and variables of this decorator should adhere to types that should be passed in machine registers (like CPU registers). This mean all these types should always be passed by value and cannot be passed by reference. These structs cannot hold values that are not register passable.

Types:
- @register_passable
	- should implement `__init__`, `__copyinit__`, `__del__` and no move.
- @register_passable("trivial")
	- can only define `__init__` not mandatory, other are only defined by compiler.
	- Arithmetic types such as `Int`, `Bool`, `Float64` etc.
	- Pointers (the address value is trivial, not the data being pointed to).
	- Arrays of other trivial types, including SIMD.