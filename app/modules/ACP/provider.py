from modules.ACP.controller.ACPController import ACPController
from modules.ACP.service.ACPService import ACPService
from modules.ACP.repository.ACPRepository import ACPRepository
from modules.ACP.view.CategoriesView import CategoriesView


class ACPProvider:

    @staticmethod
    def getResources():
        return {
            ACPController: (ACPService,),
            ACPService: (ACPRepository,),
            ACPRepository: (),
            CategoriesView: ('modules/ACP/categories.html')
        }