### Example: python3 elixir_task.py 'data/' 'testfile_a.s' 'testfile_b.f' 'seg_func_mean'

"""
The code includes the following:
1- Showing input data (show_data)
2- Finding region overlap between two SEGMENTS (region_overlap)
3- Calculating Pearson Correlation Coefficient of two FUNCTIONs (pearson_corr_coef)
4- Calculating the mean of FUNCTION corresponding to the SEGMENT (seg_func_mean) 
"""
from elixir import Elixir
import argparse


def main(task, path, filename1, filename2):
    path_to_file1 = path + filename1
    path_to_file2 = path + filename2
    el = Elixir(path_to_file1, path_to_file2)
    if task == "show_data":
        el.read_data()
        print(el.data1)
        print(el.data2)

    elif task == "region_overlap":
        el.find_region_overlap()
        print(el.region_overlap)

    elif task == "pearson_corr_coef":
        el.pearson_corr_coef()
        print(el.pearson_correlation_coefficient)

    elif task == "seg_func_mean":
        el.seg_func_mean()
        print(el.segment_function_mean)

    else:
        print(
            "Enter the correct task: show_data, region_overlap, pearson_corr_coef, seg_func_mean"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to your input data")
    parser.add_argument("filename1", type=str, help="Enter the first file")
    parser.add_argument("filename2", type=str, help="Enter the second file")
    parser.add_argument(
        "task",
        type=str,
        help="Enter the task: show_data, region_overlap, pearson_corr_coef, seg_func_mean",
    )

    args = parser.parse_args()

    main(args.task, args.path, args.filename1, args.filename2)
