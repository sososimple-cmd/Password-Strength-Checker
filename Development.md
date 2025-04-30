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

![Screenshot 2025-04-29 200333](https://github.com/user-attachments/assets/7b0c044d-a1d9-4ad9-830b-a53a7d367c99)


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
```

---

I tested the logic locally by running the script in the terminal:
python password_strength_checker.py

![Screenshot 2025-04-29 200808](https://github.com/user-attachments/assets/d3b57489-ad0e-4603-b4c6-e5c880597bf4)


![Screenshot 2025-04-29 200607](https://github.com/user-attachments/assets/ee322f81-0565-4604-8610-dc97ca663ef9)


![Screenshot 2025-04-29 200751](https://github.com/user-attachments/assets/a7419c05-27d0-4db8-b47b-1f40216a92a0)




## Step 4: Adding a GUI
To make the tool more user-friendly, I added a graphical user interface (GUI) using Python’s tkinter library. Here’s how I structured the GUI:

![Screenshot 2025-04-29 201414](https://github.com/user-attachments/assets/c14e39b4-d5f2-449f-b7c3-c221423dc4ba)

![Screenshot 2025-04-29 201457](https://github.com/user-attachments/assets/c7aac13c-a74a-423d-8aa2-52dcdc8c59a9)



Added a text box for entering the password.
Added a button to trigger the password strength check.
Displayed the result in a label below the button

![Screenshot 2025-04-29 201505](https://github.com/user-attachments/assets/4e69767d-3c73-4a4f-85fe-40b7dcef905a)



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






## Challenges and Errors
When I tried to push my code to GitHub, I got the following error:
error: src refspec main does not match any




Solution : I resolved this by renaming my branch to main:
git branch -M main

Error 2: Merge Conflict with Remote Repository
When I tried to push again, I encountered this error:
! [rejected]        main -> main (fetch first)


![Screenshot 2025-04-29 202902](https://github.com/user-attachments/assets/630c5871-b17d-43d6-9e2e-c76e489e689b)



Solution : I pulled the remote changes and merged them with my local changes:
git pull origin main --allow-unrelated-histories

After resolving these issues, I successfully pushed my code to GitHub.

## Lessons Learned
Building this project taught me several valuable lessons:

1. Problem-Solving : Debugging Git errors helped me understand version control better.
2. GUI Development : Using tkinter gave me hands-on experience with GUI programming.
3. Documentation : Writing detailed documentation improved my ability to explain my thought process and solutions.
4. Attention to Detail : Testing edge cases (e.g., empty passwords, very long passwords) ensured the program worked reliably.
