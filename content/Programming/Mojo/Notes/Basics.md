
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

```
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

```
def repeat[count: Int](msg: String):
    @parameter # evaluate the following for loop at compile time    
    for i in range(count):
            print(msg)
```

count - parameter, msg - argument
count wont change during runtime, where as msg can change.
@paramete decorator mentions compiler to optimize/evaluate for loop during compile time.  This can contribute to runtime performance.


