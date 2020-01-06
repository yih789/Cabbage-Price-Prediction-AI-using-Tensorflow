import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# tf.constant 배열의 형태를 갖는 tensor 자료형
a = tf.constant(1)
b = tf.constant(2)
c = tf.add(a, b)

sess = tf.Session()
print(sess.run(c))
print(c)