class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for file_portion in path.split("/"):

            if file_portion == "..":
                if stack:
                    stack.pop()
            elif file_portion == "." or not file_portion:
                continue
            else:
                stack.append(file_portion)

        simplified_file_path = "/" + "/".join(stack)
        return simplified_file_path
