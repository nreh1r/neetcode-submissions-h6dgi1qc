class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sorted_piles = sorted(piles)
        l, r = 1, sorted_piles[-1]
        eating_rate = float("inf")
        # while l <= r:
        #     mid = (l + r) // 2

        #     value_to_check = sorted_piles[mid]
        #     print(f"l: {l}; r: {r}; mid: {mid}, ")
        #     can_finish, time = self.can_finish(value_to_check, piles, h)
        #     print(f"eating rate: {eating_rate}, can_finish: {can_finish}")
        #     if can_finish and time < h:
        #         r = mid - 1
        #         eating_rate = min(eating_rate, value_to_check)
                
        #         while can_finish and time <= h:
        #             new_rate = eating_rate - 1
        #             new_can_finish, new_time = self.can_finish(new_rate, piles, h)
        #             time = new_time
        #             can_finish = new_can_finish
        #             print(new_can_finish)
        #             if new_can_finish:
        #                 eating_rate = min(eating_rate, new_rate)

        #         return new_rate

        #     elif not can_finish:
        #         l = mid + 1
        #     else:
        #         return value_to_check
        
        # return eating_rate

        while l <= r:
            mid = (l + r) // 2

            # can_finish, time = self.can_finish(mid, piles, h)
            # NEW CODE
            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / mid)

            # END NEW CODE
            if time <= h:
                eating_rate = min(eating_rate, mid)
                r = mid - 1
            else :
                l = mid + 1

        return eating_rate
                


    
    def can_finish(self, eating_rate, piles, h):
        time = 0
        # for pile in piles:
            # while pile > 0:
            #     if time >= h:
            #         return False, -1
            #     pile -= eating_rate
            #     time += 1

        
        return True, time
