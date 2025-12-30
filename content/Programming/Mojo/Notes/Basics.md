
## Variables

- Explicit declared `var x:Int or var x:Int = 10 or var x = 10`
- Implicit declared  `x = 10`

Bothe implicit and explicit declared variables are statically typed - set in compile time, don't change at runtime.

## Struct

- Fixed memory: Compared to python class once declared you cannot add new variables at run time, once mojo struct is declared its memory is fixed and static
- Though the variable inside struct can be a pointer with dynamic memory in heap, struct which holds these variables is always fixed.
- Comparison Table

|Property|Struct Memory|Heap Memory (Data)|
|---|---|---|
|**Location**|Inline (Stack or Registers)|External (Heap)|
|**Size**|Fixed at Compile-Time|Variable at Runtime|
|**Responsibility**|Manages the "Handle"|Stores the "Payload"|

## Trait

``` mojo
trait SomeTrait:
	fn required_method(self, x: Int): ...

@fieldwise_init
struct SomeStruct(SomeTrait):    
	fn required_method(self, x: Int):        
		print("hello traits", x)

fn fun_with_type(x: SomeStruct):
	x.required_method(42)

fn fun_with_traits[T: SomeTrait](x: T):
    x.required_method(42)

fn use_trait_function():    
	var thing = SomeStruct()    
	fun_with_traits(thing)

```

- `SomeStruct` conforms to `SomeTrait` by implementing `required_method`
- `fun_with_type` `x` has strict type conform to `SomeStruct`, where as `fun_with_triat` any `xyzStruct` can be passed if it conforms to `SomeTrait` by implementing `required_method`, now `fun_with_traits` is more generic compared to `fun_with_type`.

## Parameterization

Compile time variable that becomes runtime constant. It allows compile time metaprogramming.
Metaprogramming refers to a variety of ways a program has knowledge of itself or can manipulate itself. In our case it can use parameters and modify itself during compile time.

Argument - run time value for functions.

```mojo
def repeat[count: Int](msg: String):
    @parameter # evaluate the following for loop at compile time    
    for i in range(count):
            print(msg)
```

count - parameter, msg - argument
count wont change during runtime, where as msg can change.
@paramete decorator mentions compiler to optimize/evaluate for loop during compile time.  This can contribute to runtime performance.


## Functions

### def vs fn

- compiler doesn't allow fn to raise error without explicit raises

### Return values

- syntax: `fn  -> type`
- By default value is returned to called as an owned value
- value may be implicitly converted to return type
-  can also return a mutable or immutable reference using a `ref` return value

### Named Results

```mojo
def get_name_tag(var name: String, out name_tag: NameTag):
    name_tag = NameTag(name^)
```

- allow a function to return a value that can't be moved or copied
- function must initialize the out argument, by default its uninitialized
- no explicit return required, if valid return is included its returned as usual 
- A function can declare only one return value, whether it's declared using an `out` argument or using the standard `-> type` syntax

```
def get_name_tag(var name: String) -> NameTag:    ...
def get_name_tag(var name: String, out name_tag: NameTag):    ...
```

In both cases, the call looks like this:

```
tag = get_name_tag("Judith")
```

`...` in mojo functions represents its not defined now and should be defined by who ever uses it. 