import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Φόρτωση δεδομένων
df = pd.read_csv("Dataset_Malawi_National_Football_Team_Matches.csv")  # Αντιγράψε τα δεδομένα σου σε ένα αρχείο CSV

# Ομαδοποίηση ανά Competition και Result
results = df.groupby(['Competition', 'Result']).size().unstack(fill_value=0)
print(results)
colors = {'Win': '#4CAF50', 'Loss': '#F44336', 'Draw': '#FFC107'}

# Δημιουργία plot
ax = results.plot(kind='bar', stacked=True, 
                 color=[colors.get(x, '#333333') for x in results.columns],
                 figsize=(12, 7))

# Ρύθμιση γραφήματος
plt.title("Αποτελέσματα Μαλάουι ανά Διοργάνωση", fontsize=14, fontweight='bold')
plt.xlabel("Διοργάνωση", fontsize=12)
plt.ylabel("Αριθμός Αγώνων", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title="Αποτέλεσμα", bbox_to_anchor=(1.05, 1), loc='upper left')

# Προσθήκη τιμών
for c in ax.containers:
    ax.bar_label(c, label_type='center', fmt='%d', color='white', fontweight='bold')

plt.tight_layout()
plt.show()