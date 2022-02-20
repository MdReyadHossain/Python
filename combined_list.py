# Take two lists from user. From the first list, take all even number and from the second list, take all odd number to put those in another list. And sort this list
def show(list):
    print("\nSorted List =", list)


# sorting the list using bubble sort technique
def sort(s_list):
    for i in range(0, len(s_list)-1):
        cnt = 0
        for j in range(0, len(s_list)-i-1):
            if s_list[j] > s_list[j+1]:
                s_list[j], s_list[j+1] = s_list[j+1], s_list[j]
                cnt += 1
        
        if cnt == 0:
            break

    show(s_list)

# input in the lists
def input_lists():
    for i in range(0, 2*n):
        if i < n:
            print("Enter 1st list of no", i+1, "element : ")
            ele = int(input())
            eve_list.append(ele)
            if ele%2 == 0:
                list.append(ele)
        
        else:
            print("Enter 2nd list of no", i-(n-1), "element : ")
            ele = int(input())
            odd_list.append(ele)
            if ele%2 != 0:
                list.append(ele)

    print("\n1st List =", eve_list)
    print("2nd List =", odd_list)
    print("\nCombined List =", list)
    sort(list)

n = int(input("Enter size of list: "))
odd_list = []
eve_list = []
list = []

input_lists()