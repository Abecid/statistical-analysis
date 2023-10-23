import pandas as pd

def main():
    with open("data/majors.json", "r") as file:
        data = pd.read_json(file)
    df = pd.DataFrame(data)

    # Extract columns as individual lists
    majors = df["Major"].tolist()
    salaries = df["Salary"].tolist()
    whites = df["White"].tolist()
    asians = df["Asian"].tolist()
    minorities = df["Minorities"].tolist()
    internationals = df["International"].tolist()
    
    correlations = df.corr()['Salary'][1:] 
    print(correlations)
    
    spearman_correlation_salary = df.corr(method='spearman')['Salary'][1:]
    print(spearman_correlation_salary)

if __name__ == "__main__":
    main()