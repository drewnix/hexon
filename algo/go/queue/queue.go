package main

import "fmt"

type node struct {
	 prev *node
	 next *node
	 data int
}

type queue struct {
	head *node
	tail *node
}

func (q *queue) enqueue(item int) {
	n := node{
		data: item,
		next: q.head,
		prev: nil,
	}
	if n.next == nil {
		q.tail = &n
	} else {
		n.next.prev = &n
	}
	q.head = &n
}

func (q *queue) dequeue() (int, bool) {
	if q.tail != nil {
		rec := q.tail
		if rec.prev != nil {
			q.tail = rec.prev
			rec.prev.next = nil
		} else {
			q.tail = nil
		}
		return rec.data, true
	} else {
		return 0, false
	}
}

func main() {
	var q queue
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.enqueue(5)
	q.enqueue(6)
	fmt.Println(q.dequeue())
	fmt.Println(q.dequeue())
	fmt.Println(q.dequeue())
	fmt.Println(q.dequeue())
	fmt.Println(q.dequeue())
	fmt.Println(q.dequeue())
	fmt.Println(q.dequeue())
}