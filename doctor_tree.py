
class DoctorNode:
    """Represents a doctor in the reporting structure."""

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    """Manages the doctor reporting hierarchy."""

    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side, current_node=None):
        if self.root is None:
            print("Tree is empty. Add a lead doctor first.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == parent_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = DoctorNode(doctor_name)
                    print(f"{doctor_name} added to the LEFT of {parent_name}")
                    return True
                print(f"Error: {parent_name} already has a LEFT report.")
                return False

            elif side == "right":
                if current_node.right is None:
                    current_node.right = DoctorNode(doctor_name)
                    print(f"{doctor_name} added to the RIGHT of {parent_name}")
                    return True
                print(f"Error: {parent_name} already has a RIGHT report.")
                return False

            print("Error: Invalid side. Enter left or right.")
            return False

        if current_node.left is not None:
            if self.insert(parent_name, doctor_name, side, current_node.left):
                return True

        if current_node.right is not None:
            if self.insert(parent_name, doctor_name, side, current_node.right):
                return True

        if current_node == self.root:
            print(f"Error: Parent doctor {parent_name} was not found.")

        return False

    def preorder(self, node):
        if node is None:
            return []

        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result

    def inorder(self, node):
        if node is None:
            return []

        result = self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)
        return result

    def postorder(self, node):
        if node is None:
            return []

        result = self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)
        return result


# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("\nPreorder:")
    print(tree.preorder(tree.root))

    print("\nInorder:")
    print(tree.inorder(tree.root))

    print("\nPostorder:")
    print(tree.postorder(tree.root))

    print("\nTesting an invalid parent:")
    tree.insert("Dr. Unknown", "Dr. Smith", "left")

    print("\nTesting an invalid side:")
    tree.insert("Dr. Croft", "Dr. Smith", "middle")

    print("\nTesting an occupied position:")
    tree.insert("Dr. Croft", "Dr. Smith", "left")
