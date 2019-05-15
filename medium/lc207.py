## course scheduler


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Algorithm DFS:
        1. initialize two boolean list.(fixed size)
        2. iterate prerequistes and built a hash map:
            key: course:
            value: a set of precourse
        3. recursively check if course not in visited, check if it's prerequests in stack or not.


        1. set up a dict
            key: course
            value: a set of precourse
        2. initialize a stack with first course
        3. while stack is not empty:
            put the precourse of curr course into stack,
                if precourse is in stack, return False
                else: continue
        4. return True if stack is empty
        """
        def isCyclic(c, visited, stack):
            visited[c] = True
            stack[c] = True
            # print(c)
            # print(visited)
            # print(stack)
            if c in dic:
                for pre in dic[c]:
                    if visited[pre] == False:
                        if isCyclic(pre, visited, stack) == True:
                            return True
                    elif stack[pre] == True:
                        return True
            stack[c] = False
            return False

        if prerequisites:
            dic = {}
            for pair in prerequisites:
                course = pair[0]
                pre_co = pair[1]
                if course in dic:
                    dic[course].add(pre_co)
                else:
                    dic[course] = {pre_co}
            # print(dic)

            visited = [False] * numCourses
            stack = [False] * numCourses

            for i in range(numCourses):
                if isCyclic(i, visited, stack) == True:
                    return False
        return True
