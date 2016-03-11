package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	fmt.Println("solving wood logger problem:")
	price := make([]int, rand.Intn(20))
	for i := range price {
		price[i] = rand.Intn(100)
	}
	fmt.Println(price)
	cost := make([]int, len(price)+1)
	for j := 1; j <= len(price); j++ { //choice of lengths : 1 to n.
		maxVal := -1
		for k := 0; k < j; k++ { //
			maxVal = max(maxVal, price[k]+cost[j-k-1])
		}
		cost[j] = maxVal
	}

	fmt.Println("the best cost is:", cost[len(price)])

}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
