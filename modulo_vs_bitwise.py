import time
import dis

def is_even_modulo(num):
    return num % 2 == 0

def is_even_bitwise(num):
    return num & 1 == 0


runs = 5
percentages = []

for _ in range(runs):
    start_time = time.time()
    for num in range(1, 30000000):
        is_even_bitwise(num)
    bitwise_duration = time.time() - start_time
    
    start_time = time.time()
    for num in range(1, 30000000):
        is_even_modulo(num)
    modulo_duration = time.time() - start_time

    print(f"Bitwise AND method took: {bitwise_duration:.3f} seconds")
    print(f"Modulo method took: {modulo_duration:.3f} seconds")

    if bitwise_duration < modulo_duration:
        time_difference = modulo_duration - bitwise_duration
        percentage_faster = (time_difference / modulo_duration) * 100
        print(f"Bitwise AND is {percentage_faster:.2f}% faster than modulo.\n")
    else:
        time_difference = bitwise_duration - modulo_duration
        percentage_faster = (time_difference / bitwise_duration) * 100
        print(f"Modulo is {percentage_faster:.2f}% faster than Bitwise AND.\n")
    
    percentages.append(percentage_faster)

average_percentage_faster = sum(percentages) / len(percentages)
print(f"\nAverage performance difference over {runs} runs: {average_percentage_faster:.2f}%")






from numba import njit
import dis

@njit
def is_even_bitwise(num):
    return num & 1 == 0

@njit
def is_even_modulo(num):
    return num % 2 == 0

is_even_bitwise(500)
is_even_modulo(500)

def prettify_assembly(assembly_code):
    if isinstance(assembly_code, dict):
        assembly_code = next(iter(assembly_code.values()))
    lines = assembly_code.splitlines()

    prettified_lines = []

    for line in lines:
        if line.strip() and not line.startswith('\t'):
            prettified_lines.append(line)
        elif line.strip():
            prettified_lines.append('\t' + line.strip())
        else:
            prettified_lines.append('')

    return '\n'.join(prettified_lines)

bitwise_assembly = is_even_bitwise.inspect_asm()
modulo_assembly = is_even_modulo.inspect_asm()

"""
# Uncomment if you would like to view the full raw assembly

print("Assembly for is_even_bitwise:")
print(prettify_assembly(bitwise_assembly))

print("\nAssembly for is_even_modulo:")
print(prettify_assembly(modulo_assembly))
"""


"""
#Uncomment if you would like to view the opcodes

print("Python 3.11 Opcodes for is_even_bitwise:")
dis.dis(is_even_bitwise)

print("Python 3.11 Opcodes for is_even_modulo:")
dis.dis(is_even_modulo)
"""
