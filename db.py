db = [('Администрация города', "Главная", "true"), ("Администрация области", "Главная", "true"),
("Департамент финансов", "Администрация города", "true",), ("Департамент СХ", "Администрация области", "true"),
("Экономический отдел", "Департамент финансов", "false"), ("Транспортный отдел", "Департамент СХ", "false")]

class Category():
    def __init__(self,name, parent, childFlag):
        self.name = name
        self.parent = parent
        self.childFlag = childFlag
        self.childs = []
    def create_Hierarchy(self, categoryObjArr):
        if self.childFlag=='true':
            for item in categoryObjArr:
                if self.name == item.parent:
                    self.childs.append(item)
               
def create_categoryObjArr(db_list):
    categoryObjArr = []
    for item in db_list:
        newCategory = Category(item[0], item[1],item[2])
        categoryObjArr.append(newCategory)
    for obj in categoryObjArr:
        obj.create_Hierarchy(categoryObjArr)
    return categoryObjArr

categoryObjArr = create_categoryObjArr(db)

htmlBlock = ''
def create_htmlBlock(categoryObjArr):
    global htmlBlock
    for element in categoryObjArr:
        if not element.name in htmlBlock:
            htmlBlock += f'<div class=\'category\'> \n {element.name} \n'
            if element.childFlag == 'true':   
                create_htmlBlock(element.childs)
                htmlBlock += '</div> \n'
            else:
                htmlBlock += '</div> \n'
                
create_htmlBlock(categoryObjArr)
print(htmlBlock)



# htmlBlock = ''
# def createStructure(db):
#     global htmlBlock
#     for i in db:
#         if not i[0] in htmlBlock:
#             htmlBlock += f'<div> \n {i[0]} \n'
#             if i[2] == 'true':
#                 for child in db:
#                     if i[0] == child[1]:
#                         htmlBlock += f'<div> \n {child[0]} \n'
#             else:
#                 htmlBlock += '</div> \n'