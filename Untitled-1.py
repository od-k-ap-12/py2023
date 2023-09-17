# input
# Упражнение 1: Ввод/Вывод 
# Напишите программу на Python, которая запрашивает у пользователя ввести размеры прямоугольной 
# комнаты (длину, ширину и высоту), а затем вычисляет и выводит объем комнаты. 
# Кроме того, на основе объема программа должна определить, является ли это небольшой, средней 
# или большой комнатой, и вывести соответствующее сообщение. Какую комнату считать большой, а какую 
# маленькой, можете решить самостоятельно. Также следует добавить проверку на неправильно введенные 
# данные.

# Упражнение 2: Условия и Циклы 
# Напишите программу на Python, которая генерирует последовательность Фибоначчи. Попросите 
# пользователя ввести длину последовательности, которую он хочет сгенерировать. З
# атем, используя цикл, генерируйте и выводите последовательность Фибоначчи до указанной длины. 
# Например, если пользователь вводит 7, программа должна сгенерировать и вывести первые 7 
# чисел в последовательности Фибоначчи: 0, 1, 1, 2, 3, 5, 8. Решение должно быть итеративным, 
# НЕ рекурсивным.

# Упражнение 3: Списки
# Измените программу из задания 2 таким образом, чтобы найденные числа добавлялись в список. Выведите 
# получившийся список на экран.

# Упражнение 4: Списки и Условия 
# Добавьте в программу из задания 3 подсчет количества четных и нечетных чисел в получившемся списке.
# Выведите процентное соотношение четных и нечетных чисел.

#Упражнение 1
small_room_volume=20
medium_room_volume=50
print("Enter length, width and height:")
length = float(input())
width = float(input())
height = float(input())
if length>0 and width>0 and height>0:
    volume = length * width * height
    if volume <= 20:
        print("Volume: " + str(volume) + ". This is a small room.")
    elif volume <=50 and volume>20:
        print("Volume: " + str(volume) + ". This is a medium room.")
    else:
        print("Volume: " + str(volume) + ". This is a large room.")
else:
    print("Error")


#Упражнения 2,3,4
odd=0
even=0
firstnum=0
secondnum=1
currentnum=0
fibonacci_numbers=[]
print("Enter how many Fibonacci numbers you want:")
it=int(input())
i=0
for number in range (it):
    if i==0:
        print(0)
        fibonacci_numbers.append(0)
        even+=1
        i+=1
    elif i==1:
        print(1)
        fibonacci_numbers.append(1)
        odd+=1
        i+=1
    else:
        currentnum=firstnum+secondnum
        print(currentnum)
        fibonacci_numbers.append(currentnum)
        if currentnum % 2 == 0:
            even+=1
        else:
            odd+=1
        firstnum=secondnum
        secondnum=currentnum
print("list:")
print(fibonacci_numbers)
evenpercentage=even*100/it
oddpercentage=100-evenpercentage
print("even: "+str(evenpercentage)+"%")
print("odd: "+str(oddpercentage)+"%")
    
