x=input()
X={}

for i in range(len(x)):
    X[x[i]]=i

print(X)

for key in X:
    print("{0}: {1}".format(key,X[key]))