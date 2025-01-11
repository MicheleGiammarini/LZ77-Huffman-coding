import zlib

def compress_file(input_file, output_file):
    """
    Compress a file in a lossless manner.
    
    Args:
        input_file (str): Path to the file to be compressed.
        output_file (str): Path where the compressed file will be saved.
    """
    try:
        with open(input_file, 'rb') as f_in:
            data = f_in.read()
            compressed_data = zlib.compress(data, level=9)
        
        with open(output_file, 'wb') as f_out:
            f_out.write(compressed_data)
        
        print(f"File successfully compressed: {output_file}")
    except Exception as e:
        print(f"Error during compression: {e}")


def decompress_file(input_file, output_file):
    """
    Decompress a compressed file in a lossless manner.
    
    Args:
        input_file (str): Path to the compressed file.
        output_file (str): Path where the decompressed file will be saved.
    """
    try:
        with open(input_file, 'rb') as f_in:
            compressed_data = f_in.read()
            decompressed_data = zlib.decompress(compressed_data)
        
        with open(output_file, 'wb') as f_out:
            f_out.write(decompressed_data)
        
        print(f"File successfully decompressed: {output_file}")
    except Exception as e:
        print(f"Error during decompression: {e}")


# Example usage
if __name__ == "__main__":
    input_path = "input_file.txt"
    compressed_path = "compressed_file.zlib"
    decompressed_path = "decompressed_file.txt"

    # Compress the file
    compress_file(input_path, compressed_path)

    # Decompress the file
    decompress_file(compressed_path, decompressed_path)
