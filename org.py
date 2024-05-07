from pathlib import Path
import re

def process_packages_file(input_file):
    try:
        file_path = Path(input_file)
        if not file_path.exists():
            print(f"Error: File '{input_file}' not found.")
            return None
        
        # Read the content of the file as a single string
        file_content = file_path.read_text()
        
        # Remove commas and split the content into words
        words = file_content.replace(",", "").split()
        
        # Remove version numbers using regex and strip extra spaces
        words_without_versions = [re.sub(r'\d+(\.\d+)*', '', word).strip() for word in words]
        
        # Filter out empty strings (caused by stripping version numbers)
        filtered_words = [word for word in words_without_versions if word]
        
        # Join the words back into a single string with newlines
        processed_content = "\n".join(filtered_words)
        
        return processed_content
    
    except Exception as e:
        print(f"Error processing file '{input_file}': {e}")
        return None

def write_to_file(content, output_file):
    try:
        output_path = Path(output_file)
        output_path.write_text(content)
        print(f"Processed content written to '{output_file}'")
    
    except Exception as e:
        print(f"Error writing to file '{output_file}': {e}")

def main():
    try:
        # Prompt the user for the input file path
        input_file = input("Enter the path to the input text file: ").strip()
        if not input_file:
            print("Error: Please provide a valid input file path.")
            return
        
        # Process the input file
        processed_content = process_packages_file(input_file)
        if processed_content:
            # Display the processed content
            print(processed_content)
            
            # Ask the user if they want to write the processed content to a new file
            write_option = input("Do you want to write the processed content to a new file? (yes/no): ").strip().lower()
            if write_option == "yes":
                # Prompt the user for the output file path
                output_file = input("Enter the path to the output text file: ").strip()
                if output_file:
                    # Write the processed content to the output file
                    write_to_file(processed_content, output_file)
                else:
                    print("Error: Please provide a valid output file path.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

