import numpy as np
import matplotlib
from PIL import Image
import time

def test_time(fn):
    def wrapper(*args):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        print(f"\nВремя работы: {dt} сек")
    return wrapper

def kmeans(Input, K, Max_iters):

    N, D = np.shape(Input)
    R = np.random.permutation(N)
    Kvec = Input[R[0:K], :]
    Distance = np.zeros((N, K))

    for nn in range(0, Max_iters):
        F = np.zeros((N, K))
        for kk in range(0, K):
            Distance[:, kk] = np.sum(np.square(Input - np.tile(Kvec[kk, :],
                                                               (N, 1)), dtype=np.float64), axis=1 )
        Dmin = Distance.argmin(axis=1) % Distance.shape[1]
        for mm in range(0,K):
            if np.size(Dmin[mm == Dmin]) >0:
                Kvec[mm,:] = np.mean(Input[mm == Dmin], axis=0)
        for ii in range(0,N):
            F[ii, Dmin[ii]] = 1
        error = sum(sum((F*Distance)/N))
        print('Error = ' + str(error))
    return Kvec, Dmin


@test_time
def Compressor(requestedFile, K, maxIters):

    datain = np.asarray(Image.open(requestedFile), dtype=np.float64)
    reshapedData = np.reshape(datain, (np.size(datain, 0) * np.size(datain, 1), np.size(datain, 2)))

    if K <= 64:
        Kvec, Dmin = kmeans(reshapedData, K, maxIters)
        Dvec = np.zeros((len(Dmin), len(Kvec[0, :])))
        for jj in range(0, K):
            Dvec[jj == Dmin, :] = Kvec[jj, :]
        imout = np.reshape(np.uint8(Dvec), (np.size(datain, 0), np.size(datain, 1), len(Kvec[0, :])))
        im = Image.fromarray(imout, 'RGB')
        im.show()
        if (K <= 256 and maxIters == 5):
            if ((requestedFile == "imageExample1.jpg") or (requestedFile == "imageExample2.jpg") or
                (requestedFile == "imageExample3.jpg") or (requestedFile == "imageExample4.jpg") or
                    (requestedFile == "imageExample5.jpg")):
                savePattern = f"Image Examples/imageExampleIters{maxIters}K{K}.jpg"
            else:
                savePattern = f"Scikit Compressor/outputK{K}.jpg"
        else:
            savePattern = f"K-means Compressor/outputIters{maxIters}K{K}.jpg"
        im.save(savePattern, "JPEG", optimize=True)
