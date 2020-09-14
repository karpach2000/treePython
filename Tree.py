import json
class Tree:

    def detour(self, tree):
        """Выводит в консоль пары ключ - значения для всех не конечных элементов древа 
        значение для конечных элементов
        при работе с массивами конечным элементом является каждый элемент массива"""
        __type = str(type(tree))
        #print(__type)
        if __type == "<class 'dict'>":
            items = tree.items()
            for key, value in items: 
                print(key, '>>>' ,str(value))
                if str(type(value)) != "<class 'str'>":
                    self.detour(value)

        elif __type == "<class 'list'>":
            for element in tree:
                self.detour(element)
        elif __type == "<class 'str'>":
            print(tree)
        else:
            print("ERROR")




def main():
    data = {"samolet" : {"krilo": "white", "stabilizator": "black"}, "vertolet": "green", "pilots": ["Vasa", "Petr", "Victor", {"Android" : {"cpu": "intel", "gpu": "nvidia"}}]}
    tree = Tree()  # Новый экземпляр QApplication
    tree.detour(data)



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()