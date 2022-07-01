package main

import (
	"fmt"
)

func ReverseWords(str string) string {
	fmt.Println("Hello, world!")

	/*
		* loop thru each char (while i <= len(str)-1)
		* if i != ' ':
			* j = i
			* while str[j+1] != ' ', j++
			i = j+1
		* if i == ' ':
			* reverse and add tmp to reversed


		 i = 0
		 j = 19

		    k
		     i
		"This is an example!"

	*/
	buffer := []byte(str)
	for i, j := 0, len(buffer)-1; i < j; i++ {
		if str[i] != ' ' {
			// find end of word (k)
			k := i
			for k < j && str[k+1] != ' ' {
				k++
			}

			// reverse word
			for n, l := i, k; n < l; n, l = n+1, l-1 {
				buffer[n], buffer[l] = str[l], str[n]
			}

			i = k + 1
		}
	}
	fmt.Println("after reverse: " + string(buffer))
	return string(buffer)

	/*
		in_str := false
		var chars []byte
		var reversed bytes.Buffer

		for _, c := range str {
			fmt.Println(string(c))
			if c == ' ' {
				if in_str == true {
					for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
						chars[i], chars[j] = chars[j], chars[i]
					}
					reversed.WriteByte(chars)
					in_str = false
				} else {
					reversed.WriteString(" ")
				}
			} else if in_str == false {
				in_str = true
				runes = append(b, c)
			} else if in_str == true {
				// do nothing
				runes = append(b, c)
			}
		}
		// fields := strings.Fields(str)
		// for _, strs := range fields {
		// 	fmt.Println(strs)
		// }
		return reversed
	*/
}

func main() {
	ReverseWords("This is an example!") // ==> "sihT si na !elpmaxe"
	ReverseWords("double  spaces")      // ==> "elbuod  secaps")
}
