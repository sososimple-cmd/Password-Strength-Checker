# Development Process

This document provides a detailed, step-by-step explanation of how I built the **Password Strength Checker** project. It includes the tools I used, the challenges I faced, and the lessons I learned along the way.

---

## Step 1: Planning the Project

Before writing any code, I outlined the features I wanted to include in the password strength checker:
- Check for minimum length (at least 8 characters).
- Ensure the presence of uppercase and lowercase letters.
- Verify the inclusion of numbers and special characters.
- Provide feedback on password strength (Weak, Moderate, Strong) along with a numerical score (e.g., `Weak (2/5)`).

I decided to use Python because of its simplicity and the availability of libraries like `tkinter` for creating a GUI.

---

## Step 2: Setting Up the Environment

1. **Installed Python**:  
   Downloaded and installed Python from [python.org](https://www.python.org/).

2. **Installed Visual Studio Code (VS Code)**:  
   Installed VS Code as my code editor.

3. **Created a Project Folder**:  
   Created a new folder named `Password-Strength-Checker` to organize my files.

![Folder Structure](screenshots/folder_structure.png)

---

## Step 3: Writing the Password Strength Logic

I started by writing the core logic for checking password strength. Here’s an excerpt of the key part of the code:

```python
def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    if score <= 2:
        return f"Weak ({score}/5)"
    elif score <= 4:
        return f"Moderate ({score}/5)"
    else:
        return f"Strong ({score}/5)"

I tested the logic locally by running the script in the terminal:
python password_strength_checker.py

## Step 4: Adding a GUI
To make the tool more user-friendly, I added a graphical user interface (GUI) using Python’s tkinter library. Here’s how I structured the GUI:

Added a text box for entering the password.
Added a button to trigger the password strength check.
Displayed the result in a label below the button


## Step 5: Uploading to GitHub
Once the project was complete, I uploaded it to GitHub. Here’s how I did it:

Initialized Git in my project folder
git init
Added all files to the staging area
git add .
Committed the changes:
git commit -m "Initial commit: Added password strength checker with GUI"

Linked my local repository to GitHub:
git remote add origin https://github.com/sososimple-cmd/Password-Strength-Checker.git
Pushed the code to GitHub:
git push -u origin main

profile
Qwen2.5-Max
8:50 pm
Great! Let’s create a detailed DEVELOPMENT.md file in Markdown format. This file will document the steps you took to build your project, the challenges you faced, and the lessons you learned. I'll also guide you on how to add this file to your GitHub repository.

Markdown Version of DEVELOPMENT.md
markdown


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
# Development Process

This document provides a detailed, step-by-step explanation of how I built the **Password Strength Checker** project. It includes the tools I used, the challenges I faced, and the lessons I learned along the way.

---

## Step 1: Planning the Project

Before writing any code, I outlined the features I wanted to include in the password strength checker:
- Check for minimum length (at least 8 characters).
- Ensure the presence of uppercase and lowercase letters.
- Verify the inclusion of numbers and special characters.
- Provide feedback on password strength (Weak, Moderate, Strong) along with a numerical score (e.g., `Weak (2/5)`).

I decided to use Python because of its simplicity and the availability of libraries like `tkinter` for creating a GUI.

---

## Step 2: Setting Up the Environment

1. **Installed Python**:  
   Downloaded and installed Python from [python.org](https://www.python.org/).

2. **Installed Visual Studio Code (VS Code)**:  
   Installed VS Code as my code editor.

3. **Created a Project Folder**:  
   Created a new folder named `Password-Strength-Checker` to organize my files.

![Folder Structure](screenshots/folder_structure.png)

---

## Step 3: Writing the Password Strength Logic

I started by writing the core logic for checking password strength. Here’s an excerpt of the key part of the code:

```python
def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    if score <= 2:
        return f"Weak ({score}/5)"
    elif score <= 4:
        return f"Moderate ({score}/5)"
    else:
        return f"Strong ({score}/5)"
I tested the logic locally by running the script in the terminal:

bash


1
python password_strength_checker.py
Screenshot of Testing the Logic :


Step 4: Adding a GUI
To make the tool more user-friendly, I added a graphical user interface (GUI) using Python’s tkinter library. Here’s how I structured the GUI:

Added a text box for entering the password.
Added a button to trigger the password strength check.
Displayed the result in a label below the button.
Screenshot of the GUI :


Step 5: Uploading to GitHub
Once the project was complete, I uploaded it to GitHub. Here’s how I did it:

Initialized Git in my project folder:
bash


1
git init
Added all files to the staging area:
bash


1
git add .
Committed the changes:
bash


1
git commit -m "Initial commit: Added password strength checker with GUI"
Linked my local repository to GitHub:
bash


1
git remote add origin https://github.com/sososimple-cmd/Password-Strength-Checker.git
Pushed the code to GitHub:
bash


1
git push -u origin main
Screenshot of Successful Push :


## Challenges and Errors
When I tried to push my code to GitHub, I got the following error:
error: src refspec main does not match any

Solution : I resolved this by renaming my branch to main:
git branch -M main

Error 2: Merge Conflict with Remote Repository
When I tried to push again, I encountered this error:
! [rejected]        main -> main (fetch first)

Solution : I pulled the remote changes and merged them with my local changes:
git pull origin main --allow-unrelated-histories

After resolving these issues, I successfully pushed my code to GitHub.

## Lessons Learned
Building this project taught me several valuable lessons:

Problem-Solving : Debugging Git errors helped me understand version control better.
GUI Development : Using tkinter gave me hands-on experience with GUI programming.
Documentation : Writing detailed documentation improved my ability to explain my thought process and solutions.
Attention to Detail : Testing edge cases (e.g., empty passwords, very long passwords) ensured the program worked reliably.