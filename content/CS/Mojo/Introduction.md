[Mojo Manual | Modular](https://docs.modular.com/mojo/manual/)

Systems programming language developed from scratch with MLIR CPU+GPU

# Core Highlights

## Python Interop
Mojo Interoperability works in both directions, from python to Mojo and Mojo to python.

## Struct based types
All datatypes (int etc.) are defined as struct. User defined datatypes will have same capability as standard data types

## Traits
Zero cost. Functions/args can use traits instead of types. Traits can share multiple type behaviors. Compile time type checking, no performance cost in runtime.

## ASAP Destruction
Mojo during compile tracks the usage of variable rather than scope which many languages does (even c++). It then hardcodes to delete it immediately once the usage completes even without going out of scope.

If you have a large 1GB array and you use it on line 10, but your function goes on until line 100, Mojo can see that line 10 was the **last use**. It will deallocate that memory on line 11, even though the variable hasn't technically gone "out of scope" yet.

## Value ownership
Any specific value is always owned by only one variable at a given time. 
During compile mojo used technique called reference analysis, not reference counter like python.
### Reference Analysis
Usually in languages like python there is counter which keeps count of number of references for the variable, once the counter counts to zero it will be set to delete once out of scope, where as mojo during compile time, remembers who referenced it and who is actual owner, once after the reference or owner is last used, compiler hardcodes to delete it as per ASAP Destruction policy.

| Feature               | Python                     | Mojo                           |
| --------------------- | -------------------------- | ------------------------------ |
| **Mechanism**         | Runtime Reference Counting | Compile-time Lifetime Analysis |
| **Destruction**       | End of Scope / `del`       | Last Use (ASAP)                |
| **Runtime Overhead**  | High (updating counter)    | Zero (Static analysis)         |
| **Garbage Collector** | Yes                        | No                             |

## Compile-time Metaprogramming
During compile, based on compile time parameters unique function / type is generated, similar to C++ templates

## Hardware Portability
Mojo supports heterogeneous hardware, mojo compiler doesn't make any assumptions about hardware, instead hardware is handled in mojo libraries for both cpus and gpus.


