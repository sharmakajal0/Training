def fibonacci(n: int) -> int:
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
	n = int(input())
	print(fibonacci(n))
