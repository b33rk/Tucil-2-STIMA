import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Set the limits of the plot
# ax.set_xlim(-10, 10)
# ax.set_ylim(-10, 10)

# Draw the point at (-3, 5)
ax.plot(-3, 5, 'ro')  # 'ro' specifies red color and circle marker

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Point at (-3, 5)')

# Show the plot
plt.show()