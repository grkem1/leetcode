# https://leetcode.com/problems/generate-random-point-in-a-circle

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        p_radius = self.radius * (random.uniform(0,1)**0.5)
        p_angle  = random.uniform(0,2*math.pi)
        return [self.x_center+math.cos(p_angle)*p_radius,self.y_center+math.sin(p_angle)*p_radius]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()