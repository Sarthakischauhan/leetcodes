class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # we always start from the 0th element. 
        visited = [0]
        q = deque([0])
        while q:
            current = q.popleft()
            for key in rooms[current]:
                if (key not in visited):
                    q.append(key)
                    visited.append(key)
        
        return len(visited) == len(rooms

# Apparently, this was supposed to be easy. Wasn't  really apparent to me

