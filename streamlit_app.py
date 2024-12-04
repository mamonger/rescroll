import streamlit as st

# Hebrew word counts
word_counts = {
    "Genesis": 20512,
    "Exodus": 16723,
    "Leviticus": 11950,
    "Numbers": 16413,
    "Deuteronomy": 14488,
    # Add more books as needed...
}

def calculate_columns_and_length(word_count, lines_per_column, characters_per_line, column_width_cm):
    """
    Calculate the total number of columns and the total manuscript length.
    """
    try:
        avg_characters_per_word = 7.5  # Average characters per Hebrew word
        total_characters = word_count * avg_characters_per_word
        characters_per_column = lines_per_column * characters_per_line
        total_columns = total_characters / characters_per_column
        total_length_cm = total_columns * column_width_cm
        return round(total_columns, 2), round(total_length_cm, 2)
    except ZeroDivisionError:
        return 0, 0

# Streamlit UI
st.title("Ancient Manuscript Length Calculator")

# Input Fields
book = st.selectbox("Select Book:", list(word_counts.keys()))
lines_per_column = st.number_input("Lines per Column:", min_value=1, value=40, step=1)
characters_per_line = st.number_input("Characters per Line:", min_value=1, value=30, step=1)
column_width_cm = st.number_input("Column Width (cm):", min_value=0.1, value=10.0, step=0.1)

# Calculate button
if st.button("Calculate"):
    # Get the word count for the selected book
    word_count = word_counts.get(book)

    # Perform the calculation
    total_columns, total_length = calculate_columns_and_length(
        word_count,
        lines_per_column,
        characters_per_line,
        column_width_cm
    )

    # Display Results
    st.subheader(f"Results for {book}")
    st.write(f"**Total Columns:** {total_columns}")
    st.write(f"**Total Length:** {total_length} cm")

    # Error handling if no valid input is given
    if total_columns == 0 or total_length == 0:
        st.warning("Please ensure all input values are greater than zero.")

