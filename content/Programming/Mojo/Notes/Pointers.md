
## Origin

- Every variable that lives in memory has a unique Origin. The Mojo compiler uses this to track the **Identity** and **Lifetime** of that memory.
- If you have a `String`  (which owns its memory), it has a specific origin. If you create a `StringSlice` (which is just a "window" into that string), the slice **carries the same Origin** as the original string. This tells the compiler: _"This slice is only valid as long as the original string is still alive."_
- `origin_of()`: You can get the Origin of any variable using this built-in operator. This happens entirely during compilation.

### Types

- `MutOrigin`: A mutable origin (you can change the memory).
- `ImmutOrigin`: An immutable origin (read-only).
- `StaticConstantOrigin`: A special origin for things that **live forever** in your program's binary (like hard-coded `StringLiteral` values).