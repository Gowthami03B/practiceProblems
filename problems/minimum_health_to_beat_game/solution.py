class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        #you use armor when max damage happens
        #you can't use armor when damage > armor
        #you cannot subtract armor bcs armor helps neutralize damage but armor is not subtracted
        return sum(damage) - min(max(damage),armor)  + 1
        