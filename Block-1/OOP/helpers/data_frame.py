import statistics

class DataFrame():
    def __init__(self, column, fill_value=0) -> None:
        self.column = column
        self.fill_value = fill_value
        self.fill_missed()
        self.to_float()
        
    def fill_missed(self):
        for i, value in enumerate(self.column):
            if value is None or value == '':
                self.column[i] = self.fill_value
    
    def to_float(self):
        self.column = [float(value) for value in self.column]
    
    def median(self):
        return statistics.median(self.column)
    
    def mean(self):
        return statistics.mean(self.column)
    
    def deviation(self):
        return statistics.stdev(self.column)