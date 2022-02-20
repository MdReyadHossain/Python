def sort(s_list):
    for i in range(0, len(s_list)-1):
        cnt = 0
        for j in range(0, len(s_list)-i-1):
            if s_list[j] > s_list[j+1]:
                s_list[j], s_list[j+1] = s_list[j+1], s_list[j]
                cnt += 1
        
        if cnt == 0:
            break

    print("\nSorted List =", s_list)

list = [5, 3, 9, 1, 7]
print("The List =", list)
sort(list)