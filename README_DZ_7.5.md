**3.1 Напишите программу для перевода метров в футы (1 фут = 0.3048 метр).**  
```commandline
package main

import "fmt"

func main() {
	fmt.Print("Сколько метров? ")
	var input float64
	fmt.Scanf("%f", &input)
	output := input / 0.3048
	fmt.Printf("Футов будет: %v", output)
}
```
**3.2 Напишите программу, которая найдет наименьший элемент в любом заданном списке.**  
```commandline
package main

import "fmt"

func smallest(list []int) int {
	min := list[0]
	for _, item := range list {
		if item < min {
			min = item
		}
	}
	return min
}
func main() {
	x := []int{48, 96, 86, 68, 57, 82, 63, 70, 37, 34, 83, 27, 19, 97, 9, 17}
	main_min := smallest(x)
	fmt.Println(main_min)
}

```
**3.3 Напишите программу, которая выводит числа от 1 до 100, которые делятся на 3.**  
```commandline
package main

import "fmt"

func main() {
	for i := 3; i < 101; i += 3 {
		fmt.Println(i)
	}
}
```
**4. Создайте тесты для функций из предыдущего задания.**  
> В предыдущем задании только в задаче 3.2 использовалась функция отличная от main. Для неё тест:
```commandline
package main

import "testing"

func testMain(t *testing.T) {
	x := []int{99, 11, 2, 22, 66, 110}
	main_min := smallest(x)
	if main_min != 2 {
		t.Error("Должно быть 2, получилось", main_min)
	}
}

```