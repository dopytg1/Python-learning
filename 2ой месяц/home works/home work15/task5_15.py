nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

countTo = 9
count = 1

for i in range(2):
    for i in range(countTo):
        print("*")


for i in range(countTo):
    nums2 = []
    for j in range(countTo):
        nums2.append(count * nums[j])
        if nums2[j] >= 10:
            nums2[j] = str(nums2[j])
        else:
            nums2[j] = str(nums2[j]) + " "
    
    print("  ".join(nums2))
    count += 1
    nums2 = []