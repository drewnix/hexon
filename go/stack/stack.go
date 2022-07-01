package main

import "fmt"

type stack struct {
	data []int
}

func (s *stack) push(item int) {
	s.data = append(s.data, item)
}

func (s *stack) pop() int {
	item := s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	return item
}

func (s *stack) peek() int {
	return s.data[len(s.data)-1]
}

func main() {
	var st stack

	st.push(4)
	st.push(5)
	st.push(7)
	st.push(9)
	st.push(1)

	fmt.Println(st.pop())
	fmt.Println(st.pop())
	fmt.Println(st.pop())
	fmt.Println(st.peek())
}