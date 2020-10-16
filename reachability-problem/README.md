## Non-deterministic solution for the Reachability Problem
---
__Requirements:__
- __[Numpy](https://numpy.org/)__ - Math library for Python
- __[Networkx](https://networkx.github.io/)__ - Library to display the graphs
---
__Instructions:__
+ To build an instance:
``` bash
make build_instance name={instance_name} size={number_of_vertices}
```

+ To run the non-deterministic algorithm:
``` bash
make solve file={instance_name} start={first_vertex} end={last_vertex}
```
---