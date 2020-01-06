import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

xData = [1, 2, 3, 4, 5, 6, 7]
yData = [25000, 55000, 75000, 110000, 128000, 155000, 180000]
# W : 가설의 기울기(가중치)
# random_uniform은 랜덤한 하나의 수 (-100부터 100사이에)
W = tf.Variable(tf.random.uniform([1], -100, 100))
# b : y절편
b = tf.Variable(tf.random.uniform([1], -100, 100))
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
# 예측값 H
H = W * X + b
# 예측값 - 실제값의 제곱의 평균값
cost = tf.reduce_mean(tf.square(H-Y))
# a : 경사하강에서 점프하는 정도
a = tf.Variable(0.01)
# 텐서플로우에서 제공하는 경사하강 라이브러리
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost) # 비용을 최소화
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(5001):
    sess.run(train, feed_dict = {X: xData, Y: yData})
    if i % 500 == 0:
        print(i, sess.run(cost, feed_dict = {X: xData, Y: yData}), sess.run(W), sess.run(b))
print(sess.run(H, feed_dict = {X: (8)}))