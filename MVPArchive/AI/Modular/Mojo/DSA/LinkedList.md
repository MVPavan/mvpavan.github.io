https://github.com/MVPavan/mojos/blob/master/learn/dsa/my_linked_list.mojo

## Memory Lifecycle

Follow code for understanding, below data represents deleting a linked list from memory.
```
		Node Ptr       Data Ptr        next Ptr       prev Ptr
node:  0x55f7fa166120 0x55f7fa164048 0x55f7fa166100 0x0             (Head)
node:  0x55f7fa166100 0x55f7fa164040 0x55f7fa1660e0 0x55f7fa166120
node:  0x55f7fa1660e0 0x55f7fa164038 0x55f7fa1660c0 0x55f7fa166100
node:  0x55f7fa1660c0 0x55f7fa164030 0x55f7fa1660a0 0x55f7fa1660e0
node:  0x55f7fa1660a0 0x55f7fa164028 0x55f7fa166160 0x55f7fa1660c0
node:  0x55f7fa166160 0x55f7fa164060 0x55f7fa166000 0x55f7fa1660a0
node:  0x55f7fa166000 0x55f7fa164000 0x55f7fa166040 0x55f7fa166160
node:  0x55f7fa166040 0x55f7fa164010 0x55f7fa166060 0x55f7fa166000
node:  0x55f7fa166060 0x55f7fa164018 0x55f7fa166080 0x55f7fa166040
node:  0x55f7fa166080 0x55f7fa164020 0x0            0x55f7fa166060  (Tail)

deleting node:  0x55f7fa166080
deleting data value:  40
freeing data:  0x55f7fa164020

deleting node:  0x55f7fa166060
deleting data value:  30
freeing data:  0x55f7fa164018
freeing next ptr:  0x55f7fa166080 (above deletd node)

deleting node:  0x55f7fa166040
deleting data value:  20
freeing data:  0x55f7fa164010
freeing next ptr:  0x55f7fa166060

deleting node:  0x55f7fa166000
deleting data value:  5
freeing data:  0x55f7fa164000
freeing next ptr:  0x55f7fa166040

deleting node:  0x55f7fa166160
deleting data value:  108
freeing data:  0x55f7fa164060
freeing next ptr:  0x55f7fa166000

deleting node:  0x55f7fa1660a0
deleting data value:  -5
freeing data:  0x55f7fa164028
freeing next ptr:  0x55f7fa166160

deleting node:  0x55f7fa1660c0
deleting data value:  -10
freeing data:  0x55f7fa164030
freeing next ptr:  0x55f7fa1660a0

deleting node:  0x55f7fa1660e0
deleting data value:  -20
freeing data:  0x55f7fa164038
freeing next ptr:  0x55f7fa1660c0

deleting node:  0x55f7fa166100
deleting data value:  -30
freeing data:  0x55f7fa164040
freeing next ptr:  0x55f7fa1660e0

deleting head:  0x55f7fa166120
deleting data value:  -40
freeing data:  0x55f7fa164048
freeing next ptr:  0x55f7fa166100

Freeing head:  0x55f7fa166120
```

### Observations

1. `head = UnsafePointer[Node[T]].address_of(Node[T](value))`, here `head` is assigned address of `created Node[T]`, however `Node` dies with ASAP destructor immediately, making `head` a dangling pointer.
2. So use `address_of` only to refer to already created variables and should agree to follow variable's lifetime.
3. Instead use 
	```
	head = head.alloc(1)
	initialize_pointee_move(head, Node[T](value))
	```
	This creates buffer and copies the new node to buffer and the lifecycle of head and its value is in our hands now.