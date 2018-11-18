import tensorflow as tf

flags = tf.app.flags
FLAGS = flags.FLAGS

flags.DEFINE_multi_string('export_path','tfrecords/model.tfrecords','Export data path for TF records.')
#flags.DEFINE_multi_string('dataset','images','Import data folder.')

def write_tf_file(data,file_path):
    writer = tf.python_io.TFRecordWriter(file_path)

    features = {'x':tf.train.Feature(float_list=tf.train.FloatList(value=[data['x']])),
        'y':tf.train.Feature(float_list=tf.train.FloatList(value=[data['y']])),
        'z':tf.train.Feature(float_list=tf.train.FloatList(value=[data['z']]))}

    feature_list = tf.train.Features(feature=features)

    serial_data = tf.train.Example(features=feature_list).SerializeToString()

    writer.write(serial_data)

    writer.close()


def main(_):
    f = FLAGS.export_path
    data = {"x":1.23,"y":4.02,"z":12.34}
    write_tf_file(data,f[0])

if __name__ == '__main__':
    tf.app.run(main)
