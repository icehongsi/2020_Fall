def reorderLogFiles(self, logs):
    digit, alpha = [], []
    for i in logs:
        if i.split(" ")[1].isdigit():
            digit.append(i)
        else: alpha.append(i)
    alpha.sort(key = lambda x: (x.split(" ")[1:], x.split(" ")[9]))
    return alpha + digit