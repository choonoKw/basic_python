Certainly! Below is a Python function that checks if a directory named "my_dir" exists, and if not, creates it.

```python
import os

def check_and_create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")
    else:
        print(f"Directory '{directory_name}' already exists.")

# Usage
check_and_create_directory("my_dir")
```

This function uses the `os` module to check for the existence of the directory and creates it if it does not exist.
