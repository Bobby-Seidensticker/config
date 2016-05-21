package main

import (
	"fmt"
	"time"
)

func main() {
	COUNT := uint(1000000000)

	t := time.Now()

	sieve := NewSieve(COUNT)

	fmt.Println("Done making sieve, took:", t.UnixNano()-time.Now().UnixNano())

	i := uint(1)
	primes := 0
	onDiag := 1

	for edge := uint(3); edge < 10000000 && i < COUNT; edge += 2 {
		k := edge - 1
		for j := 0; j < 4; j++ {
			onDiag++
			i += k
			if sieve.isPrime(i) {
				primes++
			}
		}
		ratio := float64(primes) / float64(onDiag)
		if edge%1000 == 1 {
			fmt.Println(edge, primes, onDiag, ratio)
		}
		if ratio < .1 {
			fmt.Println(edge)
			return
		}
	}
	fmt.Println("nothin'")
}
