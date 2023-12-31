import time
import os
from pathlib import Path

from services.text_compressor_service import TextCompressorService
from utils.file_io import FileIO
from utils.huffman_coder import HuffmanCoder
from utils.lzw_coder import LZWCoder


def run_compression_test(service: TextCompressorService, original_file_path, compressed_file_path, compression_method):
    start_time = time.time()
    encoding_successful = service.encode_file(
        original_file_path, compressed_file_path, compression_method
    )
    end_time = time.time()
    elapsed_time = end_time-start_time
    if encoding_successful:
        file_size_original = os.path.getsize(original_file_path)
        file_size_compressed = os.path.getsize(compressed_file_path)
        print(f"File compressed, elapsed time: {elapsed_time:.2f} seconds")
        print(
            f"Original file size {file_size_original} bytes, compressed size {file_size_compressed}")
        print(
            f"Compression ratio {(file_size_compressed/file_size_original)*100:.2f} %")
    else:
        print("\nFile couldn't be compressed")


def run_decompression_test(service: TextCompressorService, original_file_path, compressed_file_path, decompressed_file_path, compression_method):
    start_time = time.time()
    decoding_successful = service.decode_file(
        compressed_file_path, decompressed_file_path, compression_method
    )
    end_time = time.time()
    elapsed_time = end_time-start_time
    if decoding_successful:
        file_size_original = os.path.getsize(original_file_path)
        file_size_decompressed = os.path.getsize(decompressed_file_path)
        print(f"File decompressed, elapsed time: {elapsed_time:.2f} seconds")
        print(f"Decompressed file size {file_size_decompressed} bytes")
        print(f"Original file size {file_size_original} bytes")
        print(
            f"File sizes equal: {file_size_decompressed == file_size_original}")
    else:
        print("\nFile couldn't be decompressed")

def run_test_set(service: TextCompressorService, method: str):
    method_for_file_path = method.replace(' ', '_')
    print(f'\n## Testing {method} method')

    print('\n# Compress Alice')
    original_file_path = 'src/tests/text_files/pg11_alice_UTF8.txt'
    compressed_file_path = f'src/tests/performance_test_files/alice_{method_for_file_path}_compressed'
    run_compression_test(service, original_file_path,
                        compressed_file_path, method)

    print('\n# Decompress Alice')
    decompressed_file_path = f'src/tests/performance_test_files/alice_{method_for_file_path}_decompressed'
    run_decompression_test(service, original_file_path,
                        compressed_file_path, decompressed_file_path, method)

    print('\n# Compress Frankenstein')
    original_file_path = 'src/tests/text_files/pg84_frankenstein_UTF8.txt'
    compressed_file_path = f'src/tests/performance_test_files/frankenstein_{method_for_file_path}_compressed'
    run_compression_test(service, original_file_path,
                        compressed_file_path, method)

    print('\n# Decompress Frankenstein')
    decompressed_file_path = f'src/tests/performance_test_files/frankenstein_{method_for_file_path}_decompressed'
    run_decompression_test(service, original_file_path,
                        compressed_file_path, decompressed_file_path, method)
    
    print('\n# Compress Pride and Prejudice')
    original_file_path = 'src/tests/text_files/pg1342_pride_and_prejudice.txt'
    compressed_file_path = f'src/tests/performance_test_files/pride_and_prejudice_{method_for_file_path}_compressed'
    run_compression_test(service, original_file_path,
                        compressed_file_path, method)

    print('\n# Decompress Pride and Prejudice')
    decompressed_file_path = f'src/tests/performance_test_files/pride_and_prejudice_{method_for_file_path}_decompressed'
    run_decompression_test(service, original_file_path,
                        compressed_file_path, decompressed_file_path, method)


def main():
    file_io = FileIO()
    huffman_coder = HuffmanCoder()
    lzw_coder = LZWCoder()
    service = TextCompressorService(file_io, huffman_coder, lzw_coder)

    print('\n### Text Compressor, performance tests ###\n')

    print('## Removing old test files')
    test_text_files = [
        'src/tests/performance_test_files/alice_huffman_coding_compressed'
        , 'src/tests/performance_test_files/alice_huffman_coding_decompressed'
        , 'src/tests/performance_test_files/alice_lzw_compressed'
        , 'src/tests/performance_test_files/alice_lzw_decompressed'
        , 'src/tests/performance_test_files/alice_both_compressed'
        , 'src/tests/performance_test_files/alice_both_decompressed'
        , 'src/tests/performance_test_files/frankenstein_huffman_coding_compressed'
        , 'src/tests/performance_test_files/frankenstein_huffman_coding_decompressed'
        , 'src/tests/performance_test_files/frankenstein_lzw_compressed'
        , 'src/tests/performance_test_files/frankenstein_lzw_decompressed'
        , 'src/tests/performance_test_files/frankenstein_both_compressed'
        , 'src/tests/performance_test_files/frankenstein_both_decompressed'
        , 'src/tests/performance_test_files/pride_and_prejudice_huffman_coding_compressed'
        , 'src/tests/performance_test_files/pride_and_prejudice_huffman_coding_decompressed'
        , 'src/tests/performance_test_files/pride_and_prejudice_lzw_compressed'
        , 'src/tests/performance_test_files/pride_and_prejudice_lzw_decompressed'
        , 'src/tests/performance_test_files/pride_and_prejudice_both_compressed'
        , 'src/tests/performance_test_files/pride_and_prejudice_both_decompressed'
    ]
    for file in test_text_files:
        if Path(file).exists():
            Path(file).unlink()
            print(f"File {file} removed")

    run_test_set(service, 'huffman coding')
    run_test_set(service, 'lzw')
    run_test_set(service, 'both')
    print()


if __name__ == "__main__":
    main()
