## Non-deterministic solution for the 3SAT Problem
---
__Requirements:__
- __[Numpy](https://numpy.org/)__ - Math library for Python
---
__Instructions:__
+ To build an instance:
``` bash
make build_sat_instance c={clauses} v={number_of_variables} name={instance_name}
```

+ To run the non-deterministic algorithm:
``` bash
make 3sat file={instance_name}.txt
```
---