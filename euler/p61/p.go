package main

import (
	"fmt"

	"github.com/willf/bitset"
)

func tri(n float64) uint {
	return uint(n * (n + 1) / 2)
}

func quad(n float64) uint {
	return uint(n * n)
}

func pent(n float64) uint {
	return uint(n * (3*n - 1) / 2)
}

func main() {
	fmt.Println("hey")

	tris := bitset.New(10000)
	quads := bitset.New(10000)
	pents := bitset.New(10000)

	for i := float64(1); i < 1000; i++ {
		if tri(i) > 10000 {
			break
		}
		tris.Set(tri(i))
		if quad(i) < 10000 {
			quads.Set(quad(i))
		}
		if pent(i) < 10000 {
			pents.Set(pent(i))
		}
	}

	for i := uint(1000); i < 10000; i++ {
		if !tris.Test(i) || i % 100 < 10 {
			continue
		}
		start := (i % 100) * 100
		end := start + 100
		for j := start + 10; j < end; j++ {
			if !quads.Test(j) {
				continue
			}
			startk := (j % 100) * 100
			endk := start + 100
			for k := startk + 10; k < endk; k++ {
				if !pents.Test(k) {
					continue
				}
				if 
			}			
		}
	}
}
