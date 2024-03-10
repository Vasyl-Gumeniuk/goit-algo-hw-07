class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        """
        Додає новий вузол до дерева зі значенням val.
        
        Параметри:
            val: Значення для вставки.
            
        Повертає:
            self: Корінь оновленого дерева.
        """
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
        return self

    def find_min(self):
        """
        Знаходить найменше значення у двійковому дереві пошуку (BST).
        
        Повертає:
            Значення найменшого вузла у дереві.
        """
        if self.left is None:
            return self.val
        return self.left.find_min()


def main():
    nodes = [10, 5, 15, 3, 7, 12, 20]
    root = TreeNode(nodes[0])
    for val in nodes[1:]:
        root.insert(val)

    # Використовуємо метод .find_min для знаходження найменшого значення у BST
    min_bst = root.find_min()
    print(f"Найменше значення у BST: {min_bst}")



if __name__ == "__main__":
    main()
