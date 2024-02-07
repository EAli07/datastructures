def merge_files(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            # Read content from both files
            content_file1 = file1.read()
            content_file2 = file2.read()

            # Combine content
            merged_content = content_file1 + '\n' + content_file2

            # Write the merged content to a new file
            with open(output_file_path, 'w') as output_file:
                output_file.write(merged_content)

        print(f"Files merged successfully. Merged content saved to '{output_file_path}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'file1.txt', 'file2.txt', and 'output.txt' with your file paths
    file1_path = 'file1.txt'
    file2_path = 'file2.txt'
    output_file_path = 'output.txt'

    merge_files(file1_path, file2_path, output_file_path)
