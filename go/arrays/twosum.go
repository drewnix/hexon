package main

import (
	"errors"
	"fmt"
)

/*
==========
= Design =
==========

Constraints:
*

Algorithm:
O(n^2) two loops -> compare each number combination to 11, return the 2 that match
O(n) use map -> store each seen number in a map, with corresponding id

Testcases:
* "Happy Path"  [1, 3, 7, 9, 2] t = 11 -> [3, 4]
* "None which add up"  [1, 3, 7, 9, 2] t = 100  -> [], err = "None found"
* "Empty"  [] -> [], err = "None found"

 */

func twoSum(nums []int, target int) (int, int, error) {
	var numbers map[int]int = make(map[int]int, 0)
	for i, num := range nums {
		diff := target - num
		if number, ok := numbers[diff]; ok {
			return number, i, nil
		}
		numbers[num] = i
	}
	fmt.Println("No match")
	return 0, 0, errors.New("not found")
}

func main() {
	data := []int{1, 3, 7, 9, 2}
	target := 11
	num1, num2, err := twoSum(data, target)
	if err != nil {
		fmt.Printf("Failed to find two numbers in list that add up to target: %d\n", target)
	} else{
		fmt.Printf("Our two numbers %d and %d were at indexes: %d and %d\n", data[num1], data[num2], num1, num2)
	}
	fmt.Println("hello!!")
}