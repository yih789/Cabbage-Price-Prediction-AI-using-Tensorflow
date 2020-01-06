import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 텐서플로우 데이터 처리 단위는 텐서(Tensor)이다.
# 일종의 다차원 배열의 객체
# tf.add(), tf.constant() 등의 명령어는 그래프를 정의한 것이고
# 실제 연산을 수행한 것은 아니다.
# 흐름을 만들어 동작시키기 위해 Session() 사용

a = tf.constant(17.5)
b = tf.constant(5.0)
c = tf.add(a, b)

# 값을 대입한 그래프가 동작하도록 한다.
sess = tf.Session()

print(c)
print(sess.run(c))
