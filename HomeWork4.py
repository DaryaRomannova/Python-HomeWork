#Скопировать из файла F1 в файл F2 все строки, которые содержат только одно слово. Найти самое короткое слово в файле F2.
import shutil
min = 1
with open(r'D:f1.txt', 'r') as file:
    for line in file:
      f=line.split(" ")
      if len(f) == 1:
          with open(r'D:f2.txt','a') as file2:
              file2.write(line)
              min = (len(list(line)))
max = 1
i = 0
k = 0
with open(r'D:f2.txt' , 'r') as file2:
    for line in file2:
        i +=1
        max = (len(list(line)))
        if max < min:
            min = max
            k = i
i = 0
print("Самое короткое слово находится в строке : ", k)
with open(r'D:f2.txt' , 'r') as file2:
    for line in file2:
        i +=1
        if i == k:
            print("Это слово : ",line)











