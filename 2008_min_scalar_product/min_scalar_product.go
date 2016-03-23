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

func main() {
	process("small.txt")
	process("large.txt")
}

func readInt(text string) int64 {
	a, _ := strconv.ParseInt(text, 10, 64)
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func process(path string) {
	inFile, _ := os.Open(path)
	defer inFile.Close()
	scanner := bufio.NewScanner(inFile)
	scanner.Split(bufio.ScanLines)

	//scan the first case.
	scanner.Scan()
	numCase := int(readInt(scanner.Text()))

	fmt.Println("num of cases:", numCase)

	//output to file
	f, err := os.Create(path + ".out")
	if err != nil {
		fmt.Println(err)
	}

	//---question specific area
	for caseNum := 1; caseNum <= numCase; caseNum++ {
		//scan for size of matrix
		scanner.Scan()
		sizeMatrix := readInt(scanner.Text())

		matA := make([]int, sizeMatrix)
		scanner.Scan()
		strA := strings.Fields(scanner.Text())
		for key, val := range strA {
			matA[key], _ = strconv.Atoi(val)
		}
		//fmt.Println(matA)

		matB := make([]int, sizeMatrix)
		scanner.Scan()
		strB := strings.Fields(scanner.Text())
		for key, val := range strB {
			matB[key], _ = strconv.Atoi(val)
		}
		//fmt.Println(matB)

		//solve

		//sort matA descending, sort matB ascending:
		sort.Ints(matA)
		sort.Sort(sort.Reverse(sort.IntSlice(matB)))
		answer := 0
		for i := 0; i < len(matA); i++ {
			answer += matA[i] * matB[i]
		}

		outstr := fmt.Sprintf("Case #%v: %v\n", caseNum, answer)

		n, err := io.WriteString(f, outstr)
		if err != nil {
			fmt.Println(n, err)
		}

	}

	//close the output
	f.Close()

}
