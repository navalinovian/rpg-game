from time import sleep
from tqdm import tqdm
from pick import pick
from tabulate import tabulate

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def gameplay():
    stats= [
        ["Name", "Azigauegr"],
        ["Health", 100],
        ["Mana", 100],
        ["Role", "Mage"],
        ["Speciality", "Shadow"]
    ]
    print(tabulate(stats, tablefmt='pretty'))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    title = 'Please choose your favorite programming language: '
    options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
    option, index = pick(options, title, indicator='=>', default_index=2)
    print(option, index)
    # for i in tqdm(range(10)):
    #     sleep(1)
    gameplay()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
