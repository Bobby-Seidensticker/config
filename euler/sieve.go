package main

import (
	"fmt"

	"github.com/willf/bitset"
)

func NewSieve(i uint) Sieve {
	var s Sieve
	s.FillTo(i)
	s.Top = i
	return s
}

type Sieve struct {
	Set *bitset.BitSet
	Top uint
}

func (s *Sieve) FillTo(stop uint) {
	s.Set = bitset.New(stop)
	s.Set.Set(0)
	s.Set.Set(1)
	for i := uint(2); i < stop; i++ {
		if !s.Set.Test(i) {
			for j := i * 2; j < stop; j += i {
				s.Set.Set(j)
			}
		}
	}
}

func (s *Sieve) isPrime(i uint) bool {
	if i > s.Top {
		return false
	}
	return !s.Set.Test(i)
}

func test() {
	s := NewSieve(1000000)

	for i := uint(2); i < 25; i++ {
		if s.isPrime(i) {
			fmt.Println(i)
		}
	}
}
