# comprehension lists
# a
print("a")
numbers_95_105: list[int] = [i for i in range(95, 106)]
print(numbers_95_105)

# b
print("b")
even_numbers: list[int] = [i for i in range(10, 21, 2)]
print(even_numbers)

# c
print("c")
true_or_false: list[int] = [i > 2 for i in range(6)]
print(true_or_false)

# d
print("d")
import random

random_numbers: list[int] = [random.randint(1, 100) for _ in range(11)]
print(random_numbers)

# e
print("e")
above_50: list[int] = [i for i in random_numbers if i > 50]
print(above_50)

# f
print("f")
rand_num: list[int] = [random.randint(50, 100) for i in range(11) if random.randint(1, 100) > 50]
print(rand_num)

# g
print("g")
sentence = input("Enter a sentence: ")
letters: list[str] = [letter for letter in sentence if letter != 't' and letter != ' ']
print(letters)

# h
print("h")
numbers_10_99: list[int] = [random.randint(10, 99) for i in range(11)]
print(numbers_10_99)
numbers_10_99_2: list[int] = [i % 10 for i in numbers_10_99]
print(numbers_10_99_2)
