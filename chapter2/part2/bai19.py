from collections import Counter
import sys

fn = input().strip() or "romeo.txt"
try:
    with open(fn, encoding="utf-8") as f:
        cnt = Counter()
        for line in f:
            for w in line.split():
                cnt[w] += 1
    items = sorted(((v, k) for k, v in cnt.items()), reverse=True)
    for v, k in items[:10]:
        print(k, v)
except Exception as e:
    print("Không đọc được file")
