i = 0

def choices():
    global i
    user_choice = 'Rock'
    cpu_choice = 'Rock'

    if user_choice == cpu_choice:
        if i > 2:
            return [user_choice, cpu_choice]
        i += 1
        choices()


answer = choices()
print(answer[0] + answer[1])
