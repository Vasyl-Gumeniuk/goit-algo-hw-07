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

    def sum_values(self):
        """
        Знаходить суму всіх значень у двійковому дереві пошуку (BST).
        
        Повертає:
            Суму всіх значень у дереві.
        """
        total = self.val
        if self.left:
            total += self.left.sum_values()
        if self.right:
            total += self.right.sum_values()
        return total


def main():
    nodes = [10, 5, 15, 3, 7, 12, 20]
    root = TreeNode(nodes[0])
    for val in nodes[1:]:
        root.insert(val)

    # Використовуємо метод .sum_values для знаходження суми усіх значень у BST
    sum_bst = root.sum_values()
    print(f"Сума всіх значень у BST: {sum_bst}")



if __name__ == "__main__":
    main()
