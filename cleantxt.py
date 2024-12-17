from openai import OpenAI

# Set your OpenAI API Key
client = OpenAI(api_key="here")

def process_text_in_chunks(file_path, output_path, chunk_size=4000):
    def call_gpt_api(chunk):
        """Send a chunk of text to GPT for correction and cleaning."""
        prompt = (
            "Améliore ce texte en corrigeant les erreurs OCR et en retirant les fragments incompréhensibles. "
            "Conserve la mise en page, les titres, la numérotation et le maximum d’éléments cohérents. N’invente rien. "
            + chunk
        )
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You clean and format textual data."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error with GPT API: {e}")
            return None

    try:
        # Read the input file with `utf-8` encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    total_chunks = len(text) // chunk_size + 1

    # Open the output file in append mode to save progress incrementally
    with open(output_path, 'a', encoding='utf-8') as output_file:
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]
            print(f"Processing chunk {i // chunk_size + 1} of {total_chunks}...")
            cleaned_chunk = call_gpt_api(chunk)
            if cleaned_chunk:
                output_file.write(cleaned_chunk + "\n")
                output_file.flush()  # Ensure progress is written to disk immediately
            else:
                print(f"Error processing chunk {i // chunk_size + 1}. Skipping.")

    print(f"Text cleaning completed. Partial or full cleaned text saved to {output_path}")

# File paths
input_file = r"D:\kotza_truncated_2_512_686.txt"  # Replace with your input file path
output_file = r"D:\cleaned_output.txt"  # Replace with your desired output file path

# Process the text
process_text_in_chunks(input_file, output_file)
