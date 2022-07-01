package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"strings"
)

/*
 * Complete the 'customSorting' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts STRING_ARRAY strArr as parameter.
 */

type byCustom []string

func (s byCustom) Len() int {
	return len(s)
}
func (s byCustom) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s byCustom) Less(i, j int) bool {
	if len(s[i])%2 != 0 && len(s[j])%2 == 0 {
		return false
	} else if len(s[i])%2 != 0 && len(s[j])%2 != 0 {
		if len(s[i]) > len(s[j]) {
			return false
		}
	} else if len(s[i])%2 == 0 && len(s[j])%2 == 0 {
		if len(s[i]) < len(s[j]) {
			return false
		}
	}
	return true
}


func customSorting(strArr []string) []string {
	sort.Sort(byCustom(strArr))
	return strArr
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

	strArrCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var strArr []string

	for i := 0; i < int(strArrCount); i++ {
		strArrItem := readLine(reader)
		strArr = append(strArr, strArrItem)
	}

	result := customSorting(strArr)

	for i, resultItem := range result {
		fmt.Fprintf(writer, "%s", resultItem)

		if i != len(result) - 1 {
			fmt.Fprintf(writer, "\n")
		}
	}

	fmt.Fprintf(writer, "\n")

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}



func main() {
	fmt.Println("hello!!")
}