import numpy as np
from os import get_terminal_size
from time import sleep


class ProgressBar:
	''' Progress bar utility.'''

	def __init__(self, n_iter, width=None, char="=", brackets="[]",
					text="", perc_float=2):
		''' To be called before the loop.'''

		if width is None or get_terminal_size().columns < width:
			self.width = get_terminal_size().columns - 10
		else:
			self.width = width
		self.width += 1

		if isinstance(n_iter, int) or len(n_iter)==1:
			self.nested = False
			if isinstance(n_iter, int):
				self.n_iter = n_iter
				self.grad = width / n_iter
			else:
				self.n_iter = n_iter[0]
				self.grad = width / n_iter[0]
			self.n_bar = 1

		else:
			self.nested = True
			self.grad = [self.width/n_it for n_it in n_iter]
			self.n_bar = len(n_iter)
			self.n_iter = n_iter

		self.char = char
		self.text = text
		self.perc_float = perc_float
		self.start_brkt, self.end_brkt = brackets

	def update(self, *indices):
		''' Called at each iteration.
			i for the iteration number.
		'''
		if not self.nested:
			index = indices[0]
			part1 = int(self.grad*index)
			part2 = self.width - part1 - 1

			perc = 100*index/self.n_iter
			if self.perc_float > 0:
				perc = np.around(perc, self.perc_float)
			else:
				perc = int(perc)

			print(self.text + " " + self.start_brkt + part1 * self.char + part2*' ' + self.end_brkt + " {}% ".format(perc) , end="\r")

		else:
			string = ""
			for i in range(self.n_bar):
				index = indices[i]
				part1 = int(self.grad[i]*index)
				part2 = self.width - part1 - 1

				perc = 100*indices[i]/self.n_iter[i]
				if self.perc_float > 0:
					perc = np.around(perc, self.perc_float)
				else:
					perc = int(perc)

				string += self.text + " " + self.start_brkt + part1 * self.char + part2*' ' + self.end_brkt + " {}% ".format(perc) + '\n'

			print(string, end='\r')
			print("\033[F"*(self.n_bar+1))


	def end(self, text="Done!"):
		print("\033[F"*(self.n_bar+1))
		print(text + " " + self.width * self.char + self.end_brkt + " 100% ", end="\n")


if __name__ == "__main__":

	n = 10
	m = 100
	p = 10000
	pbar = ProgressBar((n,m,p), width=50, perc_float=2, 
		text="Loading.", char="=", brackets="[]")
	for i in range(n):
		for j in range(m):
			for k in range(p):
				pbar.update(i, j, k)
	pbar.end()

