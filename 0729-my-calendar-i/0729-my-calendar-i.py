class MyCalendar:

    def __init__(self):
        self.events =[]        

    def book(self, start: int, end: int) -> bool:
        env = sorted(self.events)
        for s,e in env:
            if not (e<= start or end <= s):
                return False
        self.events.append([start, end])
        return True
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)