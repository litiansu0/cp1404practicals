# project_management.py
from project import Project
import datetime

def load_projects(filename="projects.txt"):
    projects = []
    try:
        with open(filename, "r") as file:
            next(file)  # Skip header
            for line in file:
                parts = line.strip().split('\t')
                project = Project(
                    parts[0], parts[1], parts[2], parts[3], parts[4]
                )
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return projects

def save_projects(projects, filename="projects.txt"):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            line = (
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                f"{project.priority}\t{project.cost}\t{project.completion}\n"
            )
            file.write(line)
    print(f"Projects saved to {filename}")

def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_completed()], key=lambda x: x.priority)
    complete = sorted([p for p in projects if p.is_completed()], key=lambda x: x.priority)
    
    print("\nIncomplete projects: ")
    for project in incomplete:
        print(f"  {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, "
              f"priority {project.priority}, estimate: ${project.cost:.2f}, "
              f"completion: {project.completion}%")
    
    print("\nCompleted projects: ")
    for project in complete:
        print(f"  {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, "
              f"priority {project.priority}, estimate: ${project.cost:.2f}, "
              f"completion: {project.completion}%")

def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered = sorted([p for p in projects if p.start_date > filter_date], key=lambda x: x.start_date)
        print()
        for project in filtered:
            print(f"{project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, "
                  f"priority {project.priority}, estimate: ${project.cost:.2f}, "
                  f"completion: {project.completion}%")
    except ValueError:
        print("Invalid date format!")

def add_project(projects):
    print("\nLet's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    completion = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost.lstrip('$'), completion))
    print()

def update_project(projects):
    print()
    for i, project in enumerate(projects):
        print(f"{i} {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, "
              f"priority {project.priority}, estimate: ${project.cost:.2f}, "
              f"completion: {project.completion}%")
    try:
        index = int(input("\nProject choice: "))
        project = projects[index]
        print(f"{project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, "
              f"priority {project.priority}, estimate: ${project.cost:.2f}, "
              f"completion: {project.completion}%")
        
        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")
        
        if new_completion:
            project.completion = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
        print()
    except (ValueError, IndexError):
        print("Invalid input\n")

def display_menu():
    print("\n- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit")

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    while True:
        display_menu()
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Enter filename (default: projects.txt): ") or "projects.txt"
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename (default: projects.txt): ") or "projects.txt"
            save_projects(projects, filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            if input("\nWould you like to save to projects.txt? ").lower().startswith('n'):
                print("Thank you for using custom-built project management software.")
                break
            save_projects(projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()