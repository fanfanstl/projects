

print("===========简单选择排序=========")
lists = [1, 5, 78, 2, 6, 99, 46]


def select_sort(lists):
    for i in range(len(lists)):
        max = i
        for j in range(i + 1, len(lists)):
            if lists[max] < lists[j]:
                max = j
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
    return lists

print(select_sort(lists))



print("===========冒泡算法=========")


def bubble_sort(lists):
    for i in range(len(lists) - 1):
        for j in range(len(lists) - i - 1):
            if lists[j] < lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists


print(bubble_sort(lists))



print("===========木桶排序===============")
'''
以空间换取时间
'''

def bucket_sort(lists):
    max_value = max(lists)
    tem_lists = ["*"]*(max_value+1)
    for item in lists:
        tem_lists[item] = item
    tem_lists = [i for i in tem_lists if i != "*"]
    return tem_lists

print(bucket_sort(lists))
