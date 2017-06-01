import tensorflow as tf
from PIL import Image


def read_and_decode(filename, batch_size):
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
    print('xxxx: ', img.get_shape())
    img = tf.reshape(img, [512, 144, 3])
    img = tf.cast(img, tf.float32) * (1. / 255) - 0.5
    label = tf.cast(features['label'], tf.int32)
    image_batch, label_batch = tf.train.batch([img, label],
                                              batch_size=batch_size,
                                              num_threads=64,
                                              capacity=2000)
    return image_batch, tf.reshape(label_batch, [batch_size])


filename = "yys_train.tfrecords"
image_batch, label_batch = read_and_decode(filename, 20)

with tf.Session() as sess:
    i = 0
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    try:
        while not coord.should_stop() and i < 1:
            # just plot one batch size
            image, label = sess.run([image_batch, label_batch])
            # plot_images(image, label)
            print(label[0], image[0])
            i += 1

    except tf.errors.OutOfRangeError:
        print('done!')
    finally:
        coord.request_stop()
    coord.join(threads)




# for serialized_example in tf.python_io.tf_record_iterator(filename):
#     example = tf.train.Example()
#     example.ParseFromString(serialized_example)
#
#     label = example.features.feature['label'].int64_list.value
#     image = example.features.feature['img_raw'].bytes_list.value[0]
#     print(label, image)
