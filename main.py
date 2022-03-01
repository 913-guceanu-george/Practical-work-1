from src.UI.userinterface import UI
from src.Repo.repo import TxtRepo


def main():

    repo = TxtRepo()
    ui = UI(repo)

    ui.welcome()
    ui.menu()
    while True:
        usr_input = ui.user()
        if usr_input == '1':
            ui.menu()
        elif usr_input == '2':
            ui.printNumberOfVertices()
        elif usr_input == '3':
            ui.printVertices()
        elif usr_input == '4':
            ui.iterateVertices()
        elif usr_input == '5':
            ui.iterateVerticesBackwards()
        elif usr_input == '6':
            return
        else:
            ui.wrong_input()


main()
