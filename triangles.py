#!/usr/bin/env python3

#  ------------------------------------------------------------>
#  Title: Triangles
#
#  Created by: Johnathan Moore
#
#  Created on: Aug 16, 2022
#
#  Purpose: To identify a triangles type based on user's input
#  of values for lengths of sides
#
#  ------------------------------------------------------------>


a = int(input('Side a?: '))
b = int(input('Side b?: '))
c = int(input('Side c?: '))


class Triangle:

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c


	def equilateral(self):

		if self.a == self.b & self.b == self.c & self.a == self.c:
			print('Is Equilateral')
		else:
			print('\x1b[31mIs NOT Equilateral\x1b[0m')


	def is_triangle(self):

		if self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
			print('Is Triangle')
		else:
			print('\x1b[31mIs NOT A Triangle')


	def right_triangle(self):

		side_list = [self.a, self.b, self.c]
		sorted_side_list = sorted(side_list)
		c_sq = sorted_side_list[-1]
		b_sq = sorted_side_list[1]
		a_sq = sorted_side_list[0]

		if a_sq ** 2 + b_sq ** 2 == c_sq ** 2:
			print('Is Special Right')
		else: 
			print('\x1b[31mIs NOT Special Right\x1b[0m')


	def isoscolese(self):

		if  self.a == self.b or self.a == self.c or self.b == self.c:
			print('Is isoscolese')
		else:
			print('\x1b[31mIs NOT isoscolese\x1b[0m')


triangle1 = Triangle(a, b, c)

triangle1.is_triangle()
triangle1.equilateral()
triangle1.right_triangle()
triangle1.isoscolese()
