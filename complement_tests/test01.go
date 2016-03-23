package main

import (
	"fmt"
	"log"
	"math/big"
)

func main() {
	fmt.Println("1.", -1<<1)
	fmt.Println("2.", -1>>1)
	fmt.Println("3.", -1>>2)
	fmt.Println("4.", -1>>3)
	fmt.Println("5.", -1>>128)
	fmt.Println("6.", -1<<63)
	fmt.Println("7.", -0>>64)
	fmt.Println("8.", 1<<62)
	i := new(big.Int)
	_, err := fmt.Sscan("18446744073709551617", i)
	if err != nil {
		log.Println("error scanning value:", err)
	} else {
		fmt.Println(i)
	}
}
