from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        num_fruits = 0
        window_start = 0
        counter = defaultdict(int)
        
        for window_end in range(len(fruits)):
            
            right = fruits[window_end]
            counter[right] += 1
            
            while len(counter) > 2:
                left = fruits[window_start]
                counter[left] -= 1
                if counter[left] == 0:
                    del counter[left]
                window_start += 1
                
            num_fruits = max(num_fruits, window_end - window_start + 1)
        return num_fruits