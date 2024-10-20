# Python Performance Comparison: Modulo vs Bitwise AND for Evenness Checking

This repository contains a Python script that compares the performance of two methods for checking the evenness of numbers: using modulo (`%`) and bitwise AND (`&`). The goal is to measure the performance difference between these operations across different environments (Linux and Windows) and Python versions (3.10 vs 3.11+), and investigate how opcode differences affect performance.

## Motivation

A LinkedIn post suggested that modulo operations in Python were faster than bitwise AND for checking evenness, contrary to the common assumption that bitwise operations are faster. This script runs performance tests to determine which method is more efficient and investigates how Python's handling of opcodes across different versions affects the outcome.

## Code Overview

The script defines two methods for evenness checking:
- `is_even_modulo(num)`: Returns `True` if `num % 2 == 0`.
- `is_even_bitwise(num)`: Returns `True` if `num & 1 == 0`.

It runs multiple iterations of performance tests on both methods and calculates the percentage difference in execution time. The script adapts based on whether modulo or bitwise AND is faster during each run.

### Example of Defined Functions:

```python
def is_even_modulo(num):
    return num % 2 == 0

def is_even_bitwise(num):
    return num & 1 == 0
```

## Test Execution
The script runs both methods 30 million times in each test run, comparing their execution time and reporting which method is faster, along with the percentage difference.

### Sample Output

```Linux Environment
Bitwise AND method took: 1.523 seconds
Modulo method took: 1.620 seconds
Bitwise AND is 5.96% faster than modulo.

Bitwise AND method took: 1.504 seconds
Modulo method took: 1.586 seconds
Bitwise AND is 5.17% faster than modulo.

...

Average performance difference over 5 runs: 5.36%
```

## Disassembly & Opcode Investigation
The script further explores how Python compiles the two methods into bytecode and the impact of different Python versions (3.10 vs 3.11+) on performance. By disassembling the functions and viewing the opcodes, we observe differences in how binary operators are handled:

### For Python 3.10:

- Bitwise AND: `BINARY_AND`
- Modulo: `BINARY_MODULO`

### For Python 3.11+:

Both methods are handled through BINARY_OP with different arguments for AND (1) and MOD (6), reflecting changes in Python's internal handling of these operations.

## Requirements
- Python 3.10 or later
- time module (part of Python standard library)

## Running the Script
1. Clone the repository:
```
git clone https://github.com/KevinRouz/modulo-vs-bitwise.git

cd modulo-vs-bitwise
```
2. Run the script:
```
python modulo_vs_bitwise.py
```
3. View the output to see which operation is faster and by what percentage.
