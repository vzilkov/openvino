import os
os.system('clear')
#os.system('ls')

path = 'src/bindings/python/tests/test_onnx'

test_names = ["test_sce_NCd1d2d3d4d5_mean_weight_cpu", #Segmentation fault error
"test_sce_NCd1d2d3d4d5_mean_weight_log_prob_cpu", #Segmentation fault error
"test_sce_NCd1d2d3_none_no_weight_negative_ii_cpu", #RuntimeError: z node not found in graph cache
"test_sce_NCd1d2d3_none_no_weight_negative_ii_log_prob_cpu", # RuntimeError: z node not found in graph cache
"test_sce_NCd1d2d3d4d5_none_no_weight_cpu", #RuntimeError: z node not found in graph cache
"test_sce_NCd1d2d3d4d5_none_no_weight_log_prob_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_3d_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_3d_log_prob_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_log_prob_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_no_weight_ii_3d_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_no_weight_ii_3d_log_prob_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_no_weight_ii_4d_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_no_weight_ii_4d_log_prob_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_no_weight_ii_cpu", #RuntimeError: z node not found in graph cache
"test_sce_mean_no_weight_ii_log_prob_cpu", #RuntimeError: z node not found in graph cache
"test_sce_none_cpu", #RuntimeError: z node not found in graph cache
"test_sce_none_log_prob_cpu", #RuntimeError: z node not found in graph cache
"test_sce_sum_cpu", #RuntimeError: z node not found in graph cache
"test_sce_sum_log_prob_cpu"] #RuntimeError: z node not found in graph cache
#platform linux -- Python 3.8.10, pytest-4.6.9, py-1.8.1, pluggy-0.13.0
#rootdir: /home/vzilkov/openvino/src/bindings/python
#src/bindings/python/tests/test_onnx/test_backend.py x

for test_name in test_names:
	print("Test name: ", test_name)
	os.system('pytest-3 %s/test_backend.py -k "%s" -s -runxfail'%(path,test_name))
	#pytest-3 src/bindings/python/tests/test_onnx/test_backend.py -k "test_sce_NCd1d2d3d4d5_mean_weight_cpu" -s -runxfail

print("***Testing ended***")