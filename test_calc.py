# coding: utf-8
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def main(x):

	# 平均値
	mean = np.mean(x)
	print("平均値: " + str(mean))

	# 中央値
	median = np.median(x)
	print("中央値: " + str(median))

	# 最頻値
	vals, counts = stats.mode(x)
	print("最頻値: " + str(vals[0]))
	print("最頻数: " + str(counts[0]))

	# 分散
	var = np.var(x)
	print("分散: " + str(var))

	# 標準偏差
	std = np.std(x)
	print("標準偏差: " + str(std))

	#第一四分位値
	q1 = stats.scoreatpercentile(x, 25)
	print("第一四分位: " + str(q1))

	#第三四分位値
	q3 = stats.scoreatpercentile(x, 75)
	print("第三四分位: " + str(q3))

	# ヒストグラム表示
	plt.hist(x)
	plt.show()

if __name__ == '__main__':
	x = [100, 20 ,2 ,2, 2, 3, 4, 5]
	y = [1, 2 ,2 ,3, 3, 3, 4, 4, 5]
	test = [55, 40, 18, 63, 77, 35, 24, 56, 44, 53, 46, 53]

	#main(x)
	#main(y)
	main(test)

	# 平均 50, 標準偏差 10 の正規乱数を1,000件生成
	#z = np.random.normal(50, 10, 1000)

	# ヒストグラムを出力
	#plt.hist(z)
	#plt.show()




