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

## Loading TFRecord file

Createa a function to parse the incoming serialized data.
```
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
```
 
 Load TFRecord or TFRecords into a dataset via *tf.data.TFRecordDataset*.
```
dataset = tf.data.TFRecordDataset('tfrecords/model.tfrecords')
```
Map each element to parsing function to convert binary file into formatted and readable.
```
dataset = dataset.map(lambda input: parse(input[0]))
```
Make an Iterator on the dataset.
```
iterator = dataset.make_one_shot_iterator().get_next()
```
