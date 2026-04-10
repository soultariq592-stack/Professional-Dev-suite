import datetime
import os

def generate_dev_report(name, skills):
    """
    Professional script to generate a technical profile summary.
    Demonstrates: Functions, Lists, File I/O, and String Formatting.
    """
    print(f"--- Generating Report for {name} ---")
    
    report_content = f"""
    TECHNICAL STATUS REPORT
    Generated on: {datetime.datetime.now()}
    Developer: {name}
    Current Tracks: {', '.join(skills)}
    
    Status: ADSE Module in Progress
    Platform: GitHub Certified Profile
    """
    
    try:
        with open("dev_report.txt", "w") as f:
            f.write(report_content)
        print("Success: dev_report.txt has been generated.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    my_skills = ["Python", "HTML", "Web3", "Data Analysis"]
    generate_dev_report("Saul Tariq", my_skills)
