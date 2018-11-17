def move_disk(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def towers_of_hanoi(n, start, end):
	if n > 0:
		tmp = 6 - start - end
		towers_of_hanoi(n-1, start, tmp)
		move_disk(start, end)
		towers_of_hanoi(n-1, tmp, end) 