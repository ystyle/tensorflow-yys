python retrain.py \
--bottleneck_dir=bottlenecks \
--how_many_training_steps 500 \
--mode_dir=inception
--output_graph=retrained_graph.pd \
--output_labels=retrained_labels.txt \
--image_dir ../train_jpg

python label_image.py \
--image ..\test_jpg\ChooseKingofGhosts\201704291810.jpg \
--num_top_predictions 3 \
--graph retrained_graph.pd \
--labels retrained_labels.txt
