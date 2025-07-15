def recommend_roles(skills):
    roles = set()

    skill_set = set(skills)

    if {"python", "machine learning", "data analysis", "pandas", "numpy"} & skill_set:
        roles.add("Data Scientist")

    if {"html", "css", "javascript"} & skill_set:
        roles.add("Frontend Developer")

    if {"python", "flask", "django"} & skill_set:
        roles.add("Backend Developer")

    if {"sql", "mysql", "database"} & skill_set:
        roles.add("Database Administrator")

    if {"java", "c++"} & skill_set:
        roles.add("Software Developer")

    if not roles:
        roles.add("General Tech Enthusiast")

    return list(roles)
