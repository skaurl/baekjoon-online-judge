a, p = input().split()

check = set({a})
nums = {a:0}
idx = 0

while True:
    a=str(sum(int(c)**int(p)for c in a))
    if a in check:
        break
    check.add(a)
    idx +=1
    nums[a] = idx

print(nums[a])