documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def first_function():
  doc_number = input("Введите пожалуйста номер документа: ")
  for paper in documents:
    if doc_number == paper["number"]: 
      print("Имя владельца: ", paper["name"])
      return
  print("Владелец не зарегистрирован")

def second_function():
  print("Список документов: \n")
  for paper in documents:
    print(paper.setdefault("type"), paper.setdefault("number"), paper.setdefault("name"))

def third_function():
  doc_number = input("Введите пожалуйста номер документа: ")
  for paper, shelf_position in directories.items():
    for doc in shelf_position:
      if doc == doc_number:
        print("Номер полки: ", paper)
  else: print("Документ не найден на полке")

def fourth_function():
  new_doc = {"type": None, "number": None, "name": None}
  print("Введите тип документа:")
  new_doc["type"] = input()
  print("Введите номер документа:")
  new_doc["number"] = input()
  print("Введите имя владельца документа:")
  new_doc["name"] = input()
  documents.append(new_doc)
  print("Новый документ: \n", new_doc, "\n")
  print("Обновленный список документов: \n", documents, "\n")
  print("Введите номер полки:")
  new_doc_1 = input()
  for i in directories:
    if new_doc_1 not in directories.keys():
      directories[new_doc_1] = list() 
  print(directories)

def fifth_function(documents):
    for document in documents:
        try:
            print(document["name"])
        except KeyError:
            print('Документ №{} не содержит поле "Имя"'.format(document["number"]))
  
print("Приветствую, ниже приведен список команд, а так же горячие клавиши для их выполнения. Обратите внимание, что команды вводятся латинскими буквами.\n" 
"except - команда для урока по исключениям; \n"
"p - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит; \n"
"l - команда, которая выведет список всех документов пользователей; \n"
"s - команда, которая спросит номер документа и выведет номер полки, на которой он находится; \n"
"a - команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться \n\n"
"Введите команду из списка:")

command = input()
if command == "p":
  first_function()
elif command == "l":
  second_function()
elif command == "s":
  third_function()
elif command == "a":
  fourth_function()
elif command == 'except':
  fifth_function(documents)