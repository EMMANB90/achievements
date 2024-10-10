class TextEditor:
    def __init__(self):
        self.document = []
        self.undo_stack = []
        self.redo_stack = []
        self.change_queue = []

    def add_text(self, text):
        self.document.append(text)
        self.undo_stack.append(('add', text))
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            action, text = self.undo_stack.pop()
            if action == 'add':
                self.document.remove(text)
                self.redo_stack.append((action, text))

    def redo(self):
        if self.redo_stack:
            action, text = self.redo_stack.pop()
            if action == 'add':
                self.document.append(text)
                self.undo_stack.append((action, text))

    def batch_process_changes(self):
        while self.change_queue:
            change = self.change_queue.pop(0)
            self.add_text(change)

editor = TextEditor()
editor.add_text("Hello, world!")
editor.add_text("This is a text editor.")
editor.undo()
editor.undo()
editor.redo()

editor.change_queue.append("Batch change 1")
editor.change_queue.append("Batch change 2")
editor.batch_process_changes()
print(editor.document)
