# Lossless File Compression and Decompression in Python

This repository contains a Python implementation for **lossless file compression and decompression** using the `zlib` module. The algorithm used is based on **DEFLATE**, which combines **LZ77 (sliding window compression)** and **Huffman coding**.

## How the Algorithm Works

The algorithm relies on **zlib**, which implements the DEFLATE compression algorithm. Here’s a breakdown of the key steps in the compression and decompression process:

### **Compression**
1. **Input File Reading**:
   - The file is opened in binary mode (`rb`), ensuring compatibility with any file type (text, images, etc.).
2. **Data Compression**:
   - The data is read into memory, and the `zlib.compress()` function is used to compress it. The compression level can be set between 1 (fastest) to 9 (most compressed).
3. **Save Compressed Data**:
   - The compressed data is written to a new file using binary write mode (`wb`).

### **Decompression**
1. **Input Compressed File Reading**:
   - The compressed file is opened in binary mode (`rb`).
2. **Data Decompression**:
   - The `zlib.decompress()` function restores the original data from the compressed file.
3. **Save Decompressed Data**:
   - The decompressed data is written to a new file in binary mode (`wb`), ensuring the file is restored to its original state.

### **Why is it Lossless?**
- The DEFLATE algorithm preserves all the original data and restores it exactly when decompressed, ensuring that no information is lost.

## How to Use

1. **Install Dependencies**:  
   No additional libraries are required; Python's built-in `zlib` module is used.

2. **Usage**:  
   - You can use the provided functions to compress and decompress files in a lossless manner.

3. **Example**:  
   The following script demonstrates how to use the compression and decompression functions:

   ```python
   # Example usage
   if __name__ == "__main__":
       input_path = "input_file.txt"
       compressed_path = "compressed_file.zlib"
       decompressed_path = "decompressed_file.txt"
   
       # Compress the file
       compress_file(input_path, compressed_path)
   
       # Decompress the file
       decompress_file(compressed_path, decompressed_path)
