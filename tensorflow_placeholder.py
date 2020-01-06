import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 다른 텐서를 할당하기 위해 사용
# 텐서는 다차원 배열 형태를 갖기 때문에
# 플레이스 홀더로 사용할 값에 배열도 들어갈 수 있다.

# tf.placeholder(dtype, shape, name)

# dtype: 플레이스 홀더에 저장되는 자료형
# shape: 배열의 차원
# name: 플레이스 홀더의 이름

input = [1, 2, 3, 4, 5]

x = tf.placeholder(dtype=tf.float32)
y = x + 5
sess = tf.Session()
print(sess.run(y, feed_dict={x: input}))
