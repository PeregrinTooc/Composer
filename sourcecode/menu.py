import composer

class menuFactory(object):
    _instance = None    
    @staticmethod
    def getFactory():
        if menuFactory._instance is None:
            menuFactory._instance = menuFactory()
        return menuFactory._instance

    def __init__(self):
        self.Menu = Menu()
    
    def getMenu(self):
        return self.Menu

class Menu(object):
    def __init__(self):
        self._setAvailableFunctions()
        self._composerFactory = composer.composerFactory.getFactory()
        self._composerFactory.createAll()
        
    def _setAvailableFunctions(self):
        self.availableFunctions = { 
            **dict.fromkeys(['E', 'e' ], self._exit), 
            **dict.fromkeys(['F', 'f'], self._findComposer),
            **dict.fromkeys(['S', 's'], self._showOptions),
            **dict.fromkeys(['D', 'd'], self._displayAll)
        }
    
    def _exit(self):
        print('Goodbye! Until Next Time!')   
        exit()  

    def _findComposer(self):
        pass #TODO: Implement Me!

    def _raiseInvalidInput(self):
        print('Please Choose a Valid Option')

    def _showOptions(self):
        print('Find Composer(F)')
        print('Display All(D)')
        print('Exit(E)')
        print('Show Options(S)')

    def _displayAll(self):
        self._composerFactory.displayAll()

    def mainMenu(self):
        print('\nHello User. This is the main menu. Please choose one of the following by typing the characters in brackets:\n')
        self._showOptions()

    def getActionFromUser(self):
        cInput = input('\nChoose Action\n')[0]
        try:
            fWhatToDo = self.availableFunctions[cInput]        
        except KeyError:
            fWhatToDo = self._raiseInvalidInput
        return fWhatToDo

                