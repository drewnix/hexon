package main

import "fmt"

func bubbleSort(items []int) []int {
	for range items {
		for i, _ := range items {
			if i != len(items)-1 {
				if items[i] > items[i+1] {
					items[i], items[i+1] = items[i+1], items[i]
				}
			}
		}
	}
	return items
}

func selectionSort(items []int) []int {
	min := 0
	for i := 0; i < len(items); i++ {
		min = i
		for j := i+1; j < len(items); j++ {
			if items[j] < items[min] {
				min = j
			}
		}
		items[i], items[min] = items[min], items[i]
	}
	return items
}

func insertionSort(items []int) []int {
	for i := 1; i < len(items); i++ {
		for j := i; j > 0; j-- {
			if items[j-1] > items[j] {
				items[j-1], items[j] = items[j], items[j-1]
			}
		}
	}
	return items
}

func main() {
	items := []int{6, 2, 156, 22, 667452, 12, 345, 6}
	//sorted := bubbleSort(items)
	//sorted := selectionSort(items)
	sorted := insertionSort(items)
	fmt.Println(sorted)
}