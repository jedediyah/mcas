# mcas
Grabs Massachusetts MCAS data from the Department Of Ed.  

To get data on the percent of students in the categories of
1. Advanced
2. Proficient
3. Needs Improvement
4. Warning / Fail 

Use, for example
```python
from mcas import *
school_data, state_data, diff_data = get_subject(2014,'01970505','MAT')
print school_data
print state_data
print diff_data
```
