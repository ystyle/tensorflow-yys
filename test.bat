@echo off
python image_retraining/label_image.py --image images/test_jpg/yysstreet/20170429175943.jpg --graph data/retrained_graph.pd --labels data/retrained_labels.txt
pause