def calculate_variance(arr):
    total = sum(arr)
    mean = total/len(arr)
    variance = 0
    for num in arr:
        deviation = (num - mean)**2
        variance += deviation
    return variance

def show_stats(arr):
    print('Total Views: ' + str(sum(arr))+ ' mil')
    mean = (sum(arr))/len(arr)
    print('Average Views: ' + str(mean) + ' mil')
    print('Variance: ' + str(calculate_variance(arr)))
    return mean
    
def calculate_covariance(array1, array2):
    n = len(array1)
    mean1 = sum(array1) / n
    mean2 = sum(array2) / n
    covariance = sum((array1[i] - mean1) * (array2[i] - mean2) for i in range(n))
    return covariance

print('Show 1')
show1 = [4, 3, 9, 15, 1, 3, 20, 18, 3, 2.5]
show1_mean = show_stats(show1)
print('----------------')

print('Show 2')
show2 = [4, 3, 4, 3, 2.9, 4, 3, 3.5, 4, 3.9]
show2_mean = show_stats(show2)
print('----------------')

#Viewership
print('Average Viewership Difference: ' + str(show1_mean - show2_mean))
print('----------------')

#Covariance
print('Covarance: ' + str(calculate_covariance(show1, show2)))