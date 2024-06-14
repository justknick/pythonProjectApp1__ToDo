# Remove item 1.45 from seconds.

seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
for i, item in enumerate(seconds):
    print(f"{i + 1}. {item}")