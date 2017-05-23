#coding:utf-8
import tensorflow as tf

images = ['test/ChooseKingofGhosts/201704291810.png',
'test/Enterthenightofghosts/201704291803.png',
'test/exorcism/2017042917270.png']

# change this as you see fit
image_path = tf.placeholder(tf.string)

def get_image(image_path):
    return tf.image.convert_image_dtype(
            tf.image.decode_png(tf.read_file(image_path), channels=3),
            dtype=tf.uint8)

# Read in the image_data
# image_data = tf.gfile.FastGFile(image_path, 'rb').read()
#
# image = Image.open(image_path)
# image_array = image.convert('RGB')
image_array = get_image(image_path)

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
    in tf.gfile.GFile("image_retraining/retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("image_retraining/retrained_graph.pd", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    for i in range(3):
        print("\n----------------------------------------------",i)
        print('预测图片：%s' %(images[i]))
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        image_test = sess.run([image_array], feed_dict={image_path:images[i]})
        predictions = sess.run(softmax_tensor,{'DecodeJpeg:0': image_test[0]})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            print('%s (score = %.5f)' % (human_string, score))
