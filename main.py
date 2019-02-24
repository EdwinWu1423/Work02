from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4, 4)
print_matrix (matrix)
print('\n')
ident(matrix)
print_matrix(matrix)
print('\n')
m1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
m2 = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
print_matrix(m1)
print('\n')
print_matrix(m2)
print('\n')
print_matrix(matrix_mult(m1, m2))
print('\n')

image = new_matrix()
add_edge(image, 0, 0, 0, 0, 250, 0)
add_edge(image, 0, 250, 0, 250, 250, 0)
add_edge(image, 250, 250, 0, 250, 0, 0)
add_edge(image, 250, 0, 0, 0, 0, 0)
add_edge(image, 0, 250, 0, 125, 375, 0)
add_edge(image, 125, 375, 0, 250, 250, 0)
add_edge(image, 100, 0, 0, 100, 100, 0)
add_edge(image, 100, 100, 0, 150, 100, 0)
add_edge(image, 150, 100, 0, 150, 0, 0)

draw_lines( image, screen, color )
display(screen)
save_extension(screen, 'img.png')
