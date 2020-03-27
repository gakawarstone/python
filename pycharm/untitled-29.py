import requests
cnt = 0

r = requests.get(input())
print(r)

for line in r.text.splitlines():
    cnt += 1

print(cnt)
