package main

import (
	"fmt"
	"math"
)

type FastNum struct {
	Arr   [8]byte
	place uint
}

func NewFastNum() FastNum {
	var f FastNum
	f.Arr = [8]byte{1}
	f.place = 1
	return f
}

func (f *FastNum) CountZeros() uint {
	var count uint

	for i := uint(0); i <= f.place; i++ {
		if f.Arr[i] == 0 {
			count++
		}
	}
	return count
}

func (f *FastNum) Incr() {
	var i uint
	for {
		if f.Arr[i] < 9 {
			f.Arr[i]++
			if i >= f.place {
				f.place = i + 1
			}
			return
		} else {
			f.Arr[i] = 0
		}
		i++
	}
}

func (f *FastNum) ExtractMap(replacer uint, mutation byte) uint {
	var result, pow, temp uint
	var zeroCounter byte
	pow = 1

	for i := uint(0); i <= f.place+1; i++ {
		temp = uint(f.Arr[i])
		if f.Arr[i] == 0 {
			if ((1 << zeroCounter) & mutation) > 0 {
				temp = replacer
			}
			zeroCounter++
		}
		result += temp * pow
		pow *= 10
	}
	return result
}

func IntPow(b, e int) int {
	return int(math.Pow(float64(b), float64(e)))
}

func main() {
	MAX := uint(10000000)
	s := NewSieve(MAX)

	f := NewFastNum()
	for i := uint(10); i < MAX; i++ {
		zeros := f.CountZeros()
		if zeros > 0 {
			mutatorMax := byte(IntPow(2, int(zeros)))
			for mutator := byte(1); mutator < mutatorMax; mutator++ {
				count := 0
				for j := uint(0); j <= 9; j++ {
					if s.isPrime(f.ExtractMap(j, mutator)) {
						count++
					}
				}
				if count >= 8 {
					for repl := uint(0); repl <= 9; repl++ {
						fmt.Println(f.ExtractMap(repl, mutator), s.isPrime(f.ExtractMap(repl, mutator)), mutator)
					}
					return
				}
			}
		}
		f.Incr()
	}
}
