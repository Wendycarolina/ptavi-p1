#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

class Calculadora():
	def __init__(self,numero1,numero2)
		self.numero1 = numero1
		self.numero2 = numero2

	def suma(self,sumando1, sumando2):
		return sumando1 + sumando2 

	def resta(self,numero1, numero2):
		return numero1 - numero2

if __name__ == "__main__":
	x = Calculadora()
	try:
	
		x.numero1 = int(sys.argv[1])
		operacion = str(sys.argv[2])
		x.numero2 = int(sys.argv[3])
