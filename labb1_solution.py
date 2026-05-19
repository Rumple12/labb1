import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------
# This checks if a year is a leap year using standard modulo (%) logic.
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# if its devisible by 4 (if its a normal year) or
# if its divisible by 400 (if its a centuary year (tex: 2000))
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# This function takes a date and formats it as a readable string.
def date_as_text(date_num):
    
    # Ensure the input is treated as an integer
    date_num = int(date_num)
    
    # '//' is floor division (drops the decimal). '%' is modulo (remainder).
    # This extracts the year, month, and day components.
    year = date_num // 10000
    month = (date_num // 100) % 100
    day = date_num % 100
    # An 'f-string' formats text. {year:04d} means "insert 'year' here, padded with zeros to be 4 digits long".
    return f"{year:04d}-{month:02d}-{day:02d}"
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# Generates a NumPy array of all expected dates between two years.
def all_dates(start_year, end_year):
    
    # A NumPy array holding the standard number of days in each of the 12 months. 
    month_lengths = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

    # An empty standard Python list to hold our generated dates temporarily.
    date_list = []

    # range(a, b) loops from a up to, but NOT including b so we add +1 to include the end year.
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):

            # Arrays are 0 indexed, so month 1 is at index 0. 
            num_days = int(month_lengths[month - 1])

            # Adjust for February in leap years.
            if month == 2 and (is_leap_year(year)==True):
                num_days = 29

            for day in range(1, num_days + 1):
                # Reconstruct the integer date format (YYYYMMDD) and add it to our list.
                date_list.append(year * 10000 + month * 100 + day)

    # Convert the standard list into a NumPy array for faster mathematical operations later.
    return np.array(date_list)
#----------------------------------------------------------------------


#----------------------------------------------------------------------
# Standard Python rounds numbers ending in .5 to the nearest EVEN number.
# This custom function forces standard mathematical rounding (half-up).
def round_to_integer(values):
    # np.where is used like this; np.where(condition, do_if_true, do_if_false)
    return np.where(values >= 0, np.floor(values + 0.5), np.ceil(values - 0.5)).astype(int)
    #.where checks if the value is positive or negative. If positive, it adds 0.5 and floors it (rounding up).
    # If negative, it subtracts 0.5 and ceils it (rounding down). Finally, it converts the result to integers.
#----------------------------------------------------------------------






# --- DATA LOADING ---
# np.loadtxt reads a text/data file and automatically parses it into a 2D matrix (rows and columns).
sundsvall_data = np.loadtxt("Sundsvall.dat")




# --- DATA SLICING from the file ---
# Syntax explanation: [:, 0] means "give me all rows (:), but only column index 0".
# This separates the 2D matrix into 1D arrays for easier use.
dates = sundsvall_data[:, 0].astype(int)#astype turns it from string to int automatically.
daily_mean = sundsvall_data[:, 1]
daily_max = sundsvall_data[:, 2]
daily_min = sundsvall_data[:, 3]

#print(np.__version__) ignore this line jakob its just to check version of numpy.

