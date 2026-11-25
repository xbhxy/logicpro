#QUESTION16

def check_pattern(arr):
    diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False

    return True

arr = [2, 4, 6, 8, 10, 12]

print(check_pattern(arr))


#QUESTION 17

arr = [2, 1, 5, 1, 3, 2]
k = 3

max_sum = 0

for i in range(len(arr) - k + 1):
    window_sum = sum(arr[i:i+k])
    print(window_sum)

    max_sum = max(max_sum, window_sum)

print("Maximum Sum:", max_sum)


#QUESTION18

arr = [1, 2, 4, 6, 8, 9]
target = 10

left = 0
right = len(arr) - 1

while left < right:
    total = arr[left] + arr[right]

    if total == target:
        print(arr[left], arr[right])
        break
    elif total < target:
        left += 1
    else:
        right -= 1


#QUESTION19

def frequency(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    print("Frequency:", freq)

    most_frequent = max(freq, key=freq.get)

    print("Most Frequent Number:", most_frequent)
    print("Frequency:", freq[most_frequent])


arr = [4, 2, 4, 3, 2, 4, 1]

frequency(arr)


#QUESTION20

arr = [3, 1, 4, 2, 5, 1, 6]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)

print("Maximum Window Sum:", max_sum)