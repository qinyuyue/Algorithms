## Keys and rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        BFS Algorithm:
        1. initialize queue
        2. put the kyes in room 0 into the queue, and change rooms[queue[0]] to inf.
        3. iterate queue until queue is empty.
            if room i == 1000 + i, continue,
            else, change it to inf.
        4. iterate room again, if not inf, return False
            else, return True
        """
        queue = collections.deque()
        queue.extend(rooms[0])
        rooms[0] = float('inf')
        # print(queue)
        while queue:
            key = queue.popleft()
            # print(key)
            if rooms[key] == float('inf'):
                continue
            else:
                queue.extend(rooms[key])
                rooms[key] = float('inf')
        # print("queue: ", queue)
        # print("rooms: ", rooms)
        for i in rooms:
            if i !=  float('inf'):
                return False
        return True
