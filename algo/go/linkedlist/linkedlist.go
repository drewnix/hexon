package main

import "fmt"

type node struct {
	next *node
	prev *node
	value int
}

type linkedList struct {
	head *node
	tail *node
}

var linked linkedList

func (l *linkedList) insert(value int) *node {
	h := l.head
	n := node{h, nil, value}
	l.head = &n
	return &n
}

func (l *linkedList) display() {
	n := l.head
	for n != nil {
		fmt.Printf("%d", n.value)
		n = n.next
		if n != nil {
			fmt.Printf(" --> ")
		}
	}
	fmt.Printf("\n")
}

func (l *linkedList) reverse() {
	curr := l.head
	var prev *node = nil

	for curr != nil {
		next := curr.next
		curr.next = prev
		prev = curr
		curr = next
	}
	l.head = prev
}

func main() {
	linked.insert(15)
	linked.insert(12)
	linked.insert(111)
	linked.display()
	linked.reverse()
	linked.display()
}

