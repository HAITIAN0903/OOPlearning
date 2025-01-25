for i in range(1,10):
    print(i)

for i in range (1,101):
    result = i+1

print(result)


def sum_of_list(list):
    total = 0
    for num in list:
        total += num
        return total

def count_even(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
        return count
    
def multiplication_table(n):
    for i in range(1,n+1):
        result = i * n
        print(result)

def mutli_table2(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(f"{i * j:4}",end=" ")
        print()

mutli_table2(16)

def find_max(lst):
    max_number=lst[0] #the idea is that you can define a max number at first and then replace it
    for num in lst:
        if num >= max_number:
            max_number = num
    return max_number
   

print(find_max([1,2,3,4,5]))

def is_prime(n):
    if n == 1 or n == 2:
        return True
    for i in (1,n-1):
        if n % i == 0:
            return False
        return True
    
print(is_prime(2))

def fizzbuzz(n):
    for i in (1,n): # i in (1,n) have 1,n; i in range(1,n) have 1.... n-1
        if n % 3 == 0 and n % 5 != 0:
            return 'Fizz'
        if n % 5 == 0 and n % 3 != 0:
            return 'Buzz'
        if n % 3 == 0 and n % 5 == 0:
            return 'FizzBuzz'
print(fizzbuzz(30))

def factorial(n):
    result = 1
    if n < 0:
        return 'non existing'
    if n == 0:
        return 1
    for i in range(1,n):
        result *= i
    return result
print(factorial(15))

def common_elements(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return i
print(common_elements([2,4,6],[1,4,5]))

def count_vowel(s):
    count = 0
    for char in s:
        if char == 'a':
            count +=1
        if char == 'e':
            count +=1
        if char == 'i':
            count +=1
        if char == 'o':
            count +=1
        if char == 'u':
            count +=1
    return count
print( count_vowel('asd'))

# ez version
def count_vowel(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count +=1
    return count


###