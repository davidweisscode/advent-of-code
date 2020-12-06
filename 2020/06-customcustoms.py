import pandas as pd

def get_groups():
    inputstr = ""
    with open("06-input.txt", "r") as file:
        for line in file:
            inputstr += line
        groups = inputstr.split("\n\n")
        for i, group in enumerate(groups):
            groups[i] = group.split("\n")
        return groups

# --- Part 1 --- For each group, count the number of questions (a-z) to which anyone answered "yes". What is the sum of those counts?

def get_count_anyone(group):
    questions = set()
    for person in group:
        for question in person:
            questions.add(question)
    return len(questions)

# --- Part 2 --- For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

def get_count_everyone(group):
    df = pd.DataFrame(columns=list("abcdefghijklmnopqrstuvwxyz"))
    for _ in group:
        df = df.append(pd.Series(), ignore_index=True)
    for i, person in enumerate(group):
        for question in person:
            df.at[i, question] = 1
    return df[df.columns[~df.isnull().any()]].shape[1]

if __name__ == '__main__':
    groups = get_groups()
    sum_anyone = 0
    sum_everyone = 0
    for group in groups:
        sum_anyone += get_count_anyone(group)
        sum_everyone += get_count_everyone(group)
    print(f"The sum of questions anyone answered with 'Yes' is {sum_anyone}")
    print(f"The sum of questions everyone answered with 'Yes' is {sum_everyone}")
