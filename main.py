## History
## 1. Finished CRUD in locally:
## 2. Finished CRUD with db data.json: AI review score 7.5/10 comment-> DRY load file every point


## AI recomment to me next steps:

# 1. Professional Error Handling (Defensive Coding) -> Currently, your app crashes if the user types a letter instead of a number for an ID, or if the data.json file gets deleted.
# -> The Task: Learn how to use try-except blocks properly to catch specific errors like ValueError (for bad inputs) and FileNotFoundError.
# -> The Goal: Make your program "un-crashable." No matter what the user types, the program should stay running. : finished



# 2. Introduce Object-Oriented Programming (OOP) -> Right now, you are using Functional Programming (writing separate functions). Professional Python developers use Classes to group data and logic together.
# -> The Task: Create a TodoItem class and a TodoManager class. : finished
# -> The Goal: Instead of handling dictionaries directly, you will handle "Objects." This makes your code much easier to read as it grows larger.

# 3. Move to a Real Database (SQLite) -> JSON is great for small projects, but in the real world, we use SQL (Structured Query Language). Python has a built-in library called sqlite3.
#

import json
import os
import datetime

def time_helper():
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

def integer_helper():
    while True:
        try:
            return int(input("Enter ID: "))
        except ValueError:
            print("Error: Enter a valid integer for ID.")

class TodoList:
    def __init__(self, db_path="data.json"):
        self.db_path = db_path
        self.data = self._load_file()
        # self.tasks stays linked dynamically to self.data["todo"]
        self.tasks = self.data["todo"] 

    # Internal helper denoted by "_"
    def _load_file(self):
        try:
            if not os.path.exists(self.db_path) or os.path.getsize(self.db_path) == 0:
                default = {"todo": []}
                self._save_to_disk(default)
                return default
            with open(self.db_path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("File syntax error. Resetting layout.")
            return {"todo": []}
        except Exception as e:
            print(f"Error opening file: {e}")
            return {"todo": []}

    def _save_to_disk(self, message=None):
        try:
            with open(self.db_path, "w") as file:
                json.dump(self.data, file, indent=4)
            if message:
                print(message)
        except Exception as e:
            print(f"Error saving file: {e}")

    def _find_item(self, item_id):
        return next((item for item in self.tasks if item["id"] == item_id), None)

    def create_todo(self):
        title = input("Title: ")
        description = input("Description: ")
        
        new_id = max([item["id"] for item in self.tasks]) + 1 if self.tasks else 1
        new_content = {
            "id": new_id,
            "title": title,
            "description": description,
            "created_at": time_helper()
        }
        
        self.tasks.append(new_content)
        self._save_to_disk("Content uploaded successfully.")

    def get_all_todo(self):
        if not self.tasks:
            print("No todos found.")
            return
        for item in self.tasks:
            print(item)

    def get_todo_by_id(self, item_id):
        item = self._find_item(item_id)
        print(item if item else "Content not found!")

    def update_todo_by_id(self, item_id):
        item = self._find_item(item_id)
        if not item:
            print("Content not found!")
            return

        new_title = input("New title (Leave blank to keep): ")
        new_desc = input("New description (Leave blank to keep): ")

        if new_title.strip():
            item["title"] = new_title
        if new_desc.strip():
            item["description"] = new_desc
            
        item["updated_at"] = time_helper()
        self._save_to_disk("Content successfully updated!")

    def delete_todo_by_id(self, item_id):
        item = self._find_item(item_id)
        if not item:
            print("Content not found!")
            return

        self.tasks.remove(item)
        self._save_to_disk("Content was successfully deleted!")


def select_do():
    # CRITICAL: Instantiate ONCE so state is preserved in memory
    todo_manager = TodoList()

    while True:
        try:
            selected = int(input("\nSelect: 1|Create, 2|GetById, 3|GetAll, 4|Update, 5|Delete, 0|Stop -> "))

            if selected == 1:
                todo_manager.create_todo()
            elif selected == 2:
                todo_manager.get_todo_by_id(integer_helper())
            elif selected == 3:
                todo_manager.get_all_todo()
            elif selected == 4:
                todo_manager.update_todo_by_id(integer_helper())
            elif selected == 5:
                todo_manager.delete_todo_by_id(integer_helper())
            elif selected == 0:
                print("Exiting.")
                break
            else:
                print("Incorrect command")
        except ValueError:
            print("Please input a valid integer.")

if __name__ == "__main__":
    # select_do()
    print("")

#     2. Обнаружение устройств в сети (Host Discovery)
# Если вы подключились к новому Wi-Fi и хотите узнать, какие еще устройства (смартфоны, роутеры, принтеры) к нему подключены, nmap может «пропинговать» весь диапазон адресов и показать список всех активных устройств.

# 3. Определение операционной системы (OS Detection)
# По тому, как именно устройство отвечает на сетевые запросы (у каждой ОС свои уникальные нюансы в реализации сетевого стека TCP/IP), nmap может с высокой точностью угадать, что работает на целевом компьютере: Windows, Linux, macOS, iOS или вообще прошивка от роутера Cisco.

# 4. Определение версий программ (Version Detection)
# nmap не просто скажет «порт 22 открыт». Он может заглянуть глубже и определить, какая конкретно программа там запущена (например, OpenSSH 8.2p1). Это критически важно, так как старые версии программ могут содержать известные уязвимости.