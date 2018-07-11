Python Better to Know

- 内建函数
  
  map 
  
```python
  #map(function_to_apply, list_of_inputs)
  items = [1, 2, 3, 4, 5]
  squared = list(map(lambda x: x**2, items))
  #squared = [1, 4, 9, 16, 25]
  
  #map 高端用法可以传function
  def multiply(x):
    return (x*x)
  def add(x):
      return (x+x)

  funcs = [multiply, add]
  for i in range(5):
      value = list(map(lambda x: x(i), funcs))
      print(value)

  # Output:
  # [0, 0]
  # [1, 2]
  # [4, 4]
  # [9, 6]
  # [16, 8]
  
```
  
  filter

```python
  #python 的filter 用法跟js的差不多
  number_list = range(-5, 5)
  less_than_zero = list(filter(lambda x: x < 0, number_list))

  #less_than_zero = [-5, -4, -3, -2, -1]
```
  
  sorted
  
  zip
  
  all
  
  any
  
  enumerate

- numpy 

  
