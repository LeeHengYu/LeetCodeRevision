from sortedcontainers import SortedList
from collections import defaultdict
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fooddict = {} # food => (rating, cuisine)
        self.cuidict = defaultdict(SortedList)

        for f,c,r in zip(foods, cuisines, ratings):
            self.fooddict[f] = (r,c)
            self.cuidict[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        rate, cui = self.fooddict[food]
        self.fooddict[food] = (newRating, cui)
        self.cuidict[cui].remove((-rate, food))
        self.cuidict[cui].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuidict[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)