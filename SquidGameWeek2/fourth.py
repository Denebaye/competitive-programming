class Solution:
    def racecar(self, target_distance):
        target_distance *= -1
        racecar_queue, visited = [(0, 0, -1)], {(0, -1)}
        while racecar_queue:
            move_count, current_position, velocity = heapq.heappop(racecar_queue)
            if current_position == target_distance:
                return move_count
            elif current_position > 20000 or -20000 > current_position:
                continue
            next_pos_vel = (current_position + velocity, velocity * 2)
            if next_pos_vel not in visited:
                heapq.heappush(racecar_queue, (move_count + 1, current_position + velocity, velocity * 2))
                visited.add(next_pos_vel)
            if velocity < 0 and (current_position, 1) not in visited:
                heapq.heappush(racecar_queue, (move_count + 1, current_position, 1))
                visited.add((current_position, 1))
            elif velocity > 0 and (current_position, -1) not in visited:
                heapq.heappush(racecar_queue, (move_count + 1, current_position, -1))
                visited.add((current_position, -1))
