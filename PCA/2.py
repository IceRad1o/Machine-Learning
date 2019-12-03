import numpy as np
 
#get number of users and movies
def GetNum():
    data_file = open("train.txt", 'r')
    numUser = 0
    numMovie = 0
    for line in data_file.readlines():
        line = line.split()
        userID = int(line[0])
        movieID = int(line[1])
        if numUser < userID:
            numUser = userID
        if numMovie < movieID:
            numMovie = movieID
    data_file.close()
    return numUser, numMovie
 
#Read data as a numUser x numMovie matrix.
#Rows are users and columns are movies.
def CreateDataMat():
    data_file = open("train.txt", 'r')
    rows, columns = GetNum()
    dataMat = np.zeros((rows, columns))
    dataMat_mask = np.zeros((rows, columns))
    for line in data_file.readlines():
        line = line.split()
        userID = int(line[0])
        movieID = int(line[1])
        rating = float(line[2])
        dataMat[userID - 1][movieID - 1] = rating
        dataMat_mask[userID - 1][movieID - 1] = 1
    data_file.close()
    return dataMat, dataMat_mask
 
#PCA Computation
def PCA(dataMat, Num):
    u, s, v = np.linalg.svd(dataMat, full_matrices = False)
    u_new = u[:,0:Num]
    v_new = v[0:Num,:]
    s_new = np.diag(s[0:Num])
    dataNew = np.dot(u_new, np.dot(s_new, v_new))
    return dataNew
 
##deal with scores-5.txt
data_train, mask = CreateDataMat()
iteration = 0
user_i, movie_j = GetNum()
while iteration < 100:
    iteration += 1
    print "iteration-5:",iteration
    data_pca = PCA(data_train, 5)
    for i in range(user_i):
        for j in range(movie_j):
            if mask[i][j] == 0:
                data_train[i][j] = data_pca[i][j]
 
#Output the result
data_index = open("test.txt", 'r')
data_output = file("scores-5.txt",'w')
rows, columns = GetNum()
for line in data_index.readlines():
    line = line.split()
    userID = int(line[0])
    movieID = int(line[1])
    ele = data_train[userID - 1][movieID - 1]
    ele = str(ele)
    data_output.write(ele[0:5])
    data_output.write('\n')
data_output.close()
data_index.close()
 
##deal with scores-20.txt
data_train, mask = CreateDataMat()
iteration = 0
user_i, movie_j = GetNum()
while iteration < 100:
    iteration += 1
    print "iteration-20:",iteration
    data_pca = PCA(data_train, 20)
    for i in range(user_i):
        for j in range(movie_j):
            if mask[i][j] == 0:
                data_train[i][j] = data_pca[i][j]
 
#Output the result
data_index = open("test.txt", 'r')
data_output = file("scores-20.txt",'w')
rows, columns = GetNum()
for line in data_index.readlines():
    line = line.split()
    userID = int(line[0])
    movieID = int(line[1])
    ele = data_train[userID - 1][movieID - 1]
    ele = str(ele)
    data_output.write(ele[0:5])
    data_output.write('\n')
data_output.close()
data_index.close()
 
##deal with scores-50.txt
data_train, mask = CreateDataMat()
iteration = 0
user_i, movie_j = GetNum()
while iteration < 100:
    iteration += 1
    print "iteration-50:",iteration
    data_pca = PCA(data_train, 50)
    for i in range(user_i):
        for j in range(movie_j):
            if mask[i][j] == 0:
                data_train[i][j] = data_pca[i][j]
 
#Output the result
data_index = open("test.txt", 'r')
data_output = file("scores-50.txt",'w')
rows, columns = GetNum()
for line in data_index.readlines():
    line = line.split()
    userID = int(line[0])
    movieID = int(line[1])
    ele = data_train[userID - 1][movieID - 1]
    ele = str(ele)
    data_output.write(ele[0:5])
    data_output.write('\n')
data_output.close()
data_index.close()

