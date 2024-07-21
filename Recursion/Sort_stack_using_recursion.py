def sort(stack):
	if len(stack) <= 1:
		return

	top = stack.pop()
	sort(stack)

	insert(stack, top)


def insert(stack, element):
	if not stack:
		stack.append(element)
		return

	if stack[-1] > element:
		top = stack.pop()
		insert(stack, element)
		stack.append(top)
	else:
		stack.append(element)


if __name__ == "__main__":
	stac = [6, 2, 3, 5, 1]
	print(stac)
	sort(stac)

	print(stac)
