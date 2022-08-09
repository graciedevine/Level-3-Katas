# Write a function that takes in a string like 'WOW this is REALLY amazing' and returns 'Wow this is really amazing'.
# String should be capitalized and properly spaced.

# Steps:
# Check if first letter is uppercase -> if not, make it uppercase
# Change all letters to be lowercase


def filter_words(s):
    capitalization = s[0].upper() + s[1:].lower()
    return " ".join(capitalization.split())

    # return ' '.join(st.capitalize().split())
    # alternative solution that I liked; did not know about .capitalize()


print(filter_words("Ydx  mbzk  gnqlefidegbndxo  bdbcftbav  dgvgxxabvbu"))
