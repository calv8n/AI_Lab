class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def create_tree(root_value, branching_factor, depth):
    if depth == 0:
        return None
    root = TreeNode(root_value)
    for i in range(branching_factor):
        child_value = f"{root_value}.{i+1}"
        child = create_tree(child_value, branching_factor, depth - 1)
        if child:
            root.children.append(child)
    return root


def print_tree(root, indent=""):
    print(indent + str(root.value))
    for child in root.children:
        print_tree(child, indent + "  ")


def depth_limited_dfs(node, target, depth_limit):
    if depth_limit == 0:
        return None
    if node.value == target:
        return node
    for child in node.children:
        result = depth_limited_dfs(child, target, depth_limit - 1)
        if result:
            return result
    return None


def iterative_deepening_search(root, target, max_depth):
    for depth_limit in range(max_depth + 1):
        result = depth_limited_dfs(root, target, depth_limit)
        if result:
            return result
    return None


branching_factor = int(input("Enter Branching Factor"))
depth = int(input("Enter Depth"))
root = create_tree("Root", branching_factor, depth)
print_tree(root)

target_value = input("Enter taget value in format Root.x.y")
max_search_depth = depth

result_node = iterative_deepening_search(root, target_value, max_search_depth)

if result_node:
    print(f"Node '{target_value}' found in the tree.")
else:
    print(f"Node '{target_value}' not found in the tree.")
