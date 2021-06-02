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

func (ll *linkedList) insert(value int) *node {
	h := ll.head
	n := node{h, nil, value}
	ll.head = &n
	return &n
}

func (ll *linkedList) display() {
	n := ll.head
	for n != nil {
		fmt.Printf("%d --> ", n.value)
		n = n.next
	}
}

func (ll *linkedList) reverse() {
	n := ll.head
	for n != nil {

	}

}

func main() {
	linked.insert(15)
	linked.insert(12)
	linked.insert(111)
	linked.display()

}

