import h5py
import numpy as np

# Create a new HDF5 file
with h5py.File('sample_hdf5_file.h5', 'w') as file:
    # Create a 1D dataset at the root level
    data1 = np.arange(10)
    dataset1 = file.create_dataset('dataset1', data=data1)
    dataset1.attrs['description'] = '1D dataset of integers'
    
    # Create a group and a 2D dataset within it
    group1 = file.create_group('group1')
    data2 = np.random.rand(5, 5)
    dataset2 = group1.create_dataset('dataset2', data=data2)
    dataset2.attrs['description'] = '2D dataset of random floats'
    
    # Create a subgroup and a 3D dataset within it
    subgroup1 = group1.create_group('subgroup1')
    data3 = np.random.randint(0, 100, size=(3, 3, 3))
    dataset3 = subgroup1.create_dataset('dataset3', data=data3)
    dataset3.attrs['description'] = '3D dataset of random integers'
    
    # Create another group with a scalar dataset
    group2 = file.create_group('group2')
    data4 = np.float32(42.0)
    dataset4 = group2.create_dataset('dataset4', data=data4)
    dataset4.attrs['description'] = 'Scalar dataset with a single float value'
    
    # Create a dataset with strings
    data5 = np.array([b'Hello', b'World', b'from', b'HDF5'], dtype='S10')
    dataset5 = group2.create_dataset('dataset5', data=data5)
    dataset5.attrs['description'] = 'Dataset with fixed-length strings'
    
    # Create a dataset with a compound data type (structured array)
    dtype = np.dtype([('field1', np.int32), ('field2', np.float32)])
    data6 = np.array([(1, 2.5), (3, 4.5), (5, 6.5)], dtype=dtype)
    dataset6 = group2.create_dataset('dataset6', data=data6)
    dataset6.attrs['description'] = 'Dataset with a compound data type'

    # Add attributes to the root group
    file.attrs['title'] = 'Sample HDF5 File'
    file.attrs['author'] = 'ChatGPT'
    file.attrs['description'] = 'This file demonstrates the structure of an HDF5 file.'

    # Add attributes to groups
    group1.attrs['description'] = 'This is group1 containing subgroup1 and dataset2'
    group2.attrs['description'] = 'This is group2 containing dataset4, dataset5, and dataset6'
    subgroup1.attrs['description'] = 'This is subgroup1 inside group1 containing dataset3'
