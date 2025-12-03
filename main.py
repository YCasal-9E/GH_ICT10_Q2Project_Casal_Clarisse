from pyscript import display, document, HTML

def calculateGWA(e):
    subjects = ["Filipino", "English", "Social Studies", "Math", "Science", "ICT"] #  list w subjects
    units = (3, 5, 3, 5, 5, 2) #  tuple w units

    #  collecting student info from input fields
    fname= document.getElementById('student-fname').value
    lname= document.getElementById('student-lname').value
    section= document.getElementById('section').value
    info = fname + " " + lname + " - " + section

    #  collecting grade inputs
    filipino = document.getElementById("filipino").value
    english = document.getElementById("english").value
    ss = document.getElementById("social-studies").value
    science = document.getElementById("science").value
    math = document.getElementById("math").value
    ict = document.getElementById("ict").value

    #  to reveal result only when button is clicked
    document.getElementById("diva2").style.display = "block"
    document.getElementById("diva3").style.display = "block"

    #  validation: checking if any field is empty
    if (fname == "" or lname == "" or section == "" or filipino == "" or 
        english == "" or ss == "" or science == "" or math == "" or ict == ""):
        display("Please complete all information.", target="diva3", append=False)
        return
    gwa = round((float(filipino) + float(english) + float(ss) + float(science) + float(math) + float(ict)) / 6, 2)  #  computing gwa (mean of all grades)
    
    summary = (
        f"Filipino: {filipino}\n"
        f"English: {english}\n"
        f"Social Studies: {ss}\n"
        f"Math: {math}\n"
        f"Science: {science}\n"
        f"ICT: {ict}\n"
    )

    #  output results to page
    display(info, target="diva2", append=False)
    display(summary, target="diva2")
    display(f"General Weighted Average: {gwa}", target="diva2", append=True)


def show_clubs(e):
    #  dictionary containing all club info
    clubs = {
        "Math Club": {
            "Description": "A club for students who enjoy solving challenging math problems, preparing for math competitions, and exploring advanced mathematical concepts.",
            "Meeting Time": "Every Monday 2:30-4:00 PM",
            "Location": "Room 711",
            "Club Moderator": "Mr. Veracion",
            "Number of Members": 30
        },
        "Science Club": {
            "Description": "Hands-on experiments, science fair projects, environmental studies, and STEM-based challenges for curious thinkers.",
            "Meeting Time": "Every Tuesday 3:00–5:30 PM",
            "Location": "Science Lab",
            "Club Moderator": "Mr. Castro",
            "Number of Members": 25
        },
        "Theatre Club": {
            "Description": "A club for students passionate about acting, directing, script writing, stage design, and live performance production.",
            "Meeting Time": "Every Wednesday 2:00–4:30 PM",
            "Location": "School Auditorium",
            "Club Moderator": "Ms. Chenoweth",
            "Number of Members": 25
        },
        "Robotics": {
            "Description": "Students design, build, and program robots for competitions while enhancing skills in coding and teamwork.",
            "Meeting Time": "Every Thursday 3:30–5:00 PM",
            "Location": "Room 607",
            "Club Moderator": "Ms. Pasco",
            "Number of Members": 18
        },
        "Volleyball Varsity": {
            "Description": "A club for students interested in learning volleyball skills, participating in team drills, and even a chance to compete against other professional teams.",
            "Meeting Time": "Every Friday 2:30–5:00 PM",
            "Location": "School Gym",
            "Club Moderator": "Ms. Lynch",
            "Number of Members": 30
        },
        "Basketball Varsity": {
            "Description": "Students practice basketball fundamentals, develop teamwork, and participate in school tournaments.",
            "Meeting Time": "Every Monday 2:00–5:00 PM",
            "Location": "School Gym",
            "Club Moderator": "Mr. Tatum",
            "Number of Members": 30
        }
    }

    #  getting selected club from dropdown menu
    selected = document.getElementById("club-select").value


    info = clubs[selected]  #  club info for display
    output = f"""
        <h4>{selected}</h4>
        <p><b>Description:</b> {info['Description']}</p>
        <p><b>Meeting Time:</b> {info['Meeting Time']}</p>
        <p><b>Location:</b> {info['Location']}</p>
        <p><b>Club Moderator:</b> {info['Club Moderator']}</p>
        <p><b>Number of Members:</b> {info['Number of Members']}</p>
    """
    display(HTML(output), target="diva2", append=False)  #  displaying results in output

