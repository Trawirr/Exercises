def pick_peaks(arr):
    pos = []
    peaks = []
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i - 1]:
            j = i+1
            while j < len(arr):
                if arr[j] < arr[i] or j == len(arr):
                    pos.append(i)
                    peaks.append(arr[i])
                    i = j
                    break
                elif arr[j] > arr[i]:
                    i = j
                    break
                j += 1
    return {'pos': pos, 'peaks': peaks}