import numpy as npy

arr1 = npy.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
print(arr1.ndim)
a = npy.array([0,30,45,60,90])
print ('Синус различных углов:')
# Преобразование в радианы, умножение на pi/180
print(npy.sin(a*npy.pi/180))
print('\n')
print('значения косинусов для углов в массиве:')
print(npy.cos(a*npy.pi/180))
print('\n')
print('значения тангенса для заданных углов:')
print(npy.tan(a*npy.pi/180))

#pillow.show()
