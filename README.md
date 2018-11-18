# tfrecords


## Saving to TFRecords

Create a file writer and set export path.
```
writer = tf.python_io.TFRecordWriter(file_path)
```
Map your data into a features map by converting to the right data type and then formatting a Feature dictionary.

```
features = {'x':tf.train.Feature(float_list=tf.train.FloatList(value=[data['x']])),
     'y':tf.train.Feature(float_list=tf.train.FloatList(value=[data['y']])),
     'z':tf.train.Feature(float_list=tf.train.FloatList(value=[data['z']]))}
     
feature_list = tf.train.Features(feature=features)
```

Using *tf.train.Example* to create serialized data to save and export.
```
serial_data = tf.train.Example(features=feature_list).SerializeToString()
```

Write the serial data out and close the writer.
```
writer.write(serial_data)
writer.close()
```
