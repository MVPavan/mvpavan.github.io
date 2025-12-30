
## Variables

- Explicit declared `var x:Int or var x:Int = 10 or var x = 10`
- Implicit declared  `x = 10 or x:Int = 10 or x:Int`
- Both implicit and explicit declared variables are strongly typed, either explicitly set with type annotation or implicit with first initialized value.
- Once initialized variable type cannot be changed (unlike python) except implicit conversion
- Implicit conversion: Int --> Float, StringLiteral --> String  etc.
- One scoping difference between `var` and normal variables, is variable shadowing is only possible with `var` declared.

```mojo
def function_scopes():
    num = 1
    if num == 1:
        print(num)   # Reads the function-scope "num"
        num = 2      # Updates the function-scope variable
        print(num)   # Reads the function-scope "num"
    print(num)       # Reads the function-scope "num"
1  
2  
2

def lexical_scopes():
    var num = 1
    var dig = 1
    if num == 1:
        print("num:", num)  # Reads the outer-scope "num"
        var num = 2         # Creates new inner-scope "num" (Variable shadowing)
        print("num:", num)  # Reads the inner-scope "num"
        dig = 2             # Updates the outer-scope "dig"
    print("num:", num)      # Reads the outer-scope "num"
    print("dig:", dig)      # Reads the outer-scope "dig"
num: 1  
num: 2  
num: 1  
dig: 2 
```

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

- `fn` : compiler doesn't allow fn to raise error without explicit raises
- `def` : is always treated as raising function by default irrespective of the `def` code
- If a non-raising function calls a raising function, it must handle any possible errors

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

###  Copy Elision

Or RVO - Return Value Optimization

```
struct ImmovableObject:
    var name: String    
    fn __init__(out self, var name: String):
            self.name = name^

def create_immovable_object(var name: String, out obj: ImmovableObject):    
	obj = ImmovableObject(name^)    
	obj.name += "!"    # obj is implicitly returned

def main():    
	my_obj = create_immovable_object("Blob")

def create_immovable_object2(var name: String) -> ImmovableObject:
    obj = ImmovableObject(name^)
    obj.name += "!"
    return obj^ # Error: ImmovableObject is not copyable or movable

def create_immovable_object3(var name: String) -> ImmovableObject:
    return ImmovableObject(name^) # OK
```

- `ImmovableObject` cannot be moved or copied, no `__copy__ or __move__` defined
- `create_immovable_object2` error because `obj` is created here and is not movable or copyable
- `create_immovable_object` works because `obj` is `out` object, its created by caller, here its only referenced by memory, once function completes, caller will have the modified `obj`
- `create_immovable_object3` also works because its an intelligent optimization done by compiler, return object is not created in `create_immovable_object3` scope, rather in caller scope. However for this happen, `return` has to be immediate after obj creation, no modifications can be done on obj.