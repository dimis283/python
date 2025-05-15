import sqlite3
import pandas as pd

# Σύνδεση με τη βάση
conn = sqlite3.connect('emp.database')

# Γράψε εδώ το SQL query σου (παράδειγμα)
query = """
SELECT Employee_Name, EmpID, GenderID, Department, Position, Salary, PerformanceScore, EmpSatisfaction, EmploymentStatus, Absences
FROM employees
WHERE PerformanceScore IN ('Exceeds', 'Fully Meets')
    AND Termd = 0
    AND Salary > 60000
    AND EmpSatisfaction >= 4;
"""

# Διάβασμα των αποτελεσμάτων του query με pandas
df = pd.read_sql_query(query, conn)

# Εξαγωγή σε CSV
output_csv = "exported_data.csv"
df.to_csv(output_csv, index=False, encoding='utf-8')

# Κλείσιμο σύνδεσης
conn.close()

print(f"Τα δεδομένα εξήχθησαν επιτυχώς στο αρχείο: {output_csv}")