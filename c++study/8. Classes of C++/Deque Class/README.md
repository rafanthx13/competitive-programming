# Deque

http://www.cplusplus.com/reference/deque/deque/


Na Deque podeoms remover e inseiri tanto no início quanto no fim.

A fila comun não. Na fila comun só podmeos inserir no fim e tirar do começo.

Double ended queues are sequence containers with the feature of expansion and contraction on both the ends.
They are similar to vectors, but are more efficient in case of insertion and deletion of elements. Unlike vectors, contiguous storage allocation may not be guaranteed.
Double Ended Queues are basically an implementation of the data structure double ended queue. A queue data structure allows insertion only at the end and deletion from the front. This is like a queue in real life, wherein people are removed from the front and added at the back. Double ended queues are a special case of queues where insertion and deletion operations are possible at both the ends.

The functions for deque are same as vector, with an addition of pus and pop operations for both front and back.

push()

assign
Assign container content (public member function )
push_back
Add element at the end (public member function )
push_front
Insert element at beginning (public member function )
pop_back
Delete last element (public member function )
pop_front
Delete first element (public member function )
insert
Insert elements (public member function )
erase
Erase elements (public member function )
swap
Swap content (public member function )
clear
Clear content (public member function )
emplace 
Construct and insert element (public member function )
emplace_front 
Construct and insert element at beginning (public member function )
emplace_back 
Construct and insert element at the end (public member function )