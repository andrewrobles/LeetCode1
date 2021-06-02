def nodeDepths(root, depth=0):
    """
    Write a function that returns the sum of
    it's node's depths
    """
    if root is None:
        return 0

    leftSum = nodeDepths(root.left, depth + 1)
    rightSum = nodeDepths(root.right, depth + 1)

    return depth + leftSum + rightSum