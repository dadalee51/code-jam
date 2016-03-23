package main

import (
	"fmt"
)

type B struct {
	val int
}

type C struct {
	x, y, r int
	B
}

type D struct {
	C
}

func main() {
	d := D{C{0, 0, 6, B{1}}}
	fmt.Println(d)
}
