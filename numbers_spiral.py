max_num = int(input()) #вводится число, для которого будем строить матрицу
m = max_num
arr = [ [0]*m for i in range(max_num) ] #строю пустую матрицу из нулей, которая будет заполняться числами по спирали
counter = max_num//2 #число кругов/"проходов" (верх-право-низ-лево) для заполнения матрицы
push_number = 1 #заполнение матрицы начинается с цифры 1
correct_it = 0 #переменная, с помощью которой будут корректироваться координаты (i,j)

while counter > 0:
        #наполнение верхнего ряда  
    for j in range (correct_it, max_num-correct_it-1): 
        arr[correct_it][j] = push_number
        push_number += 1
    
        #наполнение правого ряда
    for i in range(correct_it,max_num-correct_it-1):
        arr[i][-correct_it-1] = push_number
        push_number += 1

        #наполнение нижнего ряда
    for j in range (correct_it, max_num-correct_it-1):
        arr[-correct_it-1][-j-1] = push_number
        push_number += 1

    
        #наполнение левого ряда
    for i in range(correct_it,max_num-correct_it-1):
        arr[-i-1][correct_it] = push_number
        push_number += 1

        
    counter -= 1 #в конце "прохода" уменьшаем counter, чтобы проверки не повторялись бесконечно
    correct_it += 1 #плюсуем корректирующую переменную, которая позволяет в каждом "проходе" переходить на следующий круг
    
#если число нечётное, то последний нуль в середине матрицы принимает значение последнего недостающего числа
if max_num%2 == 1:
    arr[correct_it][correct_it] = push_number
    
#вывод для проверки
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()