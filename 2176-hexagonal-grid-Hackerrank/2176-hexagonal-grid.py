def solve(problem):
    if not problem:
        return True

    if len(problem) == 1 and not problem[0]:
        return False
    elif len(problem) == 1 and problem[0]:
        return True
    
    if problem[0]:
        return solve(problem[1:])
    if not problem[0] and not problem[1]:
        return solve(problem[2:])
    if not problem[0] and len(problem) > 2 and not problem[2]:
        return solve(problem[3:])

    return False

for i in range(int(input())):
    int(input()) # Pass, not interesting
    first_row = [int(i) for i in str(input())] 
    second_row = [int(i) for i in str(input())] 
    row = [i for tupl in zip(first_row, second_row) for i in tupl]
    if solve(row):
        print('YES')
    else:
        print('NO')


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna