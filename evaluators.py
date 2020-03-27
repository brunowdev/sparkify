import uuid

from pyspark.ml.evaluation import Evaluator

class FNR(Evaluator):
    
    def __init__(self, predictionCol = 'prediction', labelCol = 'label'):
        self.predictionCol = predictionCol
        self.labelCol = labelCol
        self.uid = str(uuid.uuid4())

    def evaluate(self, dataset):
        
        tp = dataset.where((dataset[self.labelCol] == 1) & (dataset[self.predictionCol] == 1)).count()
        fp = dataset.where((dataset[self.labelCol] == 0) & (dataset[self.predictionCol] == 1)).count()
        tn = dataset.where((dataset[self.labelCol] == 0) & (dataset[self.predictionCol] == 0)).count()
        fn = dataset.where((dataset[self.labelCol] == 1) & (dataset[self.predictionCol] == 0)).count()
        
        fnr = fn / (1 if (tp + fn) == 0 else (tp + fn))
        
        return fnr

    def isLargerBetter(self):
        return False
    
    
class F1score(Evaluator):

    def __init__(self, predictionCol = 'prediction', labelCol = 'label'):
        self.predictionCol = predictionCol
        self.labelCol = labelCol
        self.uid = str(uuid.uuid4())

    def evaluate(self, dataset):
        
        tp = dataset.where((dataset[self.labelCol] == 1) & (dataset[self.predictionCol] == 1)).count()
        fp = dataset.where((dataset[self.labelCol] == 0) & (dataset[self.predictionCol] == 1)).count()
        tn = dataset.where((dataset[self.labelCol] == 0) & (dataset[self.predictionCol] == 0)).count()
        fn = dataset.where((dataset[self.labelCol] == 1) & (dataset[self.predictionCol] == 0)).count()
        
        precision = tp / (1 if (tp + fp) == 0 else (tp + fp))
        recall = tp / (1 if (tp + fn) == 0 else (tp + fn))

        f1 = 2 * precision * recall / (1 if (precision + recall) == 0 else (precision + recall))
        
        return f1

    def isLargerBetter(self):
        return True