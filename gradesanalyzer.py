import matplotlib.pyplot as plt
from collections import Counter

def extract_info(input_file):
    grades = []
    keywordToSearch={
        "RIMANDATO": 0, "POSTPONED": 0,
        "ASSENTE": -1, "ABSENT": -1,
        "NON": -2, "NOT": -2
    }

    with open(input_file, 'r') as infile:
        for line in infile:
            parts = line.strip().split()
            if(len(parts)>0):
              grade = parts[1]
              if(grade.isdigit()):
                grades.append(int(grade))
              elif (grade in keywordToSearch):
                grades.append(keywordToSearch[grade])
    grades.sort()
    return grades

def plot_grades(grades):
    count = Counter(grades)

    label_map = {-1: 'ABSENT', 0: 'POSTPONED', -2: 'NOT'}
    labels = [label_map.get(k, str(k)) for k in count.keys()]
    values = list(count.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Result')
    plt.xticks(rotation=45)
    plt.ylabel('Frequency')
    plt.title('Exam Results')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def calculate_average(grades):
    valide_grades = list(filter(lambda x: x >= 18, grades))
    return sum(valide_grades) / len(valide_grades) if valide_grades else 0

def main():
    plot_grades(extract_info('prova.txt'))

    grades = extract_info('prova.txt')  
    average = calculate_average(grades)
    print(average)

if __name__ == "__main__":
    main()