# Extract arrays of just the years and months from the date array. 
# We don't need loops; NumPy does math on the whole array at once.
years = dates // 10000
months = (dates // 100) % 100


# --- TASK 1 a): Check if any days are missing ---
print("----------------Task 1 a)----------------")
num_rows = len(dates)                   # Count the actual rows (dates) in the file
expected_dates = all_dates(2008, 2017)  # Generate what the dates *should* be
expected_count = len(expected_dates)    # Count the number of expected rows.

# np.unique removes duplicates. If the length changes, we had duplicate dates.
unique_dates = np.unique(dates)

is_unique = (len(unique_dates) == num_rows)
# if the length of unique_dates is the same as num_rows, then all dates are unique return True. 
# If not, we had duplicates so return false.

# Sorts the file's dates and compares them exactly against our generated expected dates.
all_expected_dates_exist = np.array_equal(np.sort(dates), expected_dates)



print(f"Number of rows/days in file:                      {num_rows}")
print(f"Number of calendar days 2008-01-01 to 2017-12-31: {expected_count}") 
print(f"Row count matches:                                {num_rows == expected_count}")
print(f"All dates are unique:                             {is_unique}") 
print(f"Date series matches all expected dates:           {all_expected_dates_exist}")
print()

if ((num_rows == expected_count) and (is_unique) and (all_expected_dates_exist)):
    print("Conclusion: Yes, all days from 2008 to 2017 exist.\n")
else:
    print("Conclusion: No, data is missing days or has duplicates days.\n")



# --- TASK 1b): Find the coldest temperature and when it happened ---
print("----------------Task 1 b)----------------")
coldest_min = np.min(daily_min) # Finds the absolute lowest number in the array

 
# 'daily_min == coldest_min' creates an array of True/False values.
# Passing that into 'dates[]' filters the dates array, returning only the dates where the condition is True.
coldest_dates = dates[daily_min == coldest_min]
# Convert all the dates into a list of text strings
text_dates = [date_as_text(d) for d in coldest_dates]
# Combine that list into a single string, separated by commas
joined_dates = " and ".join(text_dates)


# .1f formats the floating-point number to 1 decimal place.
print(f"Coldest daily minimum: {coldest_min:.1f} C")
# Print the final result, adding the extra new line at the end
print("Date(s):              ", joined_dates, "\n")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# --- TASK 1c): Empirical Cumulative Distribution Function (ECDF) ---
print("----------------Task 1 c)----------------")

sorted_means = np.sort(daily_mean) #sorts the daily mean temperatures from lowest to highest. 
# This will be our x-axis for the ECDF.

# Creates a range of numbers representing probabilities (e.g., 1/3653, 2/3653 ... 1.0)
ecdf_y = (np.arange(1, num_rows + 1) / num_rows)

# For the plot to start correctly at F(x)=0, we add an artificial starting point just before the lowest temperature.
ecdf_x_plot = np.concatenate(([sorted_means[0] - 1], sorted_means))
ecdf_y_plot = np.concatenate(([0], ecdf_y))


#----
# Set up the plot canvas
plt.figure(figsize=(8, 5))
# A 'step' plot creates the staircase look required for an ECDF. 'where="post"' means the step happens after the data point.
plt.step(ecdf_x_plot, ecdf_y_plot, where="post")
plt.xlabel("Daily Mean (degrees C)")
plt.ylabel("F(x)")
plt.title("Empirical Distribution Function for Daily Means")
plt.grid(True, alpha=0.3)
plt.tight_layout() # Adjusts margins so nothing gets cut off
plt.savefig("figures/task1c_ecdf.png", dpi=150) # Save to disk instead of showing on screen
plt.close() # Free up memory
#----

# Calculates the proportion of days where the temp was 10 or below.
# 'daily_mean <= 10' makes a True/False array. True is 1, False is 0. 
# The mean of those 1s and 0s gives the probability!
f_10 = np.mean(daily_mean <= 10)
p_over_10 = 1 - f_10 # The probability it is OVER 10 degrees.

print(f"F(10) = proportion of daily means <= 10 degrees C: {f_10:.3f}")
print(f"P(X > 10) = 1 - F(10):                             {p_over_10:.3f}")
print("Figure saved as figures/task1c_ecdf.png\n")



# --- TASK 2a): Isolate and analyze data for May 2012 ---
print("----------------Task 2 a)----------------")
# Combine two conditions using '&' (bitwise AND) to find the exact month and year.
may_2012 = (years == 2012) & (months == 5)
# Use that boolean mask to filter our arrays
may_dates = dates[may_2012]
may_means = daily_mean[may_2012]
may_rounded = round_to_integer(may_means)

print("Date        Rounded Daily Mean")
# 'zip' lets us loop through two lists at the exact same time.
for d, val in zip(may_dates, may_rounded):
    # '<12' means left-align with 12 spaces. '>5d' means right-align integer with 5 spaces. (Makes columns neat)
    print(f"{date_as_text(d):<12}{val:>5d}")
print()

# np.unique with return_counts=True acts like a frequency counter. 
# It returns the unique temperatures and how many times they occurred.
frequency_values, frequencies = np.unique(may_rounded, return_counts=True)
print("Frequency Table")
print("Value    Frequency")
for val, freq in zip(frequency_values, frequencies):
    print(f"{val:>5d}{freq:>11d}")
print()



# --- TASK 2b: Calculate descriptive statistics ---
print("----------------Task 2 b)----------------")
max_frequency = np.max(frequencies)
# Find which value(s) appeared the most (the mode)
modes = frequency_values[frequencies == max_frequency]

# Built-in NumPy functions handle the heavy math
median_val = np.median(may_rounded)
mean_val = np.mean(may_rounded)
range_val = np.max(may_rounded) - np.min(may_rounded)

# 'ddof' stands for Delta Degrees of Freedom. 
# ddof=0 calculates the population variance/std dev (dividing by N).
# ddof=1 calculates the sample variance/std dev (dividing by N-1).
variance_population = np.var(may_rounded, ddof=0)
variance_sample = np.var(may_rounded, ddof=1)
std_dev_population = np.std(may_rounded, ddof=0)
std_dev_sample = np.std(may_rounded, ddof=1)

print("Mode:", ", ".join([str(int(val)) for val in modes]))
print(f"Median:                                  {median_val:.1f}")
print(f"Mean:                                    {mean_val:.3f}")
print(f"Range:                                   {range_val}")
print(f"Variance, population (ddof=0):           {variance_population:.3f}")
print(f"Variance, sample (ddof=1):               {variance_sample:.3f}")
print(f"Standard Deviation, population (ddof=0): {std_dev_population:.3f}")
print(f"Standard Deviation, sample (ddof=1):     {std_dev_sample:.3f}\n")
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# --- TASK 3: Monthly Average Temperatures (2008-2017) ---
print("----------------Task 3----------------")
month_names = np.array([
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
])
month_short = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Create an array of 12 zeros to hold our upcoming calculations
monthly_means = np.zeros(12)

# Loop through months 1 to 12
for month_number in range(1, 13):
    # Filter the entire 10-year dataset for 'month_number', find the mean, and store it.
    monthly_means[month_number - 1] = np.mean(daily_mean[months == month_number])

print("Month  Name        Mean Temperature")
for month_number in range(1, 13):
    print(f"{month_number:>5d}  {month_names[month_number - 1]:<10}{monthly_means[month_number - 1]:>10.2f}")

# Plot a bar chart
plt.figure(figsize=(9, 5))
# x-axis is 1-12, y-axis is our calculated means.
plt.bar(np.arange(1, 13), monthly_means, color="#4c78a8")
# Replace the numbers on the x-axis with the short month names
plt.xticks(np.arange(1, 13), month_short)
plt.xlabel("Month")
plt.ylabel("Average Daily Mean Temperature (degrees C)")
plt.title("Mean Temperature per Month, Sundsvall 2008-2017")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("figures/task3_monthly_averages.png", dpi=150)
plt.close()
print("Figure saved as figures/task3_monthly_averages.png\n")
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# --- TASK 4: Temperature Correlation Analysis ---
print("----------------Task 4----------------")

# We want to see if today's temp is related to tomorrow's temp.
# We do this by comparing two offset arrays.
# daily_mean[:-1] means "All elements EXCEPT the last one" (Days 1 to N-1)
# daily_mean[1:] means "All elements EXCEPT the first one" (Days 2 to N)
# np.corrcoef returns a matrix, [0, 1] extracts the specific correlation number we want.
correlation_1_day = np.corrcoef(daily_mean[:-1], daily_mean[1:])[0, 1]

# Same logic, but offset by 10 days instead of 1.
correlation_10_days = np.corrcoef(daily_mean[:-10], daily_mean[10:])[0, 1]

print(f"Correlation between day n and day n+1:  {correlation_1_day:.3f}")
print(f"Correlation between day n and day n+10: {correlation_10_days:.3f} \n")
print("Interpretation: A correlation close to 1 means strong positive correlation.")
print("The 1-day correlation is stronger than the 10-day correlation.")
print("This supports the rule of thumb that tomorrow's temperature is often close to today's,")
print("but the relationship becomes weaker as the time distance increases.")

print("\n\n\n\n----------------------DONE--------------------")
