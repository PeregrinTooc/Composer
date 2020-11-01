import menu


def initialize():
    global oMenu
    oFactory = menu.menuFactory.getFactory()
    oMenu = oFactory.getMenu()
    oMenu.mainMenu()

def main():
    initialize()
    while True:
        fWhatToDo = oMenu.getActionFromUser()
        fWhatToDo()

if __name__ == "__main__":
    main()