# Profiling

Profiling is essential for assessing how different parts of a program execute and gathering crucial performance data. It plays a vital role in debugging, pinpointing bottlenecks, optimizing code, and scaling application performance. This analysis identifies common issues such as out-of-bound memory, segmentation faults, bus errors, and runtime overhead, enabling effective troubleshooting and improvement strategies.

In research contexts, where code often performs complex or resource-intensive tasks, profiling helps identify which parts of the code consume significant compute and memory resources. This insight guides optimizations aimed at reducing execution times and enhancing the overall efficiency of the program.

## Profiling Python Codes

Three common profiling techniques used in analyzing Python codes are discussed briefly in this section.

1. Time Profiling
2. Memory Profling
3. CPU Profling

### Time Profiling

For researchers, optimizing code runtime is essential, highlighting the significance of profiling code runtime. This process aids in accurately estimating the necessary computational resources like CPU and memory for successful simulation execution.

1. Line Profiling
Line profiling is a powerful tool that provides detailed insights into the execution time of each line of code. Unlike profiling an entire program, which might miss small but crucial performance issues, line profiling meticulously examines how much time each line takes to execute. This method is particularly beneficial for pinpointing specific code segments or operations that may be contributing to slower overall performance. However, this involves modifying the exisiting code. Inorder to avoid more manual changes, you can use the `kernprof` command line utility with `line profiler`. This tool allows you to profile Python scripts without needing to add profiling code directly into the script itself.

Example1:

The following example shows profiling a input python code that calculates num_array.

```bash
import sys
import numpy as np

# Verify if correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python python_script_new.py <start> <end>")
    sys.exit(1)

# Passing start and end values from command-line arguments
start = int(sys.argv[1])
end = int(sys.argv[2])

@profile
def create_array(start, end):
    # Create an array from start to end using numpy
    return np.arange(start, end)

@profile
def compute_sum(input_array):
    # Perform addition on the array elements using numpy's sum function
    return np.sum(input_array)

# Main code execution
input_array = create_array(start, end)
sum_result = compute_sum(input_array)

# Print Input Range and Sum
print("Input Range: {} to {}, Sum: {}".format(start, end, sum_result))
```

```bash
$ kernprof -l -v python_script.py 1 1000

Input Range: 1 to 1000, Sum: 499500
Wrote profile results to python_script.py.lprof
Timer unit: 1e-06 s

Total time: 2.106e-05 s
File: python_script.py
Function: create_array at line 13

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    13                                           @profile
    14                                           def create_array(start, end):
    15                                               # Create an array from start to end using numpy
    16         1         21.1     21.1    100.0      return np.arange(start, end)

Total time: 5.1727e-05 s
File: python_script.py
Function: compute_sum at line 18

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    18                                           @profile
    19                                           def compute_sum(input_array):
    20                                               # Perform addition on the array elements using numpy's sum function
    21         1         51.7     51.7    100.0      return np.sum(input_array)
```

2. Function Profiling
tracing each function call to generate a list detailing the frequency of function calls and the average time taken for each call. This helps identify which functions are called most often and their respective performance characteristics.
