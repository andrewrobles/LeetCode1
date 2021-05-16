def nodeDepths(root, depth=0):
    if root is None:
        return 0

    leftSum = nodeDepths(root.left, depth + 1)
    rightSum = nodeDepths(root.right, depth + 1)

    return depth + leftSum + rightSum