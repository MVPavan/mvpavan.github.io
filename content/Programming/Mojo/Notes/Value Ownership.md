
Here value is usually referred to argument values in functions.

- read - immutable reference (this is default, if you don't mention any)
- mut - mutable reference
- out - A special convention used for the `self` argument in constructor and named result. An `out` argument is uninitialized at the beginning of the function, and must be initialized before the function returns. Although `out` arguments show up in the argument list, they're never passed in by the caller.
- `var` - function takes ownership of value, it can happen in two ways, he caller can transfer ownership (using `^`) if not the callee might receive a newly-created value, or a copy of an existing value.
