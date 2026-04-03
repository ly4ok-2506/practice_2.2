import psutil

print("=" * 30)
print("СИСТЕМНЫЙ МОНИТОР")
print("=" * 30)

cpu = psutil.cpu_percent(interval=1)
print(f"Загрузка CPU: {cpu}%")

ram = psutil.virtual_memory()
print(f"Использовано RAM: {ram.percent}%")

disk = psutil.disk_usage('/')
print(f"Загруженность диска: {disk.percent}%")