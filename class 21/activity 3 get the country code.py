# Step 1: Create country_code, a dictionary of three countries and their dialing codes.

# Step 2: Print a label for the India lookup.

# Step 3: Use .get() to look up India's code, with "Not Found" as a safe backup.

# Step 4: Print a label for the Japan lookup.

# Step 5: Use .get() to look up Japan's code, which is missing, so the backup answer prints instead.




country_code = {"America": "+1", "India": "+91", "japan": "+81"}
print(country_code.get("uae", "not found"))
