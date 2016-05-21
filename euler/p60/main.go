package main

import (
	"fmt"
	"math"

	"github.com/willf/bitset"
)

func digitLength(i uint) uint {
	var length, pow uint
	length = 1
	pow = 1
	for i >= pow {
		pow *= 10
		length += 1
	}
	return length - 1
}

func concat(i, j uint) uint {
	return uint(math.Pow10(int(digitLength(j))))*i + j
}

func main() {
	sieve := NewSieve(100000000)
	rels := make(map[uint]*bitset.BitSet)

	MAX := uint(100000)

	for i := uint(3); i < MAX; i++ {
		if !sieve.isPrime(i) {
			continue
		}
		for j := i + 1; j < MAX; j++ {
			if sieve.isPrime(j) && sieve.isPrime(concat(i, j)) && sieve.isPrime(concat(j, i)) {
				if _, ok := rels[i]; !ok {
					rels[i] = bitset.New(MAX)
					rels[i].Set(i)
				}
				if _, ok := rels[j]; !ok {
					rels[j] = bitset.New(MAX)
					rels[j].Set(j)
				}
				rels[i].Set(j)
				rels[j].Set(i)
			}
		}
	}

	for a := uint(3); a < MAX; a++ {
		if !sieve.isPrime(a) {
			continue
		}
		if otherSet, ok := rels[a]; ok {
			IterSets(a, 2, otherSet, rels)
		}
	}
}

func IterSets(k, depth uint, set *bitset.BitSet, rels map[uint]*bitset.BitSet) {
	REQUIRED := 5

	for i, e := set.NextSet(k + 1); e; i, e = set.NextSet(i + 1) {
		if otherSet, ok := rels[i]; ok {
			newSet := set.Intersection(otherSet)
			if newSet.Count() > uint(REQUIRED-1) &&
				depth > uint(REQUIRED-1) {
				PrintMatchStuff(newSet)
			}
			IterSets(i, depth+1, newSet, rels)
		}
	}
}

func PrintMatchStuff(newSet *bitset.BitSet) {
	s := uint(0)
	for i, e := newSet.NextSet(0); e; i, e = newSet.NextSet(i + 1) {
		s += i
		fmt.Printf("%d ", i)
	}
	fmt.Println(", sum:", s, "yatta!")
}
