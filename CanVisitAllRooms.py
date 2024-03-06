class CanVisitAllRooms:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visitedRooms = {0}
        keys = rooms[0]
        while len(keys)>0:
            key = keys.pop(0)
            visitedRooms.add(key)
            for new_key in rooms[key]:
                if new_key not in visitedRooms:
                    keys.append(new_key)
        return len(visitedRooms)>=len(rooms)