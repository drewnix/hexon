package main

import "fmt"

type treeNode struct {
	left *treeNode
	right *treeNode
	data int
}

func levelOrderDFS(node *treeNode, depth int, levels [][]int) {
	if node == nil {
		return
	}
	levels[depth] = append(levels[depth], node.data)
	depth++
	levelOrderDFS(node.left, depth, levels)
	levelOrderDFS(node.right, depth, levels)
}

func levelOrderBFS(root *treeNode) []int {
	var res []int
	q := []treeNode{*root}

	for len(q) > 0 {
		qItems = len(q)
		tN := q[0]
		q = q[1:]
		res = append(res, tN.data)
		if tN.left != nil {
			q = append(q, *tN.left)
		}
		if tN.right != nil {
			q = append(q, *tN.right)
		}
	}

	return res
}

func main() {
	root := treeNode{nil, nil, 1}

	root.left = &treeNode{nil, nil, 2}
	root.left.right = &treeNode{nil, nil, 3}
	root.left.right.left = &treeNode{nil, nil, 5}
	root.left.right.left.right = &treeNode{nil, nil, 8}
	root.right = &treeNode{nil, nil, 12}
	root.right.right = &treeNode{nil, nil, 20}
	root.right.right.left = &treeNode{nil, nil, 22}

	//levelSlice := make([][]int, 0)
	//var levels [][]int = make([][]int, 10)
	//levelOrderDFS(&root, 0, levels)
	//fmt.Println(levels)
	fmt.Println(levelOrderBFS(&root))
}