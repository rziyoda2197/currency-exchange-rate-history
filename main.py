from multiprocessing import Pool
import time

def heavy_task(n):
    # Bu vazifani bajarish uchun vaqt
    time.sleep(n)
    return n * n

if __name__ == "__main__":
    # Process Pool yaratish
    pool = Pool(processes=4)

    # Heavy tasklarni parallel ishlab chiqarish
    results = pool.map(heavy_task, [1, 2, 3, 4, 5])

    # Natija chiqarish
    print(results)
```

```python
from multiprocessing import Pool
import time

def heavy_task(n):
    # Bu vazifani bajarish uchun vaqt
    time.sleep(n)
    return n * n

if __name__ == "__main__":
    # Process Pool yaratish
    pool = Pool(processes=4)

    # Heavy tasklarni parallel ishlab chiqarish
    results = pool.map(heavy_task, [1, 2, 3, 4, 5])

    # Natija chiqarish
    print(results)
