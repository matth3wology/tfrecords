import tensorflow as tf

tf.reset_default_graph()

def parse(serialized_example):
    features = {
        'x':tf.FixedLenFeature([],tf.float32),
        'y':tf.FixedLenFeature([],tf.float32),
        'z':tf.FixedLenFeature([],tf.float32)
        }

    example = tf.parse_single_example(serialized_example,features)

    x = tf.cast(example['x'],tf.float32)
    y = tf.cast(example['y'],tf.float32)
    z = tf.cast(example['z'],tf.float32)

    return {'coordinates':[x,y,z]}

dataset = tf.data.TFRecordDataset('tfrecords/model.tfrecords')
dataset = dataset.repeat(1000)
dataset = dataset.batch(1)
dataset = dataset.map(lambda input: parse(input[0]))

iterator = dataset.make_one_shot_iterator().get_next()


with tf.Session() as sess:

    for i in range(5):

        out = sess.run(iterator)

        print(out)
