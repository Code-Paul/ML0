# import class for model
from sklearn import tree

# import data from data.py for training
from data_25_only import Training_Data as tr_D
# from data import Training_Data as tr_D

# prepare data for training
Train_X = [[_[1],_[2]] for _ in tr_D]		# Data points
Train_Y = [_[0] for _ in tr_D]				# Labels

# create our model
model = tree.DecisionTreeClassifier()
model_title = "Decision Tree"

# train our model and update it
model = model.fit(Train_X, Train_Y)

# Let's test out model bu predicted the gender of a noble data point
# Expected: ["Male","Female","Male","Male","Female"]

to_predict = [
	[69.9384752593112,170.175853813004],
	[64.7436431302013,141.980646731978],
	[64.7398154829922,169.654054121188],
	[69.3084028803936,198.378693643572],
	[65.3971324673664,141.506019820105]
]
print(model.predict(to_predict))
