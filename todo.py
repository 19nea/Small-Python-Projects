
# add task function
def add_task():
    task = input('What task would you like to add? ')
    date = input('When is the deadline? ')
    importance = input('From a scale from 1-10 how important is this task? ')

    tasks = open('tasks.txt', 'a')
    tasks.write(f'Task: {task}, Date: {date}, Importance: {importance}\n')


# view task function
def view_task():

    f = open('tasks.txt', 'r')
    for l, line in enumerate(f):
        print(f'{l+1}. {line.strip()}')


# delete task function
def delete_task():
    line = int(input('what line would you like to delete?')) - \
        1  # so that we have the right index

    with open('tasks.txt', 'r') as f:
        lines = f.readlines()
        if 0 <= line < len(lines):
            del lines[line]
        else:
            print('invalid line number')
    with open('tasks.txt', 'w') as f:
        f.writelines(lines)


# Main loop to run the program until the user quits
while True:
    mode = input(
        # !!! only the q,a,v,d/Q,A,V,D will work!
        'Welcome to your todo list! What would you want to do? Quit(q), Add(a), View(v), Delete(d) ').lower()

    if mode == 'q':
        quit()
    if mode == 'a':
        add_task()
    if mode == 'v':
        view_task()
    if mode == 'd':
        delete_task()
