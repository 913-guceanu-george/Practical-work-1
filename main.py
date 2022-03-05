from src.Repo.repo import Repository
from src.UI.userinterface import UI


def __main__():

    repo = Repository()
    ui = UI(repo)
    ui.menu()

    while True:
        usr = ui.user()
        if usr == '1':
            ui.menu()
        elif usr == '2':
            ui.numberofVertices()
        elif usr == '3':
            ui.printVertices()
        elif usr == '4':
            ui.iterForward()
        elif usr == '5':
            ui.iterBackwards()
        elif usr == '6':
            ui.resetIter()
        elif usr == '':
            continue
        elif usr == '0':
            return


__main__()
