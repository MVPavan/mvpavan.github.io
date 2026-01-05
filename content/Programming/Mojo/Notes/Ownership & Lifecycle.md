
In Value ownership and value lifecycle, value is usually referred to argument values in functions.

- `read` - immutable reference (this is default, if you don't mention any)
- `mut` - mutable reference
- `out` - A special convention used for the `self` argument in constructor and named result. An `out` argument is uninitialized at the beginning of the function, and must be initialized before the function returns. Although `out` arguments show up in the argument list, they're never passed in by the caller.
- `var` - function takes ownership of value, it can happen in two ways, he caller can transfer ownership (using `^`) if not the callee might receive a newly-created value, or a copy of an existing value.
- `deinit` - Used in the destructor and consuming-move lifecycle methods


Here is the complete summary for `var` arguments in Mojo, covering every combination of struct capabilities and calling styles:

| Logic     | Struct Capability   | WITHOUT `^`             | WITH `^`                       |
| --------- | ------------------- | ----------------------- | ------------------------------ |
| Pure Copy | `__copyinit__` only | Copy (Original stays ✅) | Bitwise Move (Original dies ❌) |
| Pure Move | `__moveinit__` only | Compile Error ❌         | Move (Original dies ❌)         |
| Standard  | Both implemented    | Copy (Original stays ✅) | Move (Original dies ❌)         |
 Key Observations:
1. Without `^`: Mojo tries to be safe. It will only let you pass the variable if it can safely duplicate it. If it can't (no copy or move / or move-only type), it stops the program during compilation.
2. With `^`: Mojo tries to be fast. It ignores your "Copy" logic entirely. Even if you haven't written a "Move" constructor, it will perform a raw Bitwise Move of the fields to ensure the transfer happens with zero overhead.
3. The "Dead" State: Regardless of _how_ the move happens (custom logic or bitwise), once you use `^`, the original variable is gone. You cannot use it again in the same function.