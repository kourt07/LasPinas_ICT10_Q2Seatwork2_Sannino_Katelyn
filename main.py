from pyscript import document

def calculate_gwa(event):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    grades = [
        float(document.getElementById("science").value or 0),
        float(document.getElementById("math").value or 0),
        float(document.getElementById("english").value or 0),
        float(document.getElementById("filipino").value or 0),
        float(document.getElementById("ict").value or 0),
        float(document.getElementById("pe").value or 0)
    ]

    subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]

   
    gwa = sum(grades) / len(grades)

  
    info = f"<b>Name:</b> {fname} {lname}<br><br>"
    for i in range(len(subjects)):
        info += f"{subjects[i]}: {grades[i]}<br>"

    document.getElementById("output").innerHTML = info
    document.getElementById("averageBox").innerText = f"Your general weighted average is {gwa:.2f}"

 
    result = "You passed!" if gwa >= 75 else "You failed."
    document.getElementById("resultBox").innerText = result
