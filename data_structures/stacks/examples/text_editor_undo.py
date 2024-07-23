import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from stacks.stack import Stack


class TextEditor:
    def __init__(self) -> None:
        self.text = ""
        self.undo_stack = Stack()

    def write(self, text: str) -> None:
        self.text += text
        self.undo_stack.push(f"Undo: Delete {len(text)} characters")

    def delete(self, num_characters: int) -> None:
        if num_characters > len(self.text):
            print("Cannot delete more characters than present in the text.")
            return

        deleted_text = self.text[-num_characters:]
        self.text = self.text[:-num_characters]
        self.undo_stack.push(f"Undo: Add {deleted_text}")

    def undo(self) -> None:
        if self.undo_stack.is_empty():
            print("Nothing to undo.")
            return

        action = self.undo_stack.pop()
        if action.startswith("Undo: Delete"):
            num_characters = int(action.split()[-2])
            self.text = self.text[:-num_characters]
        elif action.startswith("Undo: Add"):
            text = action.split()[-1]
            self.text += text

    def display(self) -> None:
        print("Text:", self.text)


editor = TextEditor()
editor.write("Hello")
editor.write(" World")
editor.display()  # Output: Current text: Hello World
editor.delete(1)
editor.display()  # Output: Current text: Hello Worl
editor.undo()
editor.display()  # Output: Current text: Hello World
editor.undo()
editor.display()  # Output: Current text: Hello
