

## @register_passable

All the arguments and variables of this decorator should adhere to types that should be passed in machine registers (like CPU registers). This mean all these types should always be passed by value and cannot be passed by reference. These structs cannot hold values that are not register passable.

Types:
- @register_passable
	- should implement `__init__`, `__copyinit__`, `__del__` and no move.
- @register_passable("trivial")
	- 
- @value

@register_passable