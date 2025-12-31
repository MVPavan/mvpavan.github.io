

## @register_passable

All the arguments and variables of this decorator should adhere to types that should be passed in machine registers (like CPU registers). This mean all these types should always be passed by value and cannot be passed by reference. These structs cannot hold values that are not register passable.

Types:
- @register_passable
  - should implement `__init__`, `__copyinit__`, `__del__` and no move.
- @register_passable("trivial")
  - can only define `__init__` not mandatory, other are only defined by compiler.
  - Arithmetic types such as `Int`, `Bool`, `Float64` etc.
  - Pointers (the address value is trivial, not the data being pointed to).
  - Arrays of other trivial types, including SIMD.

## @fieldwise_init
It tells the compiler to automatically write the constructor `__init__` for your  struct
### @fieldwise_init("implicit")
it allows the struct to be implicitly converted from its fields

## @always_inline

Mojo compiler copies the body of this function to body of the function where its being called. This avoids performance costs associated with function calls, but it increases binary size.
### @always_inline('nodebug')
Same as above but without debug info, debugger cannot step into this function when debugging, should be used with low level code.

## @value

Generates boilerplate lifecycle methods. `__init__`, `__copyinit__`, `__moveinit__`,`__del__`


## @parameter

1. Over If condition - will be evaluated at compile time. If condition should be valid parameter expression
2. Over for loop -  will be evaluated at compile time, loop sequence and induction values must be valid parameter expressions.
3. Closure function - over nested function
  1. Closure function can capture variables or parameter from outer scope
  2. Use the closure function as a parameter.
> Though closure function contains dynamic values from outer loop, it can still be accessed as parameter.
  
### `@__copy_capture(variable_name)`

Passed on top of parameter closure to capture register passable values by copy. This copies the mentioned variable in to closure function by value rather capturing it by reference. This avoids any lifetime concerns regarding that variable.

