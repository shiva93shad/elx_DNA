import numpy as np

# Read input data
def read_input_data(path_to_file):
    X = []
    with open(path_to_file, "r") as f:
        content = f.readlines()
        for line in content:
            triplets = line.split()
            X.append(triplets)

    if path_to_file[-1] == "s":
        data = np.array(X).astype(int)
    else:
        data = np.array(X).astype(float)

    return data


# Check if data have the correct format (expected '.s' or '.f' file
def check_data_fromat(input_file1, input_file2):
    if (input_file1[-1] and input_file1[-1]) in ("s", "f"):
        pass
    else:
        print("Warning: Please enter the data in correct format")
        print('Only data in ".s" or ".f" are accepted')


# Give the indices of a segment's region
def find_indices_segment(seg):
    t = np.zeros(10000000)
    for i in range(0, len(seg)):
        t[seg[i, 0] : seg[i, 1]] = 1
    seg_file_indices = np.where(t == 1)[0]

    return seg_file_indices


# Calculate pearson correlation coefficient (pcc)
def calculate_pcc(func1, func2):
    f1_ = func1 - np.mean(func1)
    f2_ = func2 - np.mean(func2)
    tm = np.sum(f1_ * f2_)
    tms = np.sqrt(np.sum(np.power(f1_, 2))) * np.sqrt(np.sum(np.power(f2_, 2)))
    pcc = tm / tms

    return pcc


# Class related to the input files
class Elixir:
    def __init__(self, path_to_file1, path_to_file2):
        self.path_to_file1 = path_to_file1
        self.path_to_file2 = path_to_file2

    def read_data(self):
        check_data_fromat(self.path_to_file1, self.path_to_file2)
        self.data1 = read_input_data(self.path_to_file1)
        self.data2 = read_input_data(self.path_to_file2)

    def find_region_overlap(
        self,
    ):  # Find and indicate the overlap between regions of two SEGMENTs
        if self.path_to_file1[-1] == "s" and self.path_to_file2[-1] == "s":
            self.read_data()
            seg1 = find_indices_segment(self.data1)
            seg2 = find_indices_segment(self.data2)
            self.region_overlap = np.intersect1d(seg1, seg2)
        else:
            self.region_overlap = 'Warning: Both inputs must be in "SEGEMENT" formant'

    def pearson_corr_coef(self):  # Indicate pcc of two FUNCTIONs
        if self.path_to_file1[-1] == "f" and self.path_to_file2[-1] == "f":
            self.read_data()
            pcc = calculate_pcc(self.data1, self.data2)
            self.pearson_correlation_coefficient = pcc
        else:
            self.pearson_correlation_coefficient = (
                "Warning: In order to calculate "
                'Pearson Correlation Coefficient, both inputs must be in "FUNCTION" formant'
            )

    def seg_func_mean(
        self,
    ):  # Calculate and indicate the mean of FUNCTION corresponding to the SEGMENT
        if self.path_to_file1[-1] == "s" and self.path_to_file2[-1] == "f":
            self.read_data()
            indices = find_indices_segment(self.data1)
            sgf = np.mean(self.data2[indices])
            self.segment_function_mean = f"Segment-Function mean is: {sgf}"
        else:
            self.segment_function_mean = (
                "Warning: SEGMENT file and FUNCTION file must be entered, respectively"
            )
