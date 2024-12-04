import streamlit as st
import matplotlib.pyplot as plt

# Hebrew character counts for all books of the Hebrew Bible, including spaces (approx. 20% added)
character_counts_with_spaces = {
    "Genesis": 93677,
    "Exodus": 76442,
    "Leviticus": 53747,
    "Numbers": 69294,
    "Deuteronomy": 62882,
    "Joshua": 34053,
    "Judges": 33034,
    "Ruth": 12222,
    "1 Samuel": 45854,
    "2 Samuel": 42058,
    "1 Kings": 41453,
    "2 Kings": 36980,
    "Isaiah": 80242,
    "Jeremiah": 83238,
    "Ezekiel": 69086,
    "Hosea": 14350,
    "Joel": 3643,
    "Amos": 6353,
    "Obadiah": 1238,
    "Jonah": 2357,
    "Micah": 5079,
    "Nahum": 1943,
    "Habakkuk": 2620,
    "Zephaniah": 2972,
    "Haggai": 1657,
    "Zechariah": 7274,
    "Malachi": 2117,
    "Psalms": 180209,
    "Proverbs": 57924,
    "Job": 47882,
    "Song of Songs": 6822,
    "Ecclesiastes": 27847,
    "Lamentations": 17395,
    "Daniel": 25644,
    "Ezra": 16922,
    "Nehemiah": 23548,
    "1 Chronicles": 44990,
    "2 Chronicles": 47799,
}

def calculate_columns_and_length(total_characters, lines_per_column, characters_per_line, column_width_cm, right_margin, left_margin, inter_column_margin):
    """
    Calculate the total number of columns and the total manuscript length,
    accounting for margins (right before first column, left after last column, and inter-column).
    """
    try:
        # Calculate total columns
        characters_per_column = lines_per_column * characters_per_line
        total_columns = total_characters / characters_per_column

        # Total length includes column widths, inter-column margins, and outer margins
        total_length_cm = (
            total_columns * column_width_cm  # Width of all columns
            + (total_columns - 1) * inter_column_margin  # Inter-column margins
            + right_margin  # Margin before the first column
            + left_margin   # Margin after the last column
        )
        return round(total_columns, 2), round(total_length_cm, 2)
    except ZeroDivisionError:
        return 0, 0

def plot_layout(total_columns, column_width_cm, right_margin, left_margin, inter_column_margin, total_length_cm):
    """
    Generate a visualization of the manuscript layout.
    """
    fig, ax = plt.subplots(figsize=(10, 2))
    
    # Set up the total length as the width of the image
    ax.set_xlim(0, total_length_cm)
    ax.set_ylim(0, 10)

    # Draw the margins and columns
    x = right_margin
    for i in range(int(total_columns)):
        # Draw column
        ax.add_patch(plt.Rectangle((x, 3), column_width_cm, 4, edgecolor='black', facecolor='lightgray'))
        x += column_width_cm
        if i < total_columns - 1:
            # Add inter-column margin
            x += inter_column_margin
    
    # Add right margin
    x += left_margin

    # Add labels for dimensions
    ax.text(right_margin / 2, 8, f"Right Margin\n{right_margin} cm", ha='center', fontsize=8)
    ax.text(total_length_cm - left_margin / 2, 8, f"Left Margin\n{left_margin} cm", ha='center', fontsize=8)
    ax.text(total_length_cm / 2, 1, f"Total Length: {total_length_cm} cm", ha='center', fontsize=10, color='blue')

    # Remove axes for a clean look
    ax.axis('off')

    return fig

# Streamlit UI
st.title("Ancient Manuscript Length Calculator (With Visualization)")

# Input Fields
book = st.selectbox("Select Book:", list(character_counts_with_spaces.keys()))
lines_per_column = st.number_input("Lines per Column:", min_value=1, value=40, step=1)
characters_per_line = st.number_input("Characters per Line:", min_value=1, value=30, step=1)
column_width_cm = st.number_input("Column Width (cm):", min_value=0.1, value=10.0, step=0.1)
right_margin = st.number_input("Right Margin Before First Column (cm):", min_value=0.0, value=1.0, step=0.1)
left_margin = st.number_input("Left Margin After Last Column (cm):", min_value=0.0, value=1.0, step=0.1)
inter_column_margin = st.number_input("Margin Between Columns (cm):", min_value=0.0, value=0.5, step=0.1)

# Calculate button
if st.button("Calculate"):
    # Get the character count for the selected book
    total_characters = character_counts_with_spaces.get(book)

    # Perform the calculation
    total_columns, total_length = calculate_columns_and_length(
        total_characters,
        lines_per_column,
        characters_per_line,
        column_width_cm,
        right_margin,
        left_margin,
        inter_column_margin
    )

    # Display Results
    st.subheader(f"Results for {book}")
    st.write(f"**Total Columns:** {total_columns}")
    st.write(f"**Total Length:** {total_length} cm")

    # Generate and display visualization
    if total_columns > 0 and total_length > 0:
        fig = plot_layout(total_columns, column_width_cm, right_margin, left_margin, inter_column_margin, total_length)
        st.pyplot(fig)

    # Error handling if no valid input is given
    if total_columns == 0 or total_length == 0:
        st.warning("Please ensure all input values are greater than zero.")
