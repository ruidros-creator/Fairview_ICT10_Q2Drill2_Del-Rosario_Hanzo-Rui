from pyscript import document

# 1. Predefine at least four sets of students
grade_7 = {"Alice Blue", "Anita Bath"}
grade_8 = {"Billy Sparks", "Eileen Dover"}
grade_9 = {"Ella Vator", "Emelita Evans"}
grade_10 = {"Francisco Portero", "Joe Kerr"}

# Initialize an empty set to hold dynamically added members
new_members = set()

def add_member(event):
    global new_members

    # 2. Retrieve user input from the text boxes
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()

    # Format the new input into a set
    current_input_set = {f"{first_name} {last_name}"}

    # 3. Use the set union operator (|) to update the new_members set
    new_members = new_members | current_input_set

    # 4. Use set operators to combine all predefined sets and new members into one master set
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_members

    # Format the output using an HTML line break instead of loops
    members_html = "<br>".join(master_set)
    
    # Calculate total members
    total_count = len(master_set)

    # 5. Output rendering using an f-string
    final_output = f"""
        <strong>ALL MEMBERS:</strong><br>
        {members_html}<br><br>
        <strong>TOTAL NUMBER OF MEMBERS:</strong> {total_count}
    """

    # Update the results on the webpage
    document.getElementById("output").innerHTML = final_output

    # Clear the text boxes for the next entry
    document.getElementById("fname").value = ""
    document.getElementById("lname").value = ""
