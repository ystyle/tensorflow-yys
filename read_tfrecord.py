import tensorflow as tf
from PIL import Image  # 注意Image,后面会用到, pillow

file = 'train'
cwd = 'D:\\Code\\Python\\yys\\yys1_' + file + ".tfrecords"


def read_and_decode(filename):
    # 根据文件名生成一个队列
    filename_queue = tf.train.string_input_producer([filename])
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)  # 返回文件名和文件
    features = tf.parse_single_example(
        serialized_example,
        features={
            'label': tf.FixedLenFeature([], tf.int64),
            'img_raw': tf.FixedLenFeature([], tf.string),
        }
    )
    img = tf.decode_raw(features['img_raw'], tf.uint8)
    img = tf.reshape(img, [128, 72])
    img = tf.cast(img, tf.float32) * (1. / 255) - 0.5
    # label = tf.cast(features['label'], tf.int32)
    # print(img, label)
    label = features['label']
    image = features['img_raw']
    return label, image, img


filename = "yys_train.tfrecords"
label, image, img = read_and_decode(filename)

sess = tf.Session()

init = tf.global_variables_initializer()
sess.run(init)
tf.train.start_queue_runners(sess=sess)

label_val_1, image_val_1 = sess.run([label, image])
print(label_val_1, image_val_1)


# for serialized_example in tf.python_io.tf_record_iterator(filename):
#     example = tf.train.Example()
#     example.ParseFromString(serialized_example)
#
#     label = example.features.feature['label'].int64_list.value
#     image = example.features.feature['img_raw'].bytes_list.value[0]
#     print(label, image)
