# # Daily challenge: Solve the Matrix
# MATRIX_STR = '''
# 7ir
# Tsi
# h%x
# i ?
# sM# 
# $a 
# #t%''' 

# rows = MATRIX_STR.strip().split("\n")

# matrix = [list(row) for row in rows]

# for row in matrix:
#     print(row)


# Daily challenge: Solve the Matrix

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%''' 

# ---- Step 1: turn the string into a 2D list (matrix) ----
rows = MATRIX_STR.strip().split("\n")

# Ensure all rows have the same length by padding with spaces (so column indexing is safe)
max_len = max(len(r) for r in rows)
matrix = [list(r.ljust(max_len)) for r in rows]  # e.g. "sM# " stays aligned

# ---- Step 2: read column-by-column into one long stream ----
stream = []
for col in range(max_len):            # left → right
    for row in range(len(matrix)):    # top → bottom
        stream.append(matrix[row][col])
stream = "".join(stream)

# ---- Steps 3–4: build the decoded message
# Rule: keep letters; if there is a run of non-letters *between* letters, emit a single space.
decoded_chars = []
have_seen_letter = False   # becomes True after first letter is added
in_gap = False             # we are currently in a run of non-letters after letters started

for ch in stream:
    if ch.isalpha():  # it's a letter
        # If we had a gap just before this letter, emit a single space (once)
        if have_seen_letter and in_gap and (not decoded_chars or decoded_chars[-1] != ' '):
            decoded_chars.append(' ')
        decoded_chars.append(ch)
        have_seen_letter = True
        in_gap = False
    else:
        # Non-letter: only matters if we've already started collecting letters
        if have_seen_letter:
            in_gap = True
        # Leading/trailing symbol runs are ignored (no spaces at start/end)

decoded_message = "".join(decoded_chars)
print(decoded_message)