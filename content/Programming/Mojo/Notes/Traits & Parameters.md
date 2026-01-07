# Traits

In dynamic languages like Python, you can pass any object to any function. But you must make sure the object implements the methods you call in that function, or you'll get a nasty runtime error.

This is where Traits come, like an abstract type, create a trait and declare a function but don't implement it, in fact implementation and default values are not supported (yet).

Any function inheriting this trait should implement its methods.

```
trait Shape:
    fn area(self) -> Float64:
        ...

@value
struct Circle(Shape):
    var radius: Float64

    fn area(self) -> Float64:
        return 3.141592653589793 * self.radius ** 2


fn print_area[T: Shape](shape: T):
    print(shape.area())
```

- Traits can inherent from other traits.

# Parameters
overview: [[Basics#Parameterization|Parameters overview]]

- generics use parameters to specify types, generics are functions/containers that can act on multiple types of values.
- `//` in parameter list indicates that everything before it is only infer type.
- 