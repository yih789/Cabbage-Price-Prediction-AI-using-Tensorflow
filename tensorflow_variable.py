import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.Variable(5)
b = tf.Variable(3)
c = tf.multiply(a, b)

# 변수 초기화 함수
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
print(sess.run(c))

a = tf.Variable(15)
c = tf.multiply(a, b)
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(c))