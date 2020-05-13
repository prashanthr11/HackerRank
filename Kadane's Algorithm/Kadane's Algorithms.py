s = int(input('Enter size of array :'))

a = list(map(int, input('Enter array Elements :').split()))

def kadane_algorithm(a):
    global_max = current_max = a[0]
    for i in range(1, len(a)):
        current_max = max(a[i], current_max + a[i])
        if(current_max > global_max):
            global_max = current_max
    return global_max


print(kadane_algorithm(a))
