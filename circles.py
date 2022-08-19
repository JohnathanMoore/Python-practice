#!/usr/bin/env python3

#  ------------------------------------------------>
#  Title: Circles
#
#  Created by: Johnathan Moore
#
#  Created on: Aug 17, 2022
#
#  Purpose: Evaluate common formulae for circles based on
#  User's input for the value of the radius
#
#  ------------------------------------------------>


import math

user_input = int(input(f'Please enter radius: '))

class Circle:
	def __init__(self, radius):
		self.radius = radius

	def diameter(self):
		d = self.radius * 2
		
		if self.radius <= 0:
			print(f'The length from the center of a circle to the edge of it\'s circumference must be greater than 0.')
		else:
			print(f'A circle with the radius of {self.radius} has a diameter of {d}.')

	def circumference(self):
		c = 2 * math.pi * self.radius
		print(f'The circumference of a circle with the radius of {self.radius} is {c}')

	def area(self):
		a = math.pi * self.radius ** 2
		print(f'The area of a circle with the radius of {self.radius} is {"{:.3f}".format(a)}.')

circle1 = Circle(user_input)
circle1.diameter()
circle1.circumference()
circle1.area()