@echo off
python image_retraining/retrain.py --bottleneck_dir=data/bottlenecks --how_many_training_steps 500 --mode_dir=data/inception --output_graph=data/retrained_graph.pd --output_labels=data/retrained_labels.txt --image_dir images/train_jpg
pause