# pylint: disable=invalid-name
# pylint: disable=too-many-locals
"""
Módulo para conversión de bases (Binario y Hexadecimal).
Maneja números negativos (complemento a dos) y datos inválidos.
Actividad 4.2 - Ejercicio 2.
"""

import sys
import time
import os


def to_binary(n):
    """Convierte a binario manual. 10-bit complemento a 2 para negativos."""
    if n >= 0:
        if n == 0:
            return "0"
        res = ""
        num = n
        while num > 0:
            res = str(num % 2) + res
            num //= 2
        return res
    # Caso negativo: Complemento a dos en 10 bits (2^10 = 1024)
    num = 1024 + n
    res = ""
    for _ in range(10):
        res = str(num % 2) + res
        num //= 2
    return res


def to_hexadecimal(n):
    """Convierte a hex manual. 10-digit complemento a 2 para negativos."""
    hex_chars = "0123456789ABCDEF"
    if n >= 0:
        if n == 0:
            return "0"
        res = ""
        num = n
        while num > 0:
            res = hex_chars[num % 16] + res
            num //= 16
        return res
    # Caso negativo: Complemento a dos en 10 dígitos hex (16^10)
    num = (16**10) + n
    res = ""
    for _ in range(10):
        res = hex_chars[num % 16] + res
        num //= 16
    return res


def main():
    """Función principal para leer archivo y convertir números."""
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        return

    input_file = sys.argv[1]
    base_name = os.path.basename(input_file).split('.')[0]
    output_filename = f"ConvertionResults{base_name}.txt"

    results = []
    item_count = 0
    try:
        with open(input_file, 'r', encoding='utf-8') as f_ptr:
            for line in f_ptr:
                parts = line.split()
                if not parts:
                    continue
                item_count += 1

                # El valor a convertir es siempre el último de la fila
                val_str = parts[-1]

                try:
                    num = int(val_str)
                    b_str = to_binary(num)
                    h_str = to_hexadecimal(num)
                except ValueError:
                    b_str = "#VALUE!"
                    h_str = "#VALUE!"

                # Guardamos: ITEM, todas las partes originales, BIN, HEX
                results.append((item_count, parts, b_str, h_str))

    except FileNotFoundError:
        print("Error: File not found.")
        return

    elapsed_time = time.time() - start_time
    header = f"ITEM\t{base_name}\tBIN\tHEX"

    with open(output_filename, "w", encoding='utf-8') as f_out:
        print(header)
        f_out.write(header + "\n")
        for res in results:
            # Unimos las partes originales con tabuladores
            orig_content = "\t".join(res[1])
            row = f"{res[0]}\t{orig_content}\t{res[2]}\t{res[3]}"
            print(row)
            f_out.write(row + "\n")

        time_msg = f"Execution Time: {elapsed_time:.6f}s"
        print(time_msg)
        f_out.write(time_msg + "\n")


if __name__ == "__main__":
    main()
