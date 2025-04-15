def DeleteElement(stack, n, k):

    if not stack:
        return

    if k <= 1:
        stack.pop()
        return

    top = stack.pop()
    DeleteElement(stack, n, k - 1)

    stack.append(top)

    return stack


stack = [1, 2, 3, 4, 5]
n = len(stack)

print("Before: ",stack)
print("After: ", DeleteElement(stack, n, n // 2 + 1))
