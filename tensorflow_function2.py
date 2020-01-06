import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.constant(17.5)
b = tf.constant(5.0)
sess = tf.Session()


# 음수를 반환
c = tf.negative(a)
print(sess.run(c))
# 부호를 반환(음수:-1, 양수:1, 0:0)
c = tf.sign(a)
print(sess.run(c))
# 제곱을 수행
c = tf.square(a)
print(sess.run(c))
# 제곱근을 반환
c = tf.sqrt(a)
print(sess.run(c))
# 거듭제곱을 수행
c = tf.pow(a, 2)
print(sess.run(c))
# 더 큰 값을 반환
c = tf.maximum(a, b)
print(sess.run(c))
# 더 작은 값을 반환
c = tf.minimum(a, b)
print(sess.run(c))
# 지수 값을 계산
c = tf.exp(b)
print(sess.run(c))
# 로그 값을 계산
c = tf.log(b)
print(sess.run(c))
# sin
c = tf.sin(b)
print(sess.run(c))
# cos
c = tf.cos(b)
print(sess.run(c))