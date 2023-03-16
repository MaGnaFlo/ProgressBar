import numpy as np
from os import get_terminal_size


class ProgressBar:
	''' Progress bar utility.'''

	def __init__(self, n_iter, width=None, char="#", brackets="[]",
					text="", perc_float=2):

		''' To be called before the loop.'''
		if width is None or get_terminal_size().columns < width:
			self.width = get_terminal_size().columns - 10
		else:
			self.width = width
		self.width += 1

		self.char = char
		self.grad = self.width/n_iter
		self.n_iter = n_iter
		self.text = text
		self.perc_float = perc_float
		self.start_brkt, self.end_brkt = brackets

		print(text + " " + self.start_brkt + (self.width+1)*' ' + self.end_brkt, end="\r")

	def update(self, i):
		''' Called at each iteration.
			i for the iteration number.
		'''
		part1 = int(self.grad*i)
		part2 = self.width - part1 - 1
		perc = 100*(i+1)/self.n_iter
		if self.perc_float > 0:
			perc = np.around(perc, self.perc_float)
		else:
			perc = int(perc)
		print(self.text + " " + self.start_brkt + part1 * self.char + part2*' ' + self.end_brkt + " {}% ".format(perc) , end="\r")

	def end(self, text=""):
		print()
		print(text)


if __name__ == "__main__":

	n = 1000000
	pbar = ProgressBar(n, width=30, perc_float=2, 
		text="Loading.", char="=", brackets="[]")
	for i in range(n):
		pbar.update(i)
	pbar.end()

