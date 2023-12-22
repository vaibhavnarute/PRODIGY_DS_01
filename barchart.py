import matplotlib.pyplot as plt

# Sample data for age groups and corresponding counts
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49']
counts = [50, 120, 300, 200, 80]

# Create a bar chart
plt.bar(age_groups, counts, color='green')

# Add labels and title
plt.title('Distribution of Individuals in Different Age Groups')
plt.xlabel('Age Groups')
plt.ylabel('Number of Individuals')

# Show the plot
plt.show()

