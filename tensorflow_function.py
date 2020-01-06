import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# tf.add: 덧셈
# tf.subtract: 뺄셈
# tf.multiply: 곱셈
# tf.truediv: 나눗셈의 몫
# tf.mod: 나눗셈의 나머지
# tf.abs: 절대값

sess = tf.Session()
a = tf.constant(17)
b = tf.constant(5)

# 덧셈
c = tf.add(a, b)
print(sess.run(c))
# 뺄셈
c = tf.subtract(a, b)
print(sess.run(c))
# 곱셈
c = tf.multiply(a, b)
print(sess.run(c))
# 나눗셈 몫
c = tf.truediv(a, b)
print(sess.run(c))
# 나눗셈 나머지
c = tf.mod(a, b)
print(sess.run(c))
# 절대값
c = tf.abs(-a)
print(sess.run(c))

