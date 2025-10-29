# Save number if its valid

try: 
    get_number: str = input("Type your number and receive our offers: ")
    clean_number: str = get_number.strip()
    string_to_number: int = int(get_number)
    
    if len(get_number) != 10:
        raise ValueError("The number must contain exactly 10 digits.")
        
    number_to_string: str = str(string_to_number)
            
    with open("logs.txt", "a") as numbers_log:
        add_number: str = numbers_log.writelines(number_to_string + "\n")
        
    print("Number registered successfully")
    
except ValueError as error: 
    print(f"Invalid input: {error}")

except OSError as file_error:
    print(f"File error: {file_error}")
    
    
    
# Read and show file content

with open("logs.txt") as numbers_file:
    for number in numbers_file:
        clean_number = number.strip()
        print(clean_number)
        
        
# Practice for counting valid and invalid numbers

with open("logs.txt") as numbers_file:
    invalid_numbers = 0
    valid_numbers = 0
    dont_know = 0

    for number in numbers_file:
        if "invalid" in number.lower():
            invalid_numbers += 1
        elif "valid" in number.lower():
            valid_numbers += 1
        else:
            dont_know += 1

print(f"Valid numbers: {valid_numbers}")
print(f"Invalid numbers: {invalid_numbers}")
print(f"Don't know: {dont_know}")

# Save various measurements
keep_adding_data: bool = True

while keep_adding_data:
    new_measurement: str = input("Type the measurement for your plant: ")
    
    try: 
        clean_measurement: float = float(new_measurement.strip())
        
        with open("measurements.txt", "a") as measurements:
            measurements.writelines(str(clean_measurement) + "\n")
    except ValueError:
        print(f"There was a problem, please enter a numeric value")
        continue
    
    ask_continuation: str = input("Do you want to add another value? (Y/N): ")
    clean_response: str = ask_continuation.lower().strip()
    
    if clean_response != "y":
        keep_adding_data = False
    
if not keep_adding_data:
    print("All registered measurements: ")
    
    with open("measurements.txt") as measurements:
        for measurement in measurements:
            print("\t" + measurement.strip())
            
            
# Copy files
with open("measurements.txt") as measurements:
    with open("measurements_backup.txt", "w") as backup:
        for measurement in measurements: 
            backup.writelines(measurement)
            
            
import shutil

shutil.copyfile("measurements.txt", "measurements_backup_2.txt")