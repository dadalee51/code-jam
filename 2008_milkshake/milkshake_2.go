package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	//	"sort"
	"strconv"
	"strings"
)

func main() {
	//process("test_in")
	process("small_in")
	//process("large_in")
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
		fmt.Println("==================", caseNum, "================")
		//N flavr
		scanner.Scan()
		flavr, _ := strconv.Atoi(scanner.Text())
		//M custmr
		scanner.Scan()
		custmr, _ := strconv.Atoi(scanner.Text())
		answer := ""
		matP := make([]int, flavr)
		for k, _ := range matP {
			matP[k] = -1
		}
		sat := 0
		fmt.Println("there are ", flavr, " flavors and ", custmr, " customers.")
		for cuNum := 0; cuNum < custmr; cuNum++ {

			scanner.Scan()
			strA := strings.Fields(scanner.Text())
			numFla, _ := strconv.Atoi(strA[0])

			fmt.Println("matP:", matP)
			satFlag := false
			for i := 0; i < numFla; i++ {
				tflav, _ := strconv.Atoi(strA[1+2*i])

				tmalt, _ := strconv.Atoi(strA[2+2*i])
				fmt.Println("tflav is: ", tflav, " tmalt:", tmalt)
				if matP[tflav-1] == -1 {
					matP[tflav-1] = tmalt
					satFlag = true

				} else if matP[tflav-1] == tmalt {
					satFlag = true

				}

			}
			if satFlag {
				sat++
				fmt.Println("this customer is satisfied.")
			} else {
				fmt.Println("this customer is NOT satisfied.")
			}
			fmt.Println("matP_after:", matP, ", sat is:", sat)
		}

		if sat == custmr && sat != 0 {
			for k, v := range matP {
				if v == -1 {
					answer += "0"
				} else {
					answer += strconv.Itoa(v)
				}
				if k < len(matP)-1 {
					answer += " "
				}
			}
			fmt.Println("sat and custmr matched.")
		} else {
			answer = "IMPOSSIBLE"
			fmt.Println("sat and custmr not matched.")
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
