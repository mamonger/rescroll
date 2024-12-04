import streamlit as st

# Hebrew character counts for all books of the Hebrew Bible, including spaces (approx. 20% added)
character_counts_with_spaces = {
    "Genesis": 93677,  # 78,064 + 20%
    "Exodus": 76442,   # 63,702 + 20%
    "Leviticus": 53747,  # 44,789 + 20%
    "Numbers": 69294,   # 57,745 + 20%
    "Deuteronomy": 62882,  # 52,402 + 20%
    "Joshua": 34053,    # 28,378 + 20%
    "Judges": 33034,    # 27,528 + 20%
    "Ruth": 12222,      # 10,185 + 20%
    "1 Samuel": 45854,  # 38,212 + 20%
    "2 Samuel": 42058,  # 35,048 + 20%
    "1 Kings": 41453,   # 34,544 + 20%
    "2 Kings": 36980,   # 30,817 + 20%
    "Isaiah": 80242,    # 66,868 + 20%
    "Jeremiah": 83238,  # 69,365 + 20%
    "Ezekiel": 69086,   # 57,572 + 20%
    "Hosea": 14350,     # 11,958 + 20%
    "Joel": 3643,       # 3,036 + 20%
    "Amos": 6353,       # 5,294 + 20%
    "Obadiah": 1238,    # 1,032 + 20%
    "Jonah": 2357,      # 1,964 + 20%
    "Micah": 5079,      # 4,233 + 20%
    "Nahum": 1943,      # 1,619 + 20%
    "Habakkuk": 2620,   # 2,184 + 20%
    "Zephaniah": 2972,  # 2,477 + 20%
    "Haggai": 1657,     # 1,381 + 20%
    "Zechariah": 7274,  # 6,062 + 20%
    "Malachi": 2117,    # 1,764 + 20%
    "Psalms": 180209,   # 150,174 + 20%
    "Proverbs": 57924,  # 48,270 + 20%
    "Job": 47882,       # 39,902 + 20%
    "Song of Songs": 6822,  # 5,685 + 20%
    "Ecclesiastes": 27847,  # 23,206 + 20%
    "Lamentations": 17395,  # 14,496 + 20%
    "Daniel": 25644,    # 21,370 + 20%
    "Ezra": 16922,      # 14,102 + 20%
    "Nehemiah": 23548,  # 19,623 + 20%
    "1 Chronicles": 44990,  # 37,492 + 20%
    "2 Chronicles": 47799,  # 39,833 + 20%
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

# Streamlit UI
st.title("Hebrew Bible Manuscript Length Calculator")

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

    # Error handling if no valid input is given
    if total_columns == 0 or total_length == 0:
        st.warning("Please ensure all input values are greater than zero.")
