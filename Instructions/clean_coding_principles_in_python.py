CLEAN_CODING_PRIN_PY = '''
# Clean Coding Principles in Python

## 1. Meaningful Names
- **Use descriptive and unambiguous names**:
  - Bad: `d`, `tmp`
  - Good: `days`, `temporary_file`
  
- **Use pronounceable and searchable names**:
  - Bad: `dbldstnce`
  - Good: `double_distance`
  
- **Avoid single letter names** (except for counters in loops):
  - Bad: `i`
  - Good: `index`, `count`
  
- **Use snake_case for function and variable names**:
  - Example: `calculate_area()`, `total_count`

## 2. Functions Should Be Small
- **Keep functions short**: Aim for functions that do one thing and do it well.
- **Functions should have a clear purpose**: Each function should have a single responsibility.
- **Limit function arguments**: Ideally, 3 or fewer arguments. Use data structures like dictionaries for more complex inputs.

## 3. Avoid Repetition (DRY Principle)
- **Do not repeat yourself**:
  - If you find yourself copying code or logic, extract it into a function or class.
  - Example:
    ```python
    # Bad
    area1 = length1 * width1
    area2 = length2 * width2
    
    # Good
    def calculate_area(length, width):
        return length * width
    ```

## 4. Use Comments Sparingly and Wisely
- **Only comment what the code cannot tell**:
  - Bad: `# Increment i by 1`
  - Good: `# Retry connection in case of temporary network failure`
  
- **Prefer readable code over excessive comments**: Code should explain itself with clear variable names and logic.
- **Use docstrings for functions**: Describe the purpose of the function and its arguments.
  ```python
  def calculate_area(length, width):
    """
      Calculate the area of a rectangle.
      
      :param length: Length of the rectangle
      :param width: Width of the rectangle
      :return: Area of the rectangle
    """
      return length * width
      
  ```
      
## 5. Error Handling
**Handle exceptions explicitly**:

Use `try-except` blocks where necessary, but avoid silent failure.

```python
try:
    result = divide(a, b)
except ZeroDivisionError:
    print("Error: Division by zero.")
    
```
      
      
## 6. Use Type Hinting in Python
**Use proper typing hint in every function**:

Use `typing` module for hints.

```python
from typing import List, Tuple, Dict, Union, Optional

# Typing for a function that takes a list of integers and returns a string

def process_numbers(numbers: List[int]) -> str:
    total: int = sum(numbers)
    return f"The total sum is {total}"

# Typing for a function that returns a tuple of string and integer
def get_user_info(user_id: int) -> Tuple[str, int]:
    user_name: str = "Harshit"
    age: int = 25
    return (user_name, age)

# Typing for a function that can return either an integer or None
def find_item_index(items: List[str], search_item: str) -> Optional[int]:
    try:
        return items.index(search_item)
    except ValueError:
        return None

# Typing for a function that accepts a dictionary and returns a string
def describe_person(details: Dict[str, Union[str, int]]) -> str:
    name: str = details.get("name", "Unknown")
    age: int = details.get("age", 0)
    return f"Name: {name}, Age: {age}"

```

'''
