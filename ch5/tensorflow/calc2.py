import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

calc1_op = a + b * c
calc2_op = (a + b) * c

sess = tf.Session()
res1 = sess.run(calc1_op)
print(res1)
res2 = sess.run(calc2_op)
print(res2)