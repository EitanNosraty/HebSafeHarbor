from hebsafeharbor import HebSafeHarbor

hsh = HebSafeHarbor()

original_file_path = "files/original.txt"
new_file_path = "files/modified.txt"
report_path = "files/report.txt"

try:
    with open(original_file_path, "r", encoding="utf-8") as original_file:
        original_text = original_file.read()
except FileNotFoundError:
    print(f"The file '{original_file_path}' does not exist.")
    exit(1)

# Step 2: Modify the text (for example, replace some text)
doc = {"text": original_text}
output = hsh([doc])
print(output[0].anonymized_text.text)

modified_text = output[0].anonymized_text.text

# Step 3: Create a new file and write the modified text to it
try:
    with open(new_file_path, "w", encoding="utf-8") as new_file:
        new_file.write(modified_text)
    print(f"Modified text saved to '{new_file_path}'.")
except Exception as e:
    print(f"An error occurred while creating the new file: {e}")

consolidated_results = []

# Extract recognized entities and their text values
for entity in output[0].consolidated_results:
    consolidated_results.append(
        f"Entity: {entity.entity_type}, Strat: {entity.start}, End: {entity.end}, Score: {entity.score}"
    )

# Join the extracted results into a single text
report_text = "\n".join(consolidated_results)

try:
    with open(report_path, "w", encoding="utf-8") as new_file:
        new_file.write(report_text)
    print(f"Modified text saved to '{report_path}'.")
except Exception as e:
    print(f"An error occurred while creating the new file: {e}")
