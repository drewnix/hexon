package main

import (
	"fmt"
	"math"
)

//type treeNode struct {
//	left *treeNode
//	right *treeNode
//	data int
//}

func maxDepth(node *treeNode, depth float64) float64 {
	if node == nil {
		return depth
	}
	depth++
	return math.Max(maxDepth(node.left, depth), maxDepth(node.right, depth))
}

func main() {
	root := treeNode{nil, nil, 0}

	root.left = &treeNode{nil, nil, 3}
	root.left.right = &treeNode{nil, nil, 4}
	root.left.right.left = &treeNode{nil, nil, 15}
	root.left.right.left.right = &treeNode{nil, nil, 9}
	root.right = &treeNode{nil, nil, 9}
	root.right.right = &treeNode{nil, nil, 11}
	root.right.right.left = &treeNode{nil, nil, 65}

	fmt.Println(maxDepth(&root, 0))
}