import tensorflow as tf
import yys_connect as adb
import time

# change this as you see fit
image_path = tf.placeholder(tf.string)
image_array = tf.image.convert_image_dtype(
        tf.image.decode_png(tf.read_file(image_path), channels=3),
        dtype=tf.uint8)

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
               in tf.gfile.GFile(r"data/retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile(r"data/retrained_graph.pd", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    adb.connect_adb()
    adb.show_devices()

    while True:
        print("\n----------------------------------------------")
        start = time.time()
        image = adb.cap()
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        image_test = sess.run([image_array], feed_dict={image_path: image})
        predictions = sess.run(softmax_tensor, {'DecodeJpeg:0': image_test[0]})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        label = label_lines[top_k[0]]
        print("预测图片为：%s(%s)" % (label, adb.Labels[label]))
        adb.click(label)
        print('耗时: %.3f' % (time.time()-start))
