import ScikitKMeansCompressor

requestedFile = "input.jpg"
K = int(input("Введите количество цветов: "))
maxIters = int(input("Введите количество итераций: "))
print("\n")

ScikitKMeansCompressor.Compressor(requestedFile, K, maxIters)