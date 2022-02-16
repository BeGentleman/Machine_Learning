借助工具flatc

下载schema.fbs（tensorflow lite的）

格式：
flatc -t schema.fbs -- 目标tflite文件
如：
flatc -t schema.fbs -- face_model_v5.tflite
