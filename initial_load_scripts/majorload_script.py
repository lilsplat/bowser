#majorload_script.py

MAJORS = [
    "Africana Studies",
    "American Studies",
    "Anthropology",
    "Art",
    "Astronomy",
    "Biological Chemistry",
    "Biological Sciences",
    "Cinema and Media Studies",
    "Chemistry",
    "Cognitive and Linguistic Sciences",
    "Classical Studies",
    "Comparative Literature",
    "Computer Science",
    "East Asian Languages and Cultures",
    "Economics",
    "Education",
    "English",
    "Environmental Studies",
    "French",
    "Geosciences",
    "German",
    "History",
    "Italian Studies",
    "Jewish Studies",
    "Mathematics",
    "Medieval Renaissance Studies",
    "Middle Eastern Studies",
    "Music",
    "Neuroscience",
    "Physical Education",
    "Peace and Justice Studies",
    "Philosophy",
    "Physics",
    "Political Science",
    "Psychology",
    "Quantitative Reasoning",
    "Religion",
    "Russian",
    "South Asia Studies",
    "Sociology",
    "Spanish",
    "Theatre Studies",
    "Women and Gender Studies",
    "Writing",
    "Other",
    "Undecided"
]



f = open('initial_major_load.json', 'w')
f.write('[\n')
x = 1
for major in MAJORS:
    f.write("  {\n")
    f.write("    \"model\": \"courses.major\",\n")
    f.write("    \"pk\": " + str(x) + ",\n")
    f.write("    \"fields\": {\n")
    f.write("      \"name\": \"" + major + "\"\n")
    f.write("    }\n")
    f.write("  },\n")
    x += 1

# f.write("]")
f.close()
