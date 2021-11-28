/**
* Syntax Test "Toit.sublime-syntax"
*/

import pubsub
export *
topic ::= "device:hello-world"

class Cat:

	say_hello: print "Meow, $name"

	say_bye: print "Bye $name! Come back soon."

fib n:
	if n <= 1: return n
	return (fib n-1) + (fib n-2)

fibonacci n:
	a := 0
	b := 1
	n.repeat:
		c := a + b
		a = b
		b = c
	return a

main:
	// This is comment
	// ...
	/*
	* And
	* This
	*/
	arr := ["John", 4, "Doe", 0]
	arr.do: print "Element: $it"
	constructor name = "world":
		arr.add name
	x := null
	print "$x"
	for i := 0; i < 10; i++:
		print ""

	kitten := Cat

	print "The 10-th Fibonacci number is $(fib 10)"
	pubsub.subscribe topic: | msg/pubsib.Message |
		print "Received message '$msg.payload.to_string'"
		return
