import streamlit as st 
import streamlit.components.v1 as components
import decimal

st.set_page_config(page_title="Midterm", layout="centered")
st.title("Midterm")

st.header("Student Information")
class_options = ["3/11", "3/12"]
selected_class = st.selectbox("Select your class:", class_options)
nickname = st.text_input("Nickname")
student_number = st.text_input("Student Number")

# ==== Part I: Sudoku Puzzle (3pts) ====
st.header("Part I: Sudoku Puzzle (3pts)")
st.write("**Instruction:** Solve the following Sudoku puzzle using the numbers 1 to 9.")

puzzle = st.secrets["sudoku"]["puzzle"]
solution = st.secrets["sudoku"]["solution"]

sudoku = components.declare_component("sudoku", path="sudoku_component")
# Call the sudoku component passing the puzzle as default
board = sudoku(default=puzzle)
# st.write(board)

answers = st.secrets["answers"]

# ==== Part II: Counting Combinations (15pts) ====
st.header("Part II: Counting Combinations (15pts)")
st.write("**Instruction:** Given the problem below, answer the following questions by selecting the correct answer.")

st.markdown("""
**(item 2-6)** Suppose that the five-character code has the following restrictions:  
- Numbers and letters  
- Uppercase and lowercase letters  
- Cannot repeat characters
""")
# Image
st.image("5ch.png")
questions_2_6 = {
    2: ("What characters can make up the code?", ["a. 10 numbers", "b. 26 letters", "c. 10 numbers and 26 letters", "d. 10 numbers and 52 letters"], answers["q2"]),
    3: ("What sets of characters can the code contain?", ["a. a-z (lowercase letters)", "b. 0-9 (numbers)", "c. A-Z (uppercase letters)", "d. All of the above"], answers["q3"]),
    4: ("How many possible characters are there for the first spot in the password?", ["a. 60 possible letters and numbers", "b. 62 possible letters and numbers", "c. 61 possible letters and numbers", "d. 59 possible letters and numbers"], answers["q4"]),
    5: ("How many possible characters are there for the fifth spot in the password?", ["a. 60 possible letters and numbers", "b. 58 possible letters and numbers", "c. 61 possible letters and numbers", "d. 59 possible letters and numbers"], answers["q5"]),
    6: ("How many total password combinations are possible?", ["a. 44,261,653,680 possible combinations", "b. 916,132,832 possible combinations", "c. 776,520,240 possible combinations", "d. 13,388,280 possible combinations"], answers["q6"]),
}
for qnum in questions_2_6:
    q, opts, _ = questions_2_6[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

st.markdown("""
**(item 7-11)** Suppose that the five-character code has the following restrictions:  
- Numbers only  
- Cannot repeat characters
""")
# Image
st.image("5ch.png")
questions_7_11 = {
    7: ("What characters can make up the code?", ["a. 10 numbers", "b. 26 letters", "c. 10 numbers and 26 letters", "d. 10 numbers and 52 letters"], answers["q7"]),
    8: ("What sets of characters can the code contain?", ["a. a-z (lowercase letters)", "b. 0-9 (numbers)", "c. A-Z (uppercase letters)", "d. All of the above"], answers["q8"]),
    9: ("How many possible characters are there for the first spot in the password?", ["a. 62 possible letters and numbers", "b. 10 possible numbers", "c. 61 possible letters and numbers", "d. 9 possible numbers"], answers["q9"]),
    10: ("How many possible characters are there for the fifth spot in the password?", ["a. 60 possible letters and numbers", "b. 10 possible numbers", "c. 61 possible letters and numbers", "d. 6 possible numbers"], answers["q10"]),
    11: ("How many total password combinations are possible?", ["a. 44,261,653,680 possible combinations", "b. 916,132,832 possible combinations", "c. 100,000 possible combinations", "d. 30,240 possible combinations"], answers["q11"]),
}
for qnum in questions_7_11:
    q, opts, _ = questions_7_11[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

st.markdown("""
**(item 12-16)** Suppose that the five-character code has the following restrictions:  
- Numbers and letters  
- Lowercase letters ONLY
""")
# Image
st.image("5ch.png")
questions_12_16 = {
    12: ("What characters can make up the code?", ["a. 10 numbers", "b. 26 letters", "c. 10 numbers and 26 letters", "d. 10 numbers and 52 letters"], answers["q12"]),
    13: ("What sets of characters can the code contain?", ["a. a-z (lowercase letters)", "b. 0-9 (numbers)", "c. A-Z (uppercase letters)", "d. a and b" ], answers["q13"]),
    14: ("How many possible characters are there for the first spot?", ["a. 62 possible letters and numbers", "b. 26 possible letters and numbers", "c. 36 possible letters and numbers", "d. 10 possible letters and numbers"], answers["q14"]),
    15: ("How many possible characters are there for the fifth spot?", ["a. 26 possible letters and numbers", "b. 22 possible letters and numbers", "c. 36 possible letters and numbers", "d. 32 possible letters and numbers"], answers["q15"]),
    16: ("How many total password combinations are possible?", ["a. 916,132,832 possible combinations", "b. 60,466,176 possible combinations", "c. 45,239,040 possible combinations", "d. 11,881,376 possible combinations"], answers["q16"]),
}
for qnum in questions_12_16:
    q, opts, _ = questions_12_16[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

# ==== Part III: GCF (2pts) ====
st.header("Part III: Greatest Common Factor (2pts)")
st.write("**Instruction:** Solve the following problem.")

gcf_questions = {
    17: "Find the GCF of 44 and 22 using the factorization method.",
    18: "Find the GCF of 20 and 50 using the factorization method.",
    19: "Find the GCF of 32 and 48 using the factorization method.",
    20: "Find the GCF of 30 and 45 using the factorization method.",
}
for qnum, qtext in gcf_questions.items():
    st.text_input(f"**{qnum}. {qtext}**", key=f"gcf{qnum}")

# ==== Grading Functions ====
def grade_sudoku(user_board, puzzle, solution):
    total = correct = 0
    if not user_board:
        return 0
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                total += 1
                if user_board[i][j] == solution[i][j]:
                    correct += 1
    return round(correct / total * 3, 2) if total else 0

def grade_count():
    correct = 0
    total = 0
    for group in (questions_2_6, questions_7_11, questions_12_16):
        for qnum, (_, _, corr) in group.items():
            ans = st.session_state.get(f"q{qnum}", "")
            if ans and ans[0].lower() == corr:
                correct += 1
            total += 1
    return round(correct / total * 15, 2)

def grade_gcf():
    gcf_answers = st.secrets["gcf"]
    score = sum(1 for k, v in gcf_answers.items() if st.session_state.get(k) == v) * 0.5
    return round(score, 2)

# if st.button("Grade Test"):
#    s1 = grade_sudoku(board, puzzle, solution)
#    s2 = grade_count()
#    s3 = grade_gcf()
#    total = s1 + s2 + s3
#    st.success(f"Scores → Part I: {s1}/3 · Part II: {s2}/15 · Part III: {s3}/2 · **Total: {total:.2f}/20**")

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

if st.button("Submit Test"):
    if not nickname or not student_number:
        st.error("Please fill in your nickname and student number.")
    else:
        # Grade parts
        s1 = grade_sudoku(board, puzzle, solution)
        s2 = grade_count()
        s3 = grade_gcf()
        total = s1 + s2 + s3

        # Build submission record
        submission = {
            "nickname": nickname,
            "student_number": student_number,
            "scores": {
                "part1_sudoku": s1,
                "part2_combinations": s2,
                "part3_gcf": s3,
                "total": total
            },
            "answers": {
                "sudoku": board,
                "multiple_choice": {f"q{q}": st.session_state.get(f"q{q}", "") for q in list(questions_2_6) + list(questions_7_11) + list(questions_12_16)},
                "gcf": {k: st.session_state.get(k, "") for k in ["gcf17", "gcf18", "gcf19", "gcf20"]},
            }
        }

        
        # Save to file
        import json, os
        os.makedirs("submissions", exist_ok=True)
        file_path = f"submissions/{student_number}.json"
        with open(file_path, "w") as f:
            json.dump(submission, f, indent=2)

        # st.markdown("### 📄 Submission Preview")
        # st.json(submission)

        import gspread
        from google.oauth2.service_account import Credentials

        # Set up creds and open your sheet
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        
        # Load credentials from Streamlit secrets
        service_account_info = st.secrets["gcp_service_account"]
        creds = Credentials.from_service_account_info(service_account_info, scopes=scopes)
        
        client = gspread.authorize(creds)
        try:
            sheet = client.open("Midterm").worksheet(selected_class)
        except gspread.WorksheetNotFound:
            st.error(f"Worksheet '{selected_class}' not found. Please check your Google Sheet.")

        import datetime
        
        # Timestamp for filenames and sheets
        # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Convert your submission dict into a list of values (flatten if needed)
        row = [
            submission["student_number"],
            submission["nickname"],
            submission["scores"]["part1_sudoku"],
            submission["scores"]["part2_combinations"],
            submission["scores"]["part3_gcf"],
            submission["scores"]["total"]
            # add other fields or stringify answers if needed
        ]

        sheet.append_row(row)
        # st.success("Submission sent to Google Sheets! ✅")
        st.success(f"Submission received! ✅ Total Score: {round(total)}/20")
