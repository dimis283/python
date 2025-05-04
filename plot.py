import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Διαβάζουμε το CSV
df = pd.read_csv("projects.csv")

# 2. Δημιουργούμε το Bar plot με Seaborn
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="type", palette="viridis")  # Προαιρετικό: palette="viridis", "Set2", κλπ.

# 3. Προσθέτουμε τίτλους και labels
plt.title("Count of Each Type", fontsize=15)
plt.xlabel("Type", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=45)

# 4. Εμφάνιση γραφήματος
plt.tight_layout()
plt.show()